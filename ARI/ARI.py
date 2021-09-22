#! /usr/bin/ari
#------------------------------------------------------------------------
#    Copyright (C) 2021 Markus Kannisto <m.kannisto01@gmail.com>
#------------------------------------------------------------------------

import sys
from install import *

if len(sys.argv) == 1:
	print('Invalid usage. Please use arguments help or -h for more information.')
else:
	if sys.argv[1] == "install" or sys.argv[1] == "-i" or sys.argv[1] == "i":
		print(len(sys.argv))
		print(sys.argv[2])
		if len(sys.argv) > 2 and sys.argv[2] != "":
			install(sys.argv[2])
		else:
			print("Invalid amount of arguments. Please use arguments help or -h for more information.")
	else:
		print(f"Unknown command {sys.argv[1]}")
