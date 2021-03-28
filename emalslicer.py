email= input("what is your email address: ")

splitEmail= email.split('.')
fname= splitEmail[0]
lname= splitEmail[1].split('@')[0]


print(f"Hi {fname} {lname} how are you")


