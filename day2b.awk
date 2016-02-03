function min3(a, b, c) {
    return a < b ? 
          (a < c ? a : c) : 
          (b < c ? b : c) 
}

BEGIN { FS = "x" }
      {   top = 2 * ($1 + $2)
          rhs = 2 * ($2 + $3)
          lhs = 2 * ($3 + $1)
          vol = $1 * $2 * $3
          ribbon += vol + min3(top, rhs, lhs)
      }
END   {   print ribbon }
