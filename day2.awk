function min3(a, b, c) {
    return a < b ? 
          (a < c ? a : c) : 
          (b < c ? b : c) 
}

BEGIN { FS = "x" }
      {   top = $1 * $2
          rhs = $2 * $3
          lhs = $3 * $1
          paper += 2 * (top + rhs + lhs) + min3(top, rhs, lhs)
      }
END   {   print paper }
