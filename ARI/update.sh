currentver=`cat /usr/lib/ari/version`

echo "Current version: $currentver"
echo "Checking for updates..."

newver=$(wget https://raw.githubusercontent.com/Marakusa/ari/main/ARI/version -q -O -)
if [ currentver != newver ]
then
	echo "A new update available ($newver)! Downloading..."
	git clone https://github.com/Marakusa/ari.git /tmp/ari/ari
	sudo chmod a+x /tmp/ari/ari/install.sh
	bash /tmp/ari/ari/install.sh
	sudo rm -rf /tmp/ari/ari
fi
