#! /bin/bash
clang++ -Wall -std=c++14 day3b.cpp -o day3b

[ $(echo -n "^v"         | ./day3b) -eq 3  ] || echo "Failed test 1"
[ $(echo -n "^>v<"       | ./day3b) -eq 3  ] || echo "Failed test 2"
[ $(echo -n "^v^v^v^v^v" | ./day3b) -eq 11 ] || echo "Failed test 3"

./day3b
