#!/bin/bash

echo "fs.inotify.max_user_watches=204800" | sudo tee -a /etc/sysctl.conf
echo 204800 | sudo tee /proc/sys/fs/inotify/max_user_watches

