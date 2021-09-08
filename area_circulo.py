#!/usr/bin/python3
# https://omegaup.com/arena/problem/Area-del-circulo/
def _main() -> None:
  import math
  r = int(input())
  a = (math.pi*r*r)
  area_redondeada = round(a,2)
  print (area_redondeada)
if __name__ == '__main__':
  _main()
