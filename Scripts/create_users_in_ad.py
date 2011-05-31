
from ad_tools import create_user

for num in range( 50,1000 ):
	login = 'ford_user%i' %  num
	domain_name = 'atchild.atlanta.local'
	psw = r'`1qwerty'
	create_user(login, domain_name, psw = psw, display_name = login)
	