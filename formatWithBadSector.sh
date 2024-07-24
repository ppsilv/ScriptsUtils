#!/bin/bash
# $0 = nome do volume
# $1 = /dev/sdaX

sudo mkfs.ext4 -cc -L $0 $1
