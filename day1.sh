#! /bin/sh
up=$(tr -dc '(' < input | wc -c)
dn=$(tr -dc ')' < input | wc -c)
echo $(($up - $dn))
