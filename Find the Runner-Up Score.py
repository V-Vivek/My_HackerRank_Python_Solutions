# Question : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
  if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split())) # Used set() to get unique items
    arr = list(arr)
    arr.sort()
    print(arr[-2])
