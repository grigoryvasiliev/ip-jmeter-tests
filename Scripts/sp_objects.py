#Copyright (C) 2010 Quest Software, Inc.
#File:		sp_objects.py
#Version:	1.0.0.11

############################################################
#
#	THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
#	EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED 
#	WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. 
#
############################################################

admin_name = "atchild\\administrator"
admin_email = "administrator@atchild.atlanta.local"
sec_admin_name = "atchild\\administrator"
sec_admin_email = "administrator@atchild.atlanta.local"
web_app_counters_port = 8888

from sp_references import *

@log.logCall
def add_tls( web_url, relative_url = '', title = 'title', descr = 'descr', web_template = 'STS#0', primAdmin = admin_name, secAdmin = sec_admin_name, hh = False):
	web_app = SPWebApplication.Lookup( Uri( web_url ) )
	site = web_app.Sites.Add(relative_url, title, descr, 1033, web_template, primAdmin, primAdmin, admin_email, secAdmin, secAdmin, sec_admin_email, hh)
	web_app.Update()

@log.logCall
def add_site_in_tls( tls_url, relative_url, title = 'title', descr = 'descr', web_template = 'STS#0'):
	site = SPSite( tls_url )
	web = site.OpenWeb().Webs.Add(relative_url, title, descr, 1033, web_template, False, False)
	return web

@log.logCall
def add_site( web, relative_url, title = 'title', descr = 'descr', web_template = 'STS#0'):	
	return web.Webs.Add(relative_url, title, descr, 1033, web_template, False, False)
	
@log.logCall
def get_site(tls_url, relative_url = ''):
	site = SPSite( tls_url )
	web = site.OpenWeb(relative_url)
	return web

def IsSiteExist(webs, name):
	for web in webs:
		if web.Title == name:
			return True
			
	return False
	
@log.logCall
def delete_web(parentUrl, webName):
	site = SPSite( parentUrl )
	parentWeb = site.OpenWeb()
	if IsSiteExist(parentWeb.Webs, webName):
		web = site.OpenWeb(webName)
		DeleteWeb(web)
	site.Dispose()	

def DeleteWeb(web):
	DeleteAllSubwebs(web)
	web.Delete()

def DeleteAllSubwebs(web):
	for subWeb in web.Webs:
		DeleteWeb(subWeb)
	
@log.logCall	
def add_list( web, title = 'title', descr = 'descr', type = SPListTemplateType.GenericList ):
	id = web.Lists.Add(title, descr, type)
	return web.Lists[id]

@log.logCall	
def add_doclib(web, title = 'title', descr = 'descr'):
	type = SPListTemplateType.DocumentLibrary
	return add_list( web, title, descr, type)
	
@log.logCall	
def add_doc(doclib, name = 'name.txt', size_b = 1):
	return doclib.RootFolder.Files.Add(name,Array.CreateInstance(Byte, size_b))

@log.logCall
def AddDocInDocLibWeb(url = '', doc_lib = 'Shared Documents', name = 'name.txt', size_b = 1):
	site = SPSite( url )
	web = site.OpenWeb()
	for a in web.Lists:
		if a.Title == doc_lib:
			return a.RootFolder.Files.Add(name,Array.CreateInstance(Byte, int(size_b) * 1024 * 1024))

@log.logCall
def CheckOutDocInWeb(url = '', name = 'name.txt'):
	site = SPSite( url )
	web = site.OpenWeb()
	docPath = name.split('/')
	folderWOSpaceEscape = docPath[1].replace('%20', ' ')
	for a in web.Lists:
		if a.Title == folderWOSpaceEscape:
			for doc in a.RootFolder.Files:
				if doc.Name == docPath[2]:
					doc.CheckOut()		

@log.logCall
def CheckInDocInWeb(url = '', name = 'name.txt', descr = 'check in'):
	site = SPSite( url )
	web = site.OpenWeb()
	docPath = name.split('/')
	folderWOSpaceEscape = docPath[1].replace('%20', ' ')
	for a in web.Lists:
		if a.Title == folderWOSpaceEscape:
			for doc in a.RootFolder.Files:
				if doc.Name == docPath[2]:
					doc.CheckIn(descr)
					
def IsDoclibExists(coll, name):
	for list in coll:
		if list.Title == name:
			return True
	return False

 
@log.logCall
def add_doc_in_list(parent_url, list_name,name, size):
	site = SPSite(parent_url )
	web = site.AllWebs['']
	if IsDoclibExists(web.Lists,list_name):
		lib = web.Lists[list_name];
	else:
		lib = add_list(web, list_name, "", SPListTemplateType.DocumentLibrary)
		
	add_doc(lib, name, size)	
	site.Dispose()
	
@log.logCall	
def add_item(list, item_title = 'item_title'):
	item = list.Items.Add()
	item["Title"] = item_title
	return item

@log.logCall	
def add_attach(item, att_name = 'name.txt', size_b = 1):
	doc = item.Attachments.Add( att_name, Array.CreateInstance(Byte, size_b))
	item.Update()
	return item

@log.logCall	
def create_items_in_list(parent, size_doc_mb, num_files, list_name, list_type):
	list = add_list(get_site(parent), list_name, "", list_type)
	list.EnableAttachments = True
	for i in range(0,num_files):
		add_attach(add_item(list), "file" + str(i) + ".txt",1024*1024*size_doc_mb)
		
@log.logCall
def create_docs_in_list(parent, size_doc_mb, num_files =1 , list_name = "Shared Documents"):
	for i in range(0,num_files):
		add_doc_in_list(parent, list_name, "file" + str(i) + ".txt", 1024*1024*size_doc_mb)	
		
@log.logCall	
def create_tls_with_documents(web_app_url, name, descr, size_doc_mb, num_files = 1, hh = False):
	add_tls(web_app_url,name, descr, hh = hh)
	if hh:
		tls_url = name
	else:
		tls_url = web_app_url + "/" + name

	create_docs_in_list(tls_url, size_doc_mb, num_files)

@log.logCall
def create_web_app( name, comment, dbname, port, owner = admin_name, email = admin_email, ssl = False, spversion = 2010 ):
	from Microsoft.SharePoint.Administration import SPWebService, SPWebApplicationBuilder, IdentityType

	from System.Security import SecureString
	
	spAdminFarm = SPWebService.AdministrationService.Farm
	spWebBuilder = SPWebApplicationBuilder(spAdminFarm)
	
	appPoolpwd = SecureString()
	appPoolpwd.AppendChar('1')
	appPoolpwd.MakeReadOnly()	
	
	spWebBuilder.Port = port
	spWebBuilder.CreateNewDatabase = True
	spWebBuilder.DatabaseName = dbname
	spWebBuilder.ServerComment = comment
	spWebBuilder.UseNTLMExclusively = True
	spWebBuilder.AllowAnonymousAccess = False
	spWebBuilder.UseSecureSocketsLayer = ssl
	
	if spversion == 2010:
		spWebBuilder.ApplicationPoolId = comment + " - AppPool"
		spWebBuilder.ApplicationPoolUsername = owner
		spWebBuilder.ApplicationPoolPassword = appPoolpwd
		spWebBuilder.IdentityType = IdentityType.SpecificUser	
	
	spWebApp = spWebBuilder.Create()
	spWebApp.Name = name
	spWebApp.Update()
	spWebApp.Provision()
	
	if spversion == 2007:
		spWebApp.ApplicationPool.CurrentIdentityType = IdentityType.SpecificUser
		spWebApp.ApplicationPool.Username = owner
		spWebApp.ApplicationPool.Password = '1'
		spWebApp.ApplicationPool.Provision()	
	
	tls = spWebApp.Sites.Add("", owner, email)
	spWebApp.Update()
	tls.Dispose()
	
@log.logCall
def setSiteQuota(tls_url, size):
	quota = SPQuota()	
	quota.StorageMaximumLevel = size
	site = SPSite( tls_url )
	site.Quota = quota
	
@log.logCall
def getSite(host,port):
	return SPSite('%s:%s'%(host,port))	

@log.logCall
def getRootWeb(host,port,url=''):
	return SPSite('%s:%s%s'%(host,port,url)).OpenWeb()	
	
@log.logCall	
def getManagedPathesOfWA(host,port):
	site = getSite(host,port)	
	return site.WebApplication.Prefixes

@log.logCall	
def addNewManagedPathes(spPathes,listnewpathes,type):
	for path in listnewpathes:
		if not spPathes.Contains(path):
			spPathes.Add(path, type)

@log.logCall	
def add_version(doc, size_b = 1, comment = 'checkin comment!'):
	doc.CheckOut()
	doc.SaveBinary(Array.CreateInstance(Byte, size_b))
	doc.CheckIn(comment)
	return doc

@log.logCall
def add_tls_in_special_db( web_url, contentdb, sql_server, relative_url = '', title = 'title', descr = 'descr', web_template = 'STS#1'):
	web_app = SPWebApplication.Lookup( Uri( web_url ) )
	site = web_app.Sites.Add(relative_url, title, descr, 1033, web_template, admin_name, admin_name, admin_email, sec_admin_name, sec_admin_name, sec_admin_email, sql_server, contentdb, None, None)
	web_app.Update()
	site.Dispose()

@log.logCall	
def ExecProcess(file, arg=''):
	from System.Diagnostics import ProcessStartInfo, Process
	processStartInfo = ProcessStartInfo(file, arg)
	processStartInfo.UseShellExecute = True
	processStartInfo.CreateNoWindow = True
	process = Process.Start(processStartInfo)	

@log.logCall
def MakeDBOffline():
	ExecProcess(r"c:\IPCE-r7\ipy\ipy.exe", "db_offliner.py")

@log.logCall
def give_user_policy_of_web_app(web_app_url, full_login):
	web_app = SPWebApplication.Lookup( Uri( web_app_url ) )
	policy = web_app.Policies.Add(full_login, "MyCustomPolicy")
	policy.PolicyRoleBindings.Add(web_app.PolicyRoles.GetSpecialRole(SPPolicyRoleType.FullControl))
	web_app.Update()

@log.logCall	
def givePermissionWithDomain( domain, site_url, login_name, user_title, permission_level ):
	assignment = SPRoleAssignment( domain + "\\" + login_name, login_name + '@' + domain + '.local', user_title, 'created by fit story')
	site = SPSite( site_url ).OpenWeb()
	if not site.HasUniqueRoleDefinitions:
		site.RoleDefinitions.BreakInheritance(True, True)
	assignment.RoleDefinitionBindings.Add( site.RoleDefinitions[ permission_level ] )
	site.RoleAssignments.Add( assignment )
	site.Update()	

@log.logCall	
def givePermissionSpGroup( site_url, group_name, permission_level ):
	site = SPSite( site_url ).OpenWeb()
	for gr in site.SiteGroups:
		if gr.Name == group_name:
			assignment = SPRoleAssignment(gr)
			if not site.HasUniqueRoleDefinitions:
				site.RoleDefinitions.BreakInheritance(True, True)
			assignment.RoleDefinitionBindings.Add( site.RoleDefinitions[ permission_level ] )
			site.RoleAssignments.Add( assignment )
			site.Update()	

@log.logCall
def addGroupsInSite( site_url, group_name):
	sc = SPSite( site_url )
	site = sc.OpenWeb()
	site.SiteGroups.Add(group_name, sc.Owner, sc.Owner, group_name)
	site.Update()	

@log.logCall
def addUserInSSpGroup( site_url, user_name, group_name):
	site = SPSite( site_url ).OpenWeb()
	user = site.EnsureUser(user_name)
	for gr in site.SiteGroups:
		if gr.Name == group_name:
			gr.AddUser(user)
			gr.Update()
			site.Update()
