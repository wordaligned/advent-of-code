#! /bin/bash

key=ckczppom

for ((n=0;;n++))
do
    [[ $(echo -n $key$n | md5) = 00000* ]] && echo $n && break
done
