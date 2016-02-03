#! /bin/sh
while read -n 1 c
    do echo $c
done | awk "/\(/ { ++floor } /\)/ { if (--floor == -1) { print NR; exit } }"
