import sys
import os
import ctypes

#This Is Adminstartor Check
def checkAdmin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def editBlock(web):
    #This Hosts File This Script Edit Hosts To Block Website
    sourceDirctory = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    #We Use Append Because Append Add String In New Line
    file = open(sourceDirctory,"a+")
    #We Add 127.0.0.1 To Block
    block = "127.0.0.1 " + web
    file.write(block + "\n")
    
def editUnblock(unblockWeb):
    #This Hosts File This Script Edit Hosts To unblock Website
    sourceDirctory = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    #We Read A Hosts File To Remove Specifed Website
    file = open(sourceDirctory,"rt")
    data = file.read()
    unBlock = "127.0.0.1 " + unblockWeb
    #We Use Replace To unblock Website
    data = data.replace(unBlock,"")
    file.close()
    file = open(sourceDirctory,"wt")
    #Use Write To Complatelly Write
    file.write(data)
    file.close()


def main():
    print("""
─────────────────────▛▀▀▀░▚▖───
───▗▖▀▀▚▖────────▄▄▖▄▖░▐▖░░░▝▀▄─
──▗▘░░░░▝▗───▄▛▀▀░░░▗▗▘░▖░░░░░▝▄
──▗░░░░░░▝▗▄▘▘░░░░░░░░▀▜▘░░░░░░▗
─▗▌░░░░░░░▝▌░░░░░░░░░░░▗░░░░░░░▐
─▞░░░░░░░░░▜░░░░░░░░░░░▝▚░░░░░▗▌  Website Blocker
▗▘░░░░░░░░░▗░░░░░░░░░░░▜▄▄▄░░▟▘─
▖░░░░░░░░░░▌▄▝░░░░░░░░▟▀─▜██▘▐▖─
▖░░░▗▄▄▖░▗▛▚█████▄░░░▐█▖─▐▛▐▌░▌─
▗░░▀▘░░░▝░▗▛──▝█▛▜▗░░░██▞▀██▘░▜─
▝▜▄░░░░░░░▐▙──▗█──▐▌░░▝▀██▀▘░░▟─
──▝▀▝▖░░░░▝███▀▝███░░▖▄▄▖░░░░▗▌─
─────▗▖░░░░▝██▄▄█▖▘░▜▄░▗▘▄░░░▛─▒
──────▜▖░░░░░▝▀▀▘░░░░▝▗▙░▘░▗▛▘▒▒
───────▀▙░░░░░░░░░░░▝▀▘░▗▄▀▘▒▒▒▒
─────────▀▀▄▖░░░░░░░░▝▀▘░▐▖▒▒▒▒▒
──────▞█░░▟▘░░░░░░░░░░░░░░▙▒▒▒▒▒
─────▐▘▗▗▗▗▄░░░░░░░░░░░░░░█─▒▒▒▒
─────▐▖▄▘░░▝▚░░░░░░░░▗▟▀░░▖▝▄▒▒▒
──────▜▘▞▙▖▟▄▌█░░░░░░▛░░░▐█▗▌▌▒▒
──────▗▐▖▄▄▘▀▖▜░░░░░░▜░░░▖▚▛░▌▒▒
──────▝▄▙▀▙▖░▌▐░░░░░░▝▜▖░░▝▗▖─▒▒
───────▝▜▙░░░▌▐▙░░░░░▐░▖░▝▐▖▚▒▒▒
─────────▝▘▝▝▘░▝▝░▄▖░▐▗▖░░▗█▘▒▒
Please Type A Number Please:
1-Block
2-Unblock""")
    choice = input("Type Number:")
    if choice == "1":
        #This Is Adminstartor Checker
        if checkAdmin() == True:
            website = input("Input a Website:")
            #If You Didn't Add www. This Is Add www.
            if "www" not in website:
                x = "www." + website
                editBlock(x)
                print("Your Website Been Blocked Succesflly")
                input("Press Any Key To Exit..........")

            else:
                x = website
                editBlock(x)
                print("Your Website Been Blocked Succesflly")
                input("Press Any Key To Exit..........")
                sys.exit(0)
        elif checkAdmin() == False:
            print("This Script Only Run Adminstrartor ! Please Run Adminstartor")
            input("Press Any Key To Exit...........")
            sys.exit(0)
    elif choice == "2":
        if checkAdmin() == True:
            website = input("Input a Website:")
            if "www" not in website:
                x = "www." + website
            
                editUnblock(x)
                print("Your Website Been unBlocked Succesflly")
                input("Press Any Key To Exit..........")

            else:
                x = website
                editUnblock(x)
                print("Your Website Been unBlocked Succesflly")
                input("Press Any Key To Exit..........")
                sys.exit(0)
        elif checkAdmin() == False:
            print("This Script Only Run Adminstrartor ! Please Run Adminstartor")
            input("Press Any Key To Exit...........")
            sys.exit(0)


if __name__ == '__main__':
    main()
