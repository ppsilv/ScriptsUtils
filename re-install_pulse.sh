#!/bin/bash
# clean and reinstall pulseaudio
sudo apt-get remove --purge alsa-base pulseaudio
sudo apt-get install alsa-base pulseaudio
sudo apt-get -f install && sudo apt-get -y autoremove && sudo apt-get autoclean && sudo apt-get clean && sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
# fixes user folder permissions
sudo chown -R $USER:$USER $HOME/
# then reboot
sudo reboot
