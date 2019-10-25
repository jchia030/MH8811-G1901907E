def genPassword(n):
    import random
    import string
    import re
    i=0
    while i<4:    
        password=''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(n)])
        i=0
        if re.search(r'[a-z]',password):
            i+=1
        if re.search(r'[A-Z]',password):
            i+=1
        if re.search(r'[0-9]',password):
            i+=1
        if re.search(r'[@_!#$%^&*()<>?/\|}{~:]',password):
            i+=1
    return password
    
if __name__=="__main__":
    print(genPassword(12))
