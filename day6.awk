# http://adventofcode.com/day/6
function switch(action, xlo, ylo, xhi, yhi) {
    for (x = xlo; x <= xhi; ++x)
        for (y = ylo; y <= yhi; ++y)
            lights[x,y] = action == "on"  ? 1 : \
                          action == "off" ? 0 : !lights[x,y]
}

BEGIN     { FS = "[ ,]" }
/^turn/   { switch($2, $3, $4, $6, $7) }
/^toggle/ { switch($1, $2, $3, $5, $6) }
END       { for (xy in lights)
                lit += lights[xy]
            print lit }
