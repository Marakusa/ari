import requests
import subprocess

searchFormat = "https://aur.archlinux.org/packages/?O=0&SeB=n&K={0}"
gitFormat = "https://aur.archlinux.org/{0}.git"
packageFormat = "https://aur.archlinux.org/packages/{0}";

def install(query):
	print(f"Starting to install {query}...")
	giturl = gitFormat.format(query);
	packageurl = packageFormat.format(query);
	response = requests.get(packageurl)
	if response.status_code == 200:
		print("git clone " + giturl)
		subprocess.run(["git", "clone", giturl, "/tmp/ari"])

		print(["cd /tmp/ari/" + query + "/"])
		subprocess.run(["cd", "/tmp/ari/" + query + "/"])

		print(["makepkg -si"])
		subprocess.run(["makepkg", "-si"])

		print(["cd .."])
		subprocess.run(["cd", ".."])

		print(["rm -rf " + query + "/"])
		subprocess.run(["rm", "-rf", query + "/"])
	else:
		print(f"An error occurred (HTTP Status Code: {response.status_code} - {url})")
