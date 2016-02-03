#! /bin/bash
clang++ -Wall -std=c++14 day3.cpp -o day3

[ $(echo -n "^"          | ./day3) -eq 2 ] || echo "Failed test 1"
[ $(echo -n "^>v<"       | ./day3) -eq 4 ] || echo "Failed test 2"
[ $(echo -n "^v^v^v^v^v" | ./day3) -eq 2 ] || echo "Failed test 3"

echo "The solution to day3 part one is:" $(./day3 < input3)

