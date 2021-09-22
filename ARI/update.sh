currentver=`cat /usr/lib/ari/version`

echo "Current version: $currentver"
echo "Checking for updates..."

newver=$(wget https://raw.githubusercontent.com/Marakusa/ari/main/ARI/version -q -O -)

echo "Latest version: $newver"

if [ currentver != newver ]
then
	echo "A new update available ($newver)! Downloading..."
	git clone https://github.com/Marakusa/ari.git /tmp/ari/ari
	cd /tmp/ari/ari
	sudo chmod a+x install.sh
	bash ./install.sh
	sudo rm -rf /tmp/ari/ari
else
	echo "You have the latest version ($currentver) installed!"
fi
