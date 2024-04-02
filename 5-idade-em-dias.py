d = int(input())

years = d // 365
months = (d % 365) // 30
days = (d % 365) % 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')