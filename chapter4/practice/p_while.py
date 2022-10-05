from cgi import print_directory


sum = 0
i = 0

while i <= 100:
  i += 1
  if i % 2 != 0:
    continue
  sum += i

print(sum)