#Copyright (C) 2009 Quest Software, Inc.
#File:		sp_references.py
#Version:	1.0.0.10

############################################################
#
#	THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
#	EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED 
#	WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. 
#
############################################################

import clr
clr.AddReference('Microsoft.SharePoint')
from Microsoft.SharePoint import *
from Microsoft.SharePoint.Administration import *
from System import *
from logger import log

log.Init(r'c:\Logs\test_scripts.log')

