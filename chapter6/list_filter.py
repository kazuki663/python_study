from unittest import result


data = [
  'フレンチブルドッグ',
  'ヨークシャテリア',
  'ダックスフンド',
  'ポメラニアン',
  'コーギー',
]

result = filter(lambda v: len(v) < 8, data)
print(list(result))