#!/usr/bin/python3
# https://omegaup.com/arena/problem/Filtrando-multiplos/
def _main() -> None:
  n = int(input())
  nums = list(map(int, input().split()))
  k = int(input())
  for i in range(n):
      if nums[i] % k == 0:
          print(nums[i], end = " ")
      else:
          print("X", end = " ")


if __name__ == '__main__':
  _main()
