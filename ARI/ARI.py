#! /usr/bin/ari
#------------------------------------------------------------------------
#    Copyright (C) 2021 Markus Kannisto <m.kannisto01@gmail.com>
#------------------------------------------------------------------------

import sys
import json
import io
from arihelp import *
from install import *
from ariupdate import *

def version(args):
	print("ARI v" + open("/usr/lib/ari/version", "r").read())

commands = json.loads(open("/usr/lib/ari/commands.json", "r").read())
functions = [install, listcommands, checkupdates, version]

if len(sys.argv) <= 1:
	print(f"No command given. Please use h or help for the list of all commands")
else:
	done = 0
	i = 0

	while i < len(commands):
		if sys.argv[1] == commands[i]["short"] or sys.argv[1] == commands[i]["full"]:
			if len(sys.argv) >= len(commands[i]["args"]):
				functions[commands[i]["func"]](sys.argv)
				done = 1
			else:
				print("Invalid amount of arguments. Please use arguments help or -h for more information.")

		i += 1

	if done == 0:
		print(f"Unknown command {sys.argv[1]}. Please use h or help for the list of all commands")
