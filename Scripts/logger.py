#Copyright (C) 2009 Quest Software, Inc.
#File:		logger.py
#Version:	1.0.0.10

############################################################
#
#	THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
#	EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED 
#	WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. 
#
############################################################

import logging
import logging.handlers

def CreateIfNeedLogFolder(fileName):
	import os.path
	
	folderName = os.path.dirname(fileName)
	if len(folderName) > 0 and not os.path.exists(folderName):
		import os
		os.mkdir(folderName)

class Log:
	log = logging.getLogger()
	
	def Init(self, filename):
		CreateIfNeedLogFolder(filename)
		self.log.setLevel(logging.DEBUG)
		formatter = logging.Formatter("%(asctime)s [%(process)d:%(thread)d] ** %(levelname)s ** %(message)s")
		handler = logging.handlers.RotatingFileHandler(filename, maxBytes=5242880, backupCount=500)
		handler.setFormatter(formatter)
		self.log.addHandler(handler)

	def Info(self, mess):
		self.log.info(mess)
	
	def Debug(self, mess):
		self.log.debug(mess)
	
	def Except(self, mess):
		import sys
		self.log.exception(mess)

	def logCall_decoratorBody(self, func,*arg, **args):
		strToLog = "%s called with %s and %s," % (func.__name__, str(arg), str(args) )
		logging.info(strToLog)
		try:
			res=func(*arg, **args)
			logging.info('result of %s: %s' % (func.__name__, str(res)))
			return res
		except:
			self.Except('Exeption in call function %s,' % (func.__name__))
			raise

	def logCall(self, func):
		def call(*arg, **args):
			return self.logCall_decoratorBody(func,*arg, **args)
		return call		
		
log = Log()