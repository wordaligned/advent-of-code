#! /usr/bin/env bash
# escape (with a \) every \ and "
escape=$(tr -d "[:alnum:]\n" < input8 | wc -c)
# and double quote every line
quote=$(wc -l < input8)
echo $((escape + 2 * quote))
