import subprocess

def checkupdates(args):
	subprocess.run(["bash", "/usr/lib/ari/update.sh"])