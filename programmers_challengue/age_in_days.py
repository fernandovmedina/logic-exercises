n: int = int(input())

years:  int = 0
months: int = 0
days:   int = 0

# 400
years = int(n / 365)
months = int((n % 365) / 30)
days = (n % 365) % 30

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
