#!/bin/bash

sudo mount -t cifs -o rw,username=myuser,domain=ad009,uid=1000,file_mode=0777,dir_mode=0777,gid=1000 //192.168.1.67/Users/pdsilva/Documents /mnt/latitude/documentos -o username=pdsilva
