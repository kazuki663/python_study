from pickle import FALSE
from unittest import result


flag = False #breakされたか

for i in range(1, 10):
  for j in range(1, 10):
    result = i * j
    if result > 50:
      #break時にflagもTrueに
      flag = True
      break
    print(result, end = ' ')
  print()
  #flagがTrueであれば外側のループも脱出
  if flag:
    break