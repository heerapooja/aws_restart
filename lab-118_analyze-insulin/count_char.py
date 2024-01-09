"""
Count Characters
"""
def countChar():
    l = 0
    with open("ainsulin-seq-clean.txt", "r") as f1:
        for line in f1:
            l += len(line)
    print(l)
    
countChar()