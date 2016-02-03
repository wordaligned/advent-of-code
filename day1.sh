#! /bin/sh
up=$(tr -dc '(' < input1 | wc -c)
dn=$(tr -dc ')' < input1 | wc -c)
echo $(($up - $dn))
