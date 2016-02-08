#! /usr/bin/env bash
grep -Ev "ab|cd|pq|xy" - | \       # Lines which do not match these patterns ...
grep -E "(.)\1" | \                # and do have a repeated character ...
while read line
do
    vowels=$(tr -Cd "aeiou" <<< $line)
    if [ ${#vowels} -ge 3 ]        # and have 3 or more vowels ...         
        then echo $line            # are echoed
    fi
done
