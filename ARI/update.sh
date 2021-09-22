echo "Checking for updates..."

content=$(wget https://raw.githubusercontent.com/Marakusa/ari/main/ARI/version -q -O -)
echo $content
echo diff /usr/lib/ari/version $content
if [ ! diff /usr/lib/ari/version $content ]
then
	echo "A new update available! Downloading..."
	git clone https://github.com/Marakusa/ari.git /tmp/ari/ari
	sudo chmod a+x /tmp/ari/ari/install.sh
	bash /tmp/ari/ari/install.sh
	sudo rm -rf /tmp/ari/ari
fi
