"""
Text file cleaning
"""   
f1 = open("preproinsulin-seq-clean.txt", "w")
f2 = open("preproinsulin-seq.txt","r")
while 1:
    scan = f2.read(1)
    if(scan>='a' and scan<='z'):
        #print(scan.read())
        f1.write(scan)
    break
print("Your file get cleaned !!")        
f1.close()

    