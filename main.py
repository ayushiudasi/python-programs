import string
import random
if __name__ == "__main__":
    s1=string.ascii_letters
    s2=string.ascii_lowercase
    s3=string.ascii_uppercase
    s4=string.punctuation
    n=(input("Enter length of password\n"))
    
    while (True):
        if(n.isdigit()):
            s=[]
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            # random.shuffle(s)
            print("Your password is :")
            # print("".join(s[0:n]))
            print("".join(random.sample(s,int(n))))
            break
        else:
            print("Please enter digits")
            n=(input("Enter length of password\n"))
    

