x = 50
y = x
x -= 10

data1 = [10, 20, 30]
data2 = data1
data1[1] = 15

print(x)  #40
print(y)  #50
print(data1)  #[10, 15, 30]
print(data2)  #[10, 15, 30]
