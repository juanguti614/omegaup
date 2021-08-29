#!/usr/bin/python3

def _main() -> None:
  a,b = input().split()
  a = int(a)
  b = int(b)
  while a <= b:
      print(a)
      a = a + 1

if __name__ == '__main__':
  _main()