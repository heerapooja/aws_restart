"""
Count Characters
"""
count = 0
f1 = open("preproinsulin-seq-clean.txt", "r")
f2 = open("binsulin-seq-clean.txt", "w")
   
ch = f1.read(24)
f2.write(ch)
f1.close()
f2.close()
