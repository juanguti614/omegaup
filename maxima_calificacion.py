#!/usr/bin/python3
# https://omegaup.com/arena/problem/Maxima-calificacion/
def _main() -> None:
    a = int(input())
    b = int(input())    
    c = int(input())    
    if a > b and a > c:
        print(a)
    if b > a and b > c:
        print(b)
    if c > b and c > a:
        print(c)

if __name__ == '__main__':
  _main()
