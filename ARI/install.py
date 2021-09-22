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
		print("rm -rf /tmp/ari/" + query + "/")
		subprocess.run(["rm", "-rf", "/tmp/ari/" + query + "/"])

		print("git clone " + giturl + " /tmp/ari/" + query)
		subprocess.run(["git", "clone", giturl, "/tmp/ari/" + query])

		print("./installpkg.si /tmp/ari/" + query + "/")
		subprocess.run(["./installpkg.si", "/tmp/ari/" + query + "/"])
	else:
		print(f"An error occurred (HTTP Status Code: {response.status_code} - {url})")
