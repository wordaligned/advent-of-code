#! /usr/bin/env python
''' http://adventofcode.com/day/6 '''

import sys
import re
from itertools import product

match = re.compile(r'(turn (on|off)|toggle) (\d+),(\d+) through (\d+),(\d+)').match

lights = {xy: 0 for xy in product(range(1000), repeat=2)}

def on(xy):     lights[xy] = 1
def off(xy):    lights[xy] = 0
def toggle(xy): lights[xy] = not lights[xy]

for instruction in sys.stdin:
    m = match(instruction)
    switch = {'turn on' : on,
              'turn off': off,
              'toggle'  : toggle}[m.group(1)]
    xlo,ylo, xhi,yhi = list(map(int, m.groups()[2:]))
    for xy in product(range(xlo, xhi+1), range(ylo, yhi+1)):
        switch(xy)

print(sum(lights.values()))

