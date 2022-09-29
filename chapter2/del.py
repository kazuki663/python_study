from unicodedata import name


name = 'Python'
print(name)  #結果：Python

# 変数のnameを破棄
del name
print(name)  #結果：NameError: name 'name' is not defined