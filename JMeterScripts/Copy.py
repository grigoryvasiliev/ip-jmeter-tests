import shutil

for i in range(51):
	shutil.copy('model.db','model%s.db' % i)
	
	