from sp_objects import *

server = 'atperf'
webapp = 'http://atperf'

for num in range( 50 ):
	sc = '/sites/toplevelsite%i' %  num 
	add_tls_in_special_db( webapp ,'WSS_ContentDB_perftest%i' % num,server, sc)
	for i in range( 20 ):	
		path = 'sub_site_withuniqperm%i'% i 
		add_site_in_tls( webapp + sc, path , title = 'title%i'%i, descr = 'descr', web_template = 'STS#2')	
		site_url = webapp + sc + '/' + path
		log.Debug('added site ')
		site = SPSite( site_url ).OpenWeb()
		if not site.HasUniqueRoleDefinitions:
			site.RoleDefinitions.BreakInheritance(True, True)
			site.Update()     

