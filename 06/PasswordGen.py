def genPassword(n):
    i=0
    while i<4:    
        password=''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(n)])
        i=0
        if re.search(r'[a-z]',password):
            i+=1
        if re.search(r'[A-Z]',password):
            i+=1
        if re.search(r'/d',password):
            i+=1
        if re.search(r'[@_!#$%^&*()<>?/\|}{~:]',password):
            i+=1
    print(password)
    
genPassword(12)
