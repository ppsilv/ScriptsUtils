#!/bin/bash

sudo mount -t cifs -o rw,username=pdsilva,domain=ad009,uid=1000,file_mode=0777,dir_mode=0777,gid=1000 //192.168.1.52/Documentos /mnt/poseidon/documentos -o username=pdsilva
