import sys
import win32com
import win32com.client as com_client
from logger import log
import win32net, win32security

DEFAULT_PASSWORD = r'1'
AD_GROUP_TYPES = {'global':-2147483646,'local':-2147483644}

def domain_name_to_disting(domain_name):
	return ','.join(['DC=%s' % name for name in domain_name.split('.')])

group_types	= {'global':-2147483646,'local':-2147483644}

def add_account_to_group_by_ADs(accountADs, groupADs):

	ad_group = find(group, disting)
	ad_account = find(account, disting)
	
	if(not ad_group.IsMember(ad_account.ADsPath)):
		ad_group.Add(ad_account.ADsPath)

	ad_group.SetInfo()

def add_account_to_group(account, group, domain_name):

	disting = domain_name_to_disting(domain_name)
	ad_account = find(account, disting)	
	
	groupDomain = disting
	groupDomainDist = disting 
	ad_group = None
	if (group.find("\\") != -1):
		groupDomain, group = group.split("\\")
		gd = groupDomain.upper()
		if gd == 'NT AUTHORITY' or gd == 'BUILTIN':
			ad_group = com_client.GetObject("LDAP://CN=%s,CN=Builtin,%s" % (group, disting))
		else:
			groupDomainDist = domain_name_to_disting(groupDomain)

	if not ad_group: ad_group = find(group, groupDomainDist)
		
	if(not ad_group.IsMember(ad_account.ADsPath)):				
		try:
			ad_group.Add(ad_account.ADsPath)
		except:			
			u_sid = win32security.SID(ad_account.objectSid)	
			ad_group.Add("LDAP://%s/<SID=%s>" % (groupDomain, str(u_sid)[6:]))		

	ad_group.SetInfo()

def add_group_to_group(group_child, group_parent, domain_name):
	disting = domain_name_to_disting(domain_name)
	ad_group_parent = find(group_parent, disting)
	ad_group_child = find(group_child, disting)

	if (not ad_group_parent.IsMember(ad_group_child.ADsPath)):
		ad_group_parent.Add(ad_group_child.ADsPath)
		ad_group_parent.SetInfo()

def getADObject(disting):
	return com_client.GetObject("LDAP://CN=Users,%s" % disting)

def create_group(group, domain_name, type = "Global"):
	disting = domain_name_to_disting(domain_name)
	type_num = group_types[type.lower().strip()]
	
	if account_exist(group, disting):
		newObject = find(group, disting)
	else:
		obj = getADObject(disting)
		objClass = "group"
		objRelativeName = "CN=%s" % group
		newObject = obj.Create(objClass, objRelativeName)
	
	newObject.Put("sAMAccountName", group)
	newObject.Put("groupType", type_num)
	newObject.SetInfo()
	return newObject

def wrap_user(user, psw):	
	user_first = user.split()[0]
	user_last = user.split()[-1]
	user_login = user
	return {'first':user_first, 'last':user_last ,'login':user_login, 'title':'Description', 'password':psw}

def delete_account(loging, domain_name, objClass = "user"):
	disting = domain_name_to_disting(domain_name)
	
	if account_exist(loging, disting):
		obj = getADObject(disting)
		objRelativeName = "CN=%s"%loging
		obj.Delete(objClass, objRelativeName)
		obj.SetInfo()
		return True
	return False
	
# splits the login in of standard formats, and returns it as (domain, user)


def SplitPrincipalName(principalName):
	if principalName.find('\\') < 0:
		raise Exception('Unknown principal name format')
	
	return principalName.split('\\')	

def FindAdPrincipal(domain, account):
	import win32com.client as wc	
	rootDse = wc.GetObject('LDAP://%s/RootDSE' % domain)
	
	namingContextStr = rootDse.get('defaultNamingContext')	
	namingContext = wc.GetObject('LDAP://%s/%s' % (domain, namingContextStr))

	adsPath = namingContext.AdsPath

	adoConnection = wc.Dispatch('ADODB.Connection')
	adoConnection.Provider='ADsDSOObject'
	adoConnection.Open('Active Directory Provider')

	adoCommand = wc.Dispatch('ADODB.Command')
	adoCommand.ActiveConnection = adoConnection
	adoQuery = "SELECT * FROM '%(adsPath)s' WHERE cn = '%(account)s'"	
	adoCommand.CommandText = adoQuery % {'adsPath':adsPath, 'account':account}
	log.Debug('adoCommand.CommandText = %s' % adoCommand.CommandText)
	
	recordSet, rowsAffected = adoCommand.Execute()
	userObj = None
	if not recordSet.EOF:
		userStr = recordSet.Fields.Item(0).value
		userObj = wc.GetObject(userStr)
		log.Debug('Ad object %s\%s found' % (domain, account))
	else:
		log.Debug('Ad object %s\%s not found' % (domain, account))
	
	return userObj

# This method needed as proxy due to sime syntactic fun of python
def RaiseException(msg):
	raise Exception(msg)
	
# This method initalizes ready Ad principal object, but does not save it to ad yet.
def InitAdPrincipal(domain, accountName, principalType='User', containerName = 'users'):
	import win32com.client as wc	
	rootDse = wc.GetObject('LDAP://%(domain)s/RootDSE' % {'domain':domain})
	namingContextStr = rootDse.get('defaultNamingContext')
	container = wc.GetObject('LDAP://%(domain)s/CN=%(containerName)s,%(namingContextStr)s' % {'domain':domain, 'containerName':containerName, 'namingContextStr':namingContextStr})
	principalObj = container.Create(principalType,'CN=%(account)s' %  {'account':accountName})	
	return principalObj

def InitUserParams(principalObj, accountName, displayName, password):	
	principalObj.displayName = displayName or accountName			
	principalObj.setpassword(password)
	principalObj.AccountDisabled = False
	principalObj.sAMAccountName = accountName
	return principalObj
	
def InitGroupParams(principalObj, accountName, displayName, groupType):	
	principalObj.displayName = displayName or accountName			
	principalObj.groupType = AD_GROUP_TYPES[groupType]	
	principalObj.sAMAccountName = accountName
	return principalObj
	
def InitContactParams(principalObj):
	# If you want to add some parameters to the Contact object... do it yourself
	return principalObj

# This method will return existing Active Directory principal object, or create a new one
def CreateAdPrincipal(principalName, principalType = 'User', displayName = None, groupType='local', password = DEFAULT_PASSWORD):	
	log.Debug('principalType = %s' % principalType)
	
	domainName, accountName = SplitPrincipalName(principalName)
	
	principalObj = FindAdPrincipal(domainName, accountName) or InitAdPrincipal(domainName, accountName, principalType)	
	principalObj.SetInfo() #before setting parameters the object must be saved into Ad
	
	if principalType.lower().find('user') >= 0:
		principalObj = InitUserParams(principalObj, accountName, displayName, password)
	elif principalType.lower().find('group') >= 0:				
		principalObj = InitGroupParams(principalObj, accountName, displayName, groupType)	
	elif principalType.lower().find('contact') >= 0:
		principalObj = InitContactParams(principalObj)
		
	principalObj.SetInfo()
	return True

def AddPrincipalToGroup(principalName, groupName):
	domainName, accountName = SplitPrincipalName(principalName)
	groupDomainName, groupAccountName = SplitPrincipalName(groupName)
	principalObj = FindAdPrincipal(domainName, accountName)
	groupObj = FindAdPrincipal(groupDomainName, groupAccountName)
	
	principalObj or RaiseException('The principal not found')
	groupObj or RaiseException('The group not found')
	
	if groupObj.IsMember(principalObj.ADsPath) != True:			
		groupObj.Add(principalObj.ADsPath)
		groupObj.SetInfo()
	
def create_user(loging, domain_name, psw=DEFAULT_PASSWORD, display_name=None):
	if not display_name: display_name = loging
	user = wrap_user(loging, psw)
	log.Debug('user = %s' % str(user))
	disting = domain_name_to_disting(domain_name)
	log.Debug('disting = %s' % str(disting))
	
	# if account_exist(loging, disting):	
		# newObject = find(loging, disting)
	# else:
	obj = getADObject(disting)
	objClass = "user"
	fullname = loging
	objRelativeName = "CN=%s" % loging
	newObject = obj.Create(objClass, objRelativeName)

	newObject.Put("sAMAccountName", user['login'])
	newObject.Put('userPrincipalName',user['login']+'@' + domain_name)
	newObject.Put('givenName',user['first'])
	newObject.Put('sn',user['last'])
	newObject.Put('DisplayName', display_name) 
	newObject.SetInfo()
	newObject.GetInfo()
	newObject.AccountDisabled=0
	newObject.setpassword(user['password'])
	newObject.SetInfo()
	return True

def create_contact(login):
	import principalUtils as utils
	domain, name = utils.split(login)
	disting = domain_name_to_disting(domain)
	if account_exist(name, disting):
		newObject = find(name, disting)
	else:
		obj = getADObject(disting)
		newObject = obj.Create("contact", "cn=%s" % name)
		newObject.SetInfo()
	
	return True

def create_user_ex(loging, domain_name, psw=DEFAULT_PASSWORD, display_name=None):
	if not display_name: display_name = loging
	user = wrap_user(loging, psw)
	
	disting = domain_name_to_disting(domain_name)
	
	if account_exist(display_name, disting):
		newObject = find(display_name, disting)
	else:
		obj = getADObject(disting)
		objClass = "user"
		fullname = loging
		objRelativeName = get_escaped_account(display_name)
		newObject = obj.Create(objClass, objRelativeName)

	newObject.Put("sAMAccountName", user['login'])
	newObject.Put('userPrincipalName',user['login']+'@' + domain_name)
	newObject.Put('givenName',user['first'])
	newObject.Put('sn',user['last'])
	newObject.Put('DisplayName', display_name) 
	newObject.SetInfo()
	newObject.GetInfo()
	newObject.AccountDisabled=0
	newObject.setpassword(user['password'])
	newObject.SetInfo()
	return True

def get_ADsPath_new(account, disting):
	return "LDAP://CN=%s,CN=Users,%s" % (account, disting)

def get_ADsPath(account, disting):
	log.Debug('account, disting = %s, %s' % (account, disting))
	sub_cont = "CN=Users"
	name = account
	if account.find("\\") != -1:
		(a,b) = account.split("\\")
		if a.upper() == "BUILTIN":
			sub_cont = "CN=Builtin"
			name = b
		elif a.upper() == "NT AUTHORITY":
			sub_cont = "CN=WellKnown Security Principals,CN=Configuration"
			name = b
			
	log.Debug('get_escaped_account(name), sub_cont, disting = %s,%s,%s' % (get_escaped_account(name), sub_cont, disting))
	adsPath = get_escaped_ADsPath("%s,%s,%s" % (get_escaped_account(name), sub_cont, disting))
	log.Debug('adsPath = %s' % adsPath)
	return adsPath

def get_escaped_ADsPath(fullName):
	Pathname = com_client.Dispatch("Pathname")
	Pathname.Set(fullName, 4)
	return Pathname.Retrieve(2)

def get_escaped_account(account):
	Pathname = com_client.Dispatch("Pathname")
	esc_account = Pathname.GetEscapedElement(0, "CN=%s"%account)
	return esc_account

def find_by_ADs(ADsPath):
	print ADsPath
	return com_client.GetObject(ADsPath)
	
def find_in_domain(account, domain_name):
	disting = domain_name_to_disting(domain_name)
	return find_by_ADs(get_ADsPath(account, disting))
	
def find(account, disting):
	return find_by_ADs(get_ADsPath(account, disting))
	
def account_exist(account, disting):	
	try:
		obj = find(account, disting)
	except com_client.pywintypes.com_error, e:
		if e.args[0] == -2147016656:
			return False
		raise e
		
	return True

def GetDomainDN(server):
	dn = ''
	domain = win32security.DsGetDcName(computerName = server)['DomainName']
	for s in domain.split('.'): dn += "DC=%s," % s
	return dn[:-1]

def GetDomain(server):
	return win32security.DsGetDcName(computerName = server)['DomainName'].split('.')[0]

def GetDomainFull(server):
	return win32security.DsGetDcName(computerName = server)['DomainName']

def DeleteUser(server, name):
	win32net.NetUserDel(server, name)

def CreateUser(server, name):
	data = {'name':name, 'password':DEFAULT_PASSWORD, 'password_age':0, 'priv':1,
		'home_dir':u'', 'comment':u'', 'flags':0x0200, 'script_path':u''}
	win32net.NetUserAdd(server, 1, data)
	u = com_client.GetObject(
		"LDAP://CN=%s,CN=Users,%s" % (name, GetDomainDN(server)))
	u.Put('userPrincipalName', name +'@' + GetDomainFull(server))
	u.SetInfo()

def IsItemExist(server, name):
	try:
		com_client.GetObject(
			"LDAP://CN=%s,CN=Users,%s" % (name, GetDomainDN(server)))
		return True
	except:
		return False

def DeleteGroup(server, name):
	cont = com_client.GetObject("LDAP://CN=Users,%s" % GetDomainDN(server))
	cont.Delete("group", "CN=%s" % name)

def CreateGroup(server, name):
	cont = com_client.GetObject("LDAP://CN=Users,%s" % GetDomainDN(server))
	g = cont.Create("group", "cn=%s" % name)
	g.Put("sAMAccountName", name)
	g.Put("groupType", group_types['local'])
	g.SetInfo()

def AddUserToGroup(server_u, user, server_g, group):
	g = com_client.GetObject(
		"LDAP://CN=%s,CN=Users,%s" % (group, GetDomainDN(server_g)))
	u = com_client.GetObject(
		"LDAP://CN=%s,CN=Users,%s" % (user, GetDomainDN(server_u)))
	u_sid = win32security.SID(u.objectSid)
	try:
		g.Add("LDAP://%s/<SID=%s>" % (server_u, str(u_sid)[6:]))
		g.SetInfo()
	except:
		pass
		
#Add Access Control Entry to domain. (by A.Wu)
def SetRight(domain, accesstype, trustee):
	domainfull = 'LDAP://' + domain_name_to_disting(domain)
	sec = find_by_ADs(domainfull)
	sd = sec.Get('nTSecurityDescriptor')
	dacl = sd.DiscretionaryAcl
	newace = com_client.Dispatch("AccessControlEntry")
	newace.AccessMask = 0xf01ff
	newace.AceType = accesstype
	newace.AceFlags = 0x2
	newace.trustee = trustee
	dacl.AddAce(newace)
	sd.DiscretionaryAcl = dacl
	sec.Put('nTSecurityDescriptor', sd)
	sec.SetInfo()
	
#Remove Access Control Entry from domain. (by A.Wu)
def RemoveRight(domain, trustee):
	import string
	domainfull = 'LDAP://' + domain_name_to_disting(domain)
	sec = find_by_ADs(domainfull)
	sd = sec.Get('nTSecurityDescriptor')
	dacl = sd.DiscretionaryAcl
	for ace in dacl:
		if string.lower(trustee) == string.lower(ace.Trustee):
			dacl.RemoveAce(ace)
			break
	sd.DiscretionaryAcl = dacl
	sec.Put('nTSecurityDescriptor', sd)
	sec.SetInfo()
	

def getObject(dn, autoFindRootDSE):
	if not autoFindRootDSE:
		return com_client.GetObject(dn)
	ldap_loc = com_client.GetObject('LDAP://rootDSE').Get("defaultNamingContext")
	ldap_obj_loc=dn+ldap_loc
	print 	ldap_obj_loc
	return com_client.GetObject("LDAP://" + ldap_obj_loc)
	
rightsDict = {'read':0x20014}	

def grantRightsForAdObject(principal, dn, right, autoFindRootDSE = False):
	setRightOfTypeForPrincipalToADObject(principal, dn, rightsDict[right], 0, autoFindRootDSE)
	
def denyRightsFromAdObject(principal, dn, right, autoFindRootDSE = False):
	setRightOfTypeForPrincipalToADObject(principal, dn, rightsDict[right], 1, autoFindRootDSE)

def setRightOfTypeForPrincipalToADObject(principal, dn, right, typeOfright, autoFindRootDSE):
	o = getObject(dn, autoFindRootDSE)

	sd = getattr(o,'nTSecurityDescriptor')
	dacl = sd.DiscretionaryAcl

	newace = com_client.Dispatch("AccessControlEntry")
	newace.AccessMask = right
	newace.AceType = typeOfright
	newace.AceFlags = 0
	newace.trustee = principal
	dacl.AddAce(newace)
	sd.DiscretionaryAcl = dacl
	o.Put('nTSecurityDescriptor', sd)
	o.SetInfo()			
	
def removeRightsForPrincipalFromAdObject(principal, dn, autoFindRootDSE = False):
	o = getObject(dn, autoFindRootDSE)
	sd = getattr(o,'nTSecurityDescriptor')
	dacl = sd.DiscretionaryAcl
	for ace in dacl:
		if ace.Trustee.lower() == principal.lower():
			dacl.RemoveAce(ace)
			print "removed"
	sd.DiscretionaryAcl = dacl
	o.Put('nTSecurityDescriptor', sd)
	o.SetInfo()

def listPerms(dn, autoFindRootDSE = False):
	o = getObject(dn, autoFindRootDSE)
	sd = getattr(o,'nTSecurityDescriptor')
	dacl = sd.DiscretionaryAcl
	for ace in dacl:
		print ace.trustee
