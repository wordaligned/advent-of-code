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

[22]: http://adventofcode.com/day/22