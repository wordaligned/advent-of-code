# http://adventofcode.com/day/6
function turn_up(d, xlo, ylo, xhi, yhi) {
    for (x = xlo; x <= xhi; ++x)
        for (y = ylo; y <= yhi; ++y)
            if ((lights[x,y] += d) < 0) lights[x,y] = 0
}

BEGIN       { FS = "[ ,]" }
/^turn on/  { turn_up( 1, $3, $4, $6, $7) }
/^turn off/ { turn_up(-1, $3, $4, $6, $7) }
/^toggle/   { turn_up( 2, $2, $3, $5, $6) }
END         { for (xy in lights)
                  brightness += lights[xy]
              print brightness }
