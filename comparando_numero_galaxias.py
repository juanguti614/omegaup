#!/usr/bin/python3
# https://omegaup.com/arena/problem/Comparando-numero-de-galaxias

def resultado(res):
    if res:
        return "True"
    return "False"

def _main() -> None:
  a,b,c = input().split()
  a = int(a)
  b = int(b)
  c = int(c)
  print(resultado(a < b), end=" ")
  print(resultado(c > a), end=" ")
  print(resultado(a == b), end=" ")
  print(resultado(a != c), end=" ")
  print(resultado(c <= b), end=" ")

if __name__ == '__main__':
  _main()
