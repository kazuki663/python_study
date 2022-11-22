d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}

#項目の列挙
for item in d.items():
  print(item)

for key, value in d.items():
  print(key, ':', value)

#キーを列挙
for key in d.keys():
  print(key)

#値を列挙
for value in d.values():
  print(value)
