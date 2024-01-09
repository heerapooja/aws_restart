#import count_char

f1 = open("preproinsulin-seq-clean.txt", "r")
f2 = open("cinsulin-seq-clean.txt", "w")

ch = f1.read(24)
ch = f1.read(30)
ch = f1.read(35)
f2.write(ch)

print("SUCCESS!!")
f1.close()
f2.close()
