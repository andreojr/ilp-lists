c1, c2, c3 = map(int, input().split())
v1, v2, v3 = map(int, input().split())

c1 = c1 - v1 - 2 * v1
c2 = c2 - v2 - 2 * v2
c3 = c3 - v3 - 2 * v3

print(c1+c2+c3)
