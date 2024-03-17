#! bin/bash

a=$1 
b=$2

if [ $a -gt 10 ]; then     
    echo "input number $a has been greater than 10"
else
   echo "input number $a has been less than 10"
fi   
if [ $b -lt 10 ]; then 
    echo "input number $b has been less than 10"
else 
    echo " please check the input number"
fi   

