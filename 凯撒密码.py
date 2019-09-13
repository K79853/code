def encryption():
    x=input("请输入明文:")
    m=int(input("请输入偏移值(整数):"))
    for y in x:
        if ord('A') <= ord(y) <= ord('Z'):
            t =chr(ord('A')+(ord(y)-ord('A')+m)%26)
        elif ord('a') <= ord(y) <= ord('z'):
            t =chr(ord('a')+(ord(y)-ord('a')+m)%26)
        else:
            t =y
        print(t,end="")

def decryption():
    x=input("请输入密文:")
    m=int(input("请输入偏移值(整数):"))
    for y in x:
        if ord('A') <= ord(y) <= ord('Z'):
            t =chr(ord('A')+(ord(y)-ord('A')+26-m)%26)
        elif ord('a') <= ord(y) <= ord('z'):
            t =chr(ord('a')+(ord(y)-ord('a')+26-m)%26)
        else:
            t =y
        print(t,end="")

def file_():
    file_path=input("请输入文件路径:")
    with open(file_path) as  file_a:
        lines=file_a.readlines()
    print ("1.加密")
    print ("2.解密")
    choice = input("请选择:")
    m=int(input("请输入偏移值(整数):"))
    for line in lines:
        if choice == '1':
            for y in line :
                if ord('A') <= ord(y) <= ord('Z'):
                    t =chr(ord('A')+(ord(y)-ord('A')+m)%26)
                elif ord('a') <= ord(y) <= ord('z'):
                    t =chr(ord('a')+(ord(y)-ord('a')+m)%26)
                else:
                    t =y
                print(t,end="")
                with open(file_path,'a') as file_b:
                    lines_a=file_b.write(t)
        elif choice == '2':
            for y in line :
                if ord('A') <= ord(y) <= ord('Z'):
                    t =chr(ord('A')+(ord(y)-ord('A')+26-m)%26)
                elif ord('a') <= ord(y) <= ord('z'):
                    t =chr(ord('a')+(ord(y)-ord('a')+26-m)%26)
                else:
                    t =y
                print(t,end="")
                with open(file_path,'a') as file_b:
                    lines_a=file_b.write(t)
        else:
            print ("您的输入有误！")
        

print("---*---   凯撒密码   ---*---")
print()
print("*导入的文件需在当前目录下*")
print()
print ("1.加密")
print ("2.解密")
print ("3.导入文件")
choice = input("请选择:")
if choice == '1':
    encryption()
elif choice == '2':
    decryption()
elif choice == '3':
    file_()
else:
    print ("您的输入有误！")
input("\n\nPress <enter> to exit")
