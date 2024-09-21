a = int(input("Введіть початкове число "))
b = int(input("Введіть кінцеве число "))
s = 0
i = a - 1
n = (b - a) + 1
f = 0
for j in range(n):
    i = i + 1
    if i % 2 == 1:
        s = s + i
        f = f + 1
else:
    i = i + 1 
Sa = s/f
print (s)
print (Sa)