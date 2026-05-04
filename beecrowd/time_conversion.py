n: int = int(input())

hours: int = 0
minutes: int = 0
seconds: int = 0

hours = int(n / 60 / 60)
minutes = int(n / 60) % 60
seconds = n % 60
  
print(f"{hours}:{minutes}:{seconds}")