sample = '''
    'db%s': {
        'NAME': os.path.dirname( __file__ ) + '/database/model%s.db',
        'ENGINE': 'sqlite3',
        'USER': '',
        'PASSWORD': '',
		'HOST':'',
		'PORT':'',
		'OPTIONS':{'timeout': 30}		
    },
'''
res = ''

# for i in range(21,51):
	# res += sample % (i,i,i,i,i) + '\n'

for i in range(9,50):
	res += sample % (i,i) + '\n'
	
	
f = open('res1.txt', 'w')
f.write( res )
f.close()
	