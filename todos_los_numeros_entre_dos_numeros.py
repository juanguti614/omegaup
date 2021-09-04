#!/usr/bin/python3
# https://omegaup.com/arena/problem/todosNumerosEntreEllos/

def _main() -> None:
  x1 = int(input())
  x2 = int(input())

  if x1<0 or x2<0 or x1 >= x2:
    print("Error")
    return 
  inicio = x1 + 1
  while inicio < x2:
      print(inicio, end = " ")
      inicio= inicio + 2
      

if __name__ == '__main__':
  _main()
 