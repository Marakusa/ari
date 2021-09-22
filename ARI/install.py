import requests
import subprocess

searchFormat = "https://aur.archlinux.org/packages/?O=0&SeB=n&K={0}"
gitFormat = "https://aur.archlinux.org/{0}.git"
packageFormat = "https://aur.archlinux.org/packages/{0}";

def install(args):
	gitpkg = args[2]

	print(f"Starting to install {gitpkg}...")

	giturl = gitFormat.format(gitpkg)
	packageurl = packageFormat.format(gitpkg)
	response = requests.get(packageurl)

	if response.status_code == 200:
		print("rm -rf /tmp/ari/" + gitpkg + "/")
		subprocess.run(["rm", "-rf", "/tmp/ari/" + gitpkg + "/"])

		print("git clone " + giturl + " /tmp/ari/" + gitpkg)
		subprocess.run(["git", "clone", giturl, "/tmp/ari/" + gitpkg])

		print("bash /usr/lib/ari/installpkg.sh /tmp/ari/" + query + "/")
		subprocess.run(["bash", "/usr/lib/ari/installpkg.sh", "/tmp/ari/" + gitpkg + "/"])
	else:
		print(f"An error occurred (HTTP Status Code: {response.status_code} - {url})")
