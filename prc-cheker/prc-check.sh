#!/bin/bash

jk(){
if [[ -n $(jobs) ]]
then 
	kill %1
	echo "done"
else 
	echo 'nothing to do'
fi 
}
