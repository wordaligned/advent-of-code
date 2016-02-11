// http://adventofcode.com/day/8
package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func fatal(e string) {
	fmt.Fprintln(os.Stderr, "Error:", e)
	os.Exit(1)
}

func check(cond bool, e string) {
	if !cond {
		fatal(e)
	}
}

func ishex(c byte) bool {
	return '0' <= c && c <= '9' ||
		'a' <= c && c <= 'f' ||
		'A' <= c && c <= 'F'
}

func main() {
	data, err := ioutil.ReadAll(os.Stdin)
	check(err == nil, "failed to read stdin")

	surplus := 0
	for i := 0; i < len(data); i++ {
		switch data[i] {
		case byte('\\'):
			i++
			check(i < len(data), "invalid escape sequence")
			switch data[i] {
			case byte('"'), byte('\\'):
				surplus++
			case byte('x'):
				i += 2
				check(i < len(data) && ishex(data[i-1]) && ishex(data[i]),
					"invalid hex escape sequence")
				surplus += 3
			default:
				fatal("invalid escape sequence")
			}
		case byte('"'):
			surplus++
		}
	}
	print(surplus)
}
