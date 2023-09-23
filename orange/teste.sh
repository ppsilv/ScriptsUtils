#!/bin/bash

for i in $(seq 0 $(( $(nproc --all) - 1)) ); 
	do (taskset -c $i yes > /dev/null &); 
done
