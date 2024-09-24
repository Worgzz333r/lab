ch1 = int(input())
zn1 = int(input())
ch2 = int(input())
zn2 = int(input())
zn11 = zn1
zn22 = zn2
ch11 = ch1
ch22 = ch2
Dio = input("- or + ")
if Dio == "+": 
    if zn1 == zn2:
        ch = ch1 + ch2
        print(ch)
        print(zn1)
        chs = ch // zn1
        print(chs)
    else:
        def nsd(zn1, zn2): 
            while zn1 * zn2 != 0:
                if zn1 >= zn2:
                    zn1 = zn1 % zn2
                else:
                    zn2 = zn2 % zn1
            return zn1 + zn2
        zn = zn1 * zn2 // nsd(zn1, zn2) 
        print (zn)
        ch111 = zn // zn1
        ch222 = zn // zn2
        ch1111 = ch111 * ch11
        ch2222 = ch222 * ch22
        print(ch1111)
        print(ch2222)
        ch = ch1111 + ch2222
        if ch >= zn:
            chs = ch // zn
            print(chs)
        else:
            print(ch)
            print(zn)
else:
    if zn1 == zn2:
        ch = ch1 - ch2
        print(ch)
        print(zn1)
        chs = ch // zn1
        print(chs)
    else:
        def nsd(zn1, zn2): 
            while zn1 * zn2 != 0:
                if zn1 >= zn2:
                    zn1 = zn1 % zn2
                else:
                    zn2 = zn2 % zn1
            return zn1 + zn2
        zn = zn1 * zn2 // nsd(zn1, zn2) 
        print (zn)
        ch111 = zn // zn1
        ch222 = zn // zn2
        ch1111 = ch111 * ch11
        ch2222 = ch222 * ch22
        print(ch1111)
        print(ch2222)
        ch = ch1111 - ch2222
        if ch >= zn:
            chs = ch // zn
            print(chs)
        else:
            print(ch)
            print(zn)