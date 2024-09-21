bin = input()
j = ["000", "001", "010", "011", "100", "101", "110", "111"]
s = ""

while len(bin) % 3 != 0:
    bin = "0" + bin
    print(bin)
while len(bin) > 0:
    a = bin[-3:]
    l = str(j.index(a))
    s = l + s
    bin = bin[:-3]
print(s)
