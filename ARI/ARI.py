#! /usr/bin/ari
#------------------------------------------------------------------------
#    Copyright (C) 2021 Markus Kannisto <m.kannisto01@gmail.com>
#------------------------------------------------------------------------

import sys
import requests
import subprocess

searchFormat = "https://aur.archlinux.org/packages/?O=0&SeB=n&K={0}"
gitFormat = "https://aur.archlinux.org/{0}.git"
packageFormat = "https://aur.archlinux.org/packages/{0}";

if len(sys.argv) == 1:
	print('Invalid usage. Please use arguments help or -h for more information.')
else:
	if sys.argv[2] == "install" or sys.argv[2] == "-i" or sys.argv[2] == "i":
		if len(sys.argv) > 3 and sys.argv[3] != "":
			search(sys.argv[3])
		else:
			print("Invalid amount of arguments. Please use arguments help or -h for more information.")

def search(query):
	print(f"Starting to install {query}...")
	giturl = gitFormat.format(query);
	packageurl = packageFormat.format(query);
	response = requests.get(packageurl)
	if response.status_code == 200:
		print("git clone " + giturl)
		subprocess.run(["git", "clone", giturl, "/tmp/ari"])

		print(["cd " + query + "/"])
		subprocess.run(["cd", query + "/"])

		print(["makepkg -si"])
		subprocess.run(["makepkg", "-si"])

		print(["cd .."])
		subprocess.run(["cd", ".."])

		print(["rm -rf " + query + "/"])
		subprocess.run(["rm", "-rf", query + "/"])
	else:
		print(f"An error occurred (HTTP Status Code: {response.status_code} - {url})")
