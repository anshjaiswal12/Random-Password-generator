import string
import random
val=1
while val==1:
    lower=string.ascii_lowercase
    upper=string.ascii_lowercase
    digits=string.digits
    symbols=string.punctuation
    name=input("Enter your name>>")
    all=lower + upper + digits +symbols
    length=int(input("Enter the length of password which should not be more than 94>>"))
    if length<=94:
        password= "".join(random.sample(all,length))
        print("Hi!",name,"your random password is written here")
        print("-->",password)
    elif length>95:
        print("The length is more than 94. Plese enter smaller number")
    else:
        print("wrong input")
    print("Want to create more passwords?")
    print("enter - Yes for creating more")
    print(("enter - No to exit"))
    inp=input("Enter yes or no>>")
    inp=inp.lower()
    if inp=="yes":
        continue
    else:
        break
print("Thanks for using code by Ansh Jaiswal")
print("For any information contact - contact.arthj@gmail.com")
