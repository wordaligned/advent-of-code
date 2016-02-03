# Advent of Code

Selected solutions to the set of puzzles on [Eric Wastl](http://was.tl)'s
excellent <http://adventofcode.com> site.

From [the site](http://adventofcode.com/about):

> Advent of Code is a series of small programming puzzles for a
variety of skill levels. They are self-contained and are just as
appropriate for an expert who wants to stay sharp as they are for a
beginner who is just learning to code. Each puzzle calls upon
different skills and has two parts that build on a theme.

## [Day 22][22]

This is the puzzle I finished last. I had trouble understanding the
problem description, then I failed to transcribe the specification of
the spells correctly. The spells themselves differ in ways that make
the code tricky: some have instant results, some have extended
effects, and the shield spell takes effect when cast and when it
expires. I also needed to prune the search space and game state to 
find the result.


## [Day 1][1]

All those parentheses suggest lisp for a solution, but I went for
`bash` and `awk`. The input is all on one line which doesn't work well
with awk. Here's how to work around that:

    while read -n 1 c ; do echo $c; done

## [Day 2][2]

Awk again. Much as I like `awk` I almost never use it, and attempting
this simple question reminded me why. Why isn't `min` a builtin
function, for example?

## [Day 3][3]

I wrote a C++ solution system tested using the supplied
examples. C++14 is more convenient for handling coordinate pairs
than C++98 was. I find it easier to write C++ than `bash`.

I used [lambdas for the second part](./day3b.cpp), more to
practice using them than because it was the easiest thing to do. You
can't use `auto` everwhere, it seems, but `std::function` fills the
gaps.

## [Day 4][4]

Easily and swiftly done in Python. Slowly but correctly in `bash`

    $ time ./day4.sh 
    117946
    
    real	7m29.612s
    user	2m46.140s
    sys 	5m26.347s

[1]: http://adventofcode.com/day/1
[2]: http://adventofcode.com/day/2
[3]: http://adventofcode.com/day/3
[4]: http://adventofcode.com/day/4
[5]: http://adventofcode.com/day/5
[6]: http://adventofcode.com/day/6
[7]: http://adventofcode.com/day/7
[8]: http://adventofcode.com/day/8
[9]: http://adventofcode.com/day/9
[10]: http://adventofcode.com/day/10
[11]: http://adventofcode.com/day/11
[12]: http://adventofcode.com/day/12
[13]: http://adventofcode.com/day/13
[14]: http://adventofcode.com/day/14
[15]: http://adventofcode.com/day/15
[16]: http://adventofcode.com/day/16
[17]: http://adventofcode.com/day/17
[18]: http://adventofcode.com/day/18
[19]: http://adventofcode.com/day/19
[20]: http://adventofcode.com/day/20
[21]: http://adventofcode.com/day/21
[22]: http://adventofcode.com/day/22
[23]: http://adventofcode.com/day/23
[24]: http://adventofcode.com/day/24
[25]: http://adventofcode.com/day/25

