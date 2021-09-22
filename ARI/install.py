import requests
import subprocess

searchFormat = "https://aur.archlinux.org/packages/?O=0&SeB=n&K={0}"
gitFormat = "https://aur.archlinux.org/{0}.git"
packageFormat = "https://aur.archlinux.org/packages/{0}";

def install(args):
	pkgname = args[2]

	print(f"Starting to install {pkgname}...")

	giturl = gitFormat.format(pkgname)
	packageurl = packageFormat.format(pkgname)
	response = requests.get(packageurl)

	if response.status_code == 200:
		print("rm -rf /tmp/ari/" + pkgname + "/")
		subprocess.run(["rm", "-rf", "/tmp/ari/" + pkgname + "/"])

		print("git clone " + giturl + " /tmp/ari/" + pkgname)
		subprocess.run(["git", "clone", giturl, "/tmp/ari/" + pkgname])

		print("bash /usr/lib/ari/installpkg.sh /tmp/ari/" + pkgname + "/")
		subprocess.run(["bash", "/usr/lib/ari/installpkg.sh", "/tmp/ari/" + pkgname + "/"])
	else:
		print(f"An error occurred (HTTP Status Code: {response.status_code} - {url})")
