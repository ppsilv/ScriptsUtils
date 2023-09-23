#!/bin/bash

while :
do	
echo "*********************************************"	
date
va=`cat /sys/devices/virtual/thermal/thermal_zone0/temp`
echo zone0  `expr $va / 1000`

va=`cat /sys/devices/virtual/thermal/thermal_zone1/temp`
echo zone1 `expr $va / 1000`

va=`cat /sys/devices/virtual/thermal/thermal_zone2/temp`
echo zone2 `expr $va / 1000`

va=`cat /sys/devices/virtual/thermal/thermal_zone3/temp`
echo zone3 `expr $va / 1000`

va=`cat /sys/devices/virtual/thermal/thermal_zone4/temp`
echo zone4 `expr $va / 1000`

va=`cat /sys/devices/virtual/thermal/thermal_zone5/temp`
echo zone5 `expr $va / 1000`

va=`cat /sys/devices/virtual/thermal/thermal_zone6/temp`
echo zone6 `expr $va / 1000`

sleep 30
done
