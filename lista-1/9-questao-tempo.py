l, d, a, k, b, v = map(int, input().split())

CURRENT_YEAR = 2023

l = abs(CURRENT_YEAR - l) * 2
d = abs(CURRENT_YEAR - d) * 2
a = abs(CURRENT_YEAR - a) * 2
k = abs(CURRENT_YEAR - k) * 2
b = abs(CURRENT_YEAR - b) * 2
v = abs(CURRENT_YEAR - v) * 2

f = l + d + a + k + b + v

print(f"Luther {l}")
print(f"Diego {d}")
print(f"Alisson {a}")
print(f"Klaus {k}")
print(f"Five {f}")
print(f"Ben {b}")
print(f"Viktor {v}")
