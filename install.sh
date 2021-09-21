sudo mkdir -m 777 /usr/lib/ari
sudo cp -fv ARI/ARI.py /usr/lib/ari/ari.py
sudo cp -fv ARI/install.py /usr/lib/ari/install.py
sudo ln /usr/lib/ari/ari.py /bin/ari
./requirements.sh