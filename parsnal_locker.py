import os

def hidedir():
    os.system('PowerShell "attrib +h +s +r Parsnal"')

hidedir()

def showdir():
    os.system('PowerShell "attrib -h -s -r Parsnal"')


if not os.path.exists("Parsnal"):
    pwd = input("Enter password --> ")
    cmpwd =  input("Enter conform password --> ")
    if pwd==cmpwd:
        p = open('ps.txt','a')
        p.write(pwd)
        p.close()
        os.system('PowerShell "attrib +h +s +r ps.txt"')
        print('password set sucessful...')
    else:
        print("Password do not match......")
    os.mkdir("Parsnal")


print("\nWelcome to dhiraj locker system\n")
print('''1. Show parsnal folder
2. Hide parsnal folder
3. View parsnal file
4. Exit''')

user = int(input("Enter value--> "))

if user==1:
    with open("ps.txt") as f:
        pwd = f.read()
    unlock = input('Enter password --> ')
    if unlock==pwd:
        showdir()
        print("Parsnal folder now live.")
    
    else:
        print("invaild password !!!!!")

    
elif user==2:
    hidedir()
    print('Folder hide succesful.....')


elif user==3:
    os.chdir("D:\\python project\\Parsnal")
    print("Folder items............\n")
    os.startfile("D:\\python project\\Parsnal")
    
else:
    exit()
