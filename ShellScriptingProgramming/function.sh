#! /bin/bash


Myfunadd(){
    a=$1
    b=$2
    c=$((a + b))
    echo "sum $c"
    
}
echo "calling add"
Myfunadd 2 3 