data = [
  ['Sみかん', 'Mみかん', 'Lみかん'],
  ['S八', 'M八', 'Lはち'],
  ['Sネーブル', 'Mネーブル', 'Lネーブル'],
]

print(len(data))
print([len(clist) for clist in data])
print(sum(len(clist) for clist in data))