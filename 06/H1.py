from genPassword import Passwordgen

length=input('How long is your password?')
while length<4:
    length=input('Pls key in at least 4. How long is your password?')
print(Passwordgen(length))
    
