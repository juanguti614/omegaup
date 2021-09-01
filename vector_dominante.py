#!/usr/bin/python3
# https://omegaup.com/arena/problem/Vector-dominante

def _main() -> None:
  n = int(input())
  nums = list(map(int, input().split()))
  nums2 = list(map(int, input().split()))
  for i in range(n):
      if nums[i] > nums2[i]:
          pass
      else:
          print("0")
          return
  print("1")


if __name__ == '__main__':
  _main()
