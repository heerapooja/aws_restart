#file handling
try:
    f1=open("file1.txt","r")
    print(f1.read())
    f1.close()
except:
    print("FILE DOES NOT EXIST, CREATE THE FILE FIRST")