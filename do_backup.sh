#!/bin/bash
#
# Backup script
#
BACKUP_SERVER=pdsilva@192.168.1.200:

/usr/bin/rsync -avz --delete-excluded --exclude-from /home/pdsilva/tmp/Toexclude /home/pdsilva/tmp $BACKUP_SERVER

