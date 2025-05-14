
limit = 3000

num1 = 0
num2 = 1
print(num1)
print(num2)
s = num1 + num2

while s < limit:
    print(s)
    num1 = num2
    num2 = s
    s = num1 + num2
else: 
  print('s ya supero el valor de limit')