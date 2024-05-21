start = int(input())
end = int(input())
for i in range(start, end + 1):
  print(f"{i} дюймов = {(i*25.4)/10:.2f} cm")