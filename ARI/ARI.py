#! /usr/bin/ari
#------------------------------------------------------------------------
#    Copyright (C) 2021 Markus Kannisto <m.kannisto01@gmail.com>
#------------------------------------------------------------------------

import sys
from .install import *

if len(sys.argv) == 1:
	print('Invalid usage. Please use arguments help or -h for more information.')
else:
	if sys.argv[2] == "install" or sys.argv[2] == "-i" or sys.argv[2] == "i":
		if len(sys.argv) > 3 and sys.argv[3] != "":
			search(sys.argv[3])
		else:
			print("Invalid amount of arguments. Please use arguments help or -h for more information.")
