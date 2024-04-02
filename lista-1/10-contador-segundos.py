seconds = int(input())

h = seconds // (60 * 60)
m = (seconds % (60 * 60)) // 60
s = (seconds % (60 * 60)) % 60

print(f"{h}h {m}m {s}s")
