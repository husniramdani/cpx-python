n = int(input())
arr = input().split()
for i in range(n):
    print( arr.index( str(i+1) ) +1 )