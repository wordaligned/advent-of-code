// This program calculates the number of digits in the Nth looksay
// number following the supplied start number.  Slices of ints are
// used internally to represent the looksay numbers.
package main

import (
	"flag"
	"fmt"
)

var start = flag.String("start", "3113322113", "starting from this value")
var count = flag.Int("count", 40, "count this many looksay numbers")

func to_looksay(s string) (looksay []int) {
	for _, c := range s {
		looksay = append(looksay, int(c-'0'))
	}
	return looksay
}

func next_looksay(n []int) (r []int) {
	prev_d := n[0]
	prev_i := 0
	for i, d := range n {
		if prev_d != d {
			r = append(r, i-prev_i, prev_d)
			prev_i = i
			prev_d = d
		}
	}
	return append(r, len(n)-prev_i, prev_d)
}

func main() {
	flag.Parse()
	n := to_looksay(*start)
	for i := 0; i < *count; i++ {
		n = next_looksay(n)
	}
	fmt.Printf("Starting from %v, length of looksay(%v) = %v\n",
		*start, *count, len(n))
}
