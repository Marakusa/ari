echo "Creating a new directory to /usr/lib/ari for ARI..."
sudo mkdir -m 777 /usr/lib/ari
sudo chmod 777 /usr/lib/ari

echo "Done! (1/5)"
echo ""
echo ""

copycount=$((8))
copied=$((1))

echo "Copying files ($copied/$copycount)..."
sudo cp -fv ARI/ARI.py /usr/lib/ari/ari.py
copied=$((copied + 1))

echo "Copying files ($copied/$copycount)..."
sudo cp -fv ARI/arihelp.py /usr/lib/ari/arihelp.py
copied=$((copied + 1))

echo "Copying files ($copied/$copycount)..."
sudo cp -fv ARI/arihelp.py /usr/lib/ari/arihelp.py
copied=$((copied + 1))

echo "Copying files ($copied/$copycount)..."
sudo cp -fv ARI/install.py /usr/lib/ari/install.py
copied=$((copied + 1))

echo "Copying files ($copied/$copycount)..."
sudo cp -fv ARI/commands.json /usr/lib/ari/commands.json
copied=$((copied + 1))

echo "Copying files ($copied/$copycount)..."
sudo cp -fv ARI/installpkg.sh /usr/lib/ari/installpkg.sh
copied=$((copied + 1))

echo "Copying files ($copied/$copycount)..."
sudo cp -fv ARI/update.sh /usr/lib/ari/update.sh
copied=$((copied + 1))

echo "Copying files ($copied/$copycount)..."
sudo cp -fv ARI/version /usr/lib/ari/version

echo "Done! (2/5)"
echo ""
echo ""


echo "Creating the binaries..."
echo "==> '/bin/ari'"
sudo cp -fv ARI/ari /bin/ari

echo "Done! (3/5)"
echo ""
echo ""


echo "Adding permissions..."
sudo chmod a+x /usr/lib/ari/ari.py
sudo chmod a+x /usr/lib/ari/arihelp.py
sudo chmod a+x /usr/lib/ari/install.py
sudo chmod a+x /usr/lib/ari/installpkg.sh
sudo chmod a+x /usr/lib/ari/update.sh

sudo chmod a+r /usr/lib/ari/commands.json
sudo chmod a+r /usr/lib/ari/version

sudo chmod a+x /bin/ari
sudo chmod a+x ARI/requirements.sh

echo "Done! (4/5)"
echo ""
echo ""


echo "Installing the requirements..."
./ARI/requirements.sh

echo "Done! (5/5)"
echo "ARI installed!"