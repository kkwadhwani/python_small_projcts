dob = input("Your birth date in this format dd/mm/yyyy: ")
yourDob = f"{dob}"
newDob = yourDob.split('.')
print(newDob)

check = True
while check:
    if len(str((newDob[0])))!=2 or len(str(newDob[1]))!=2 or len(str(newDob[2]))!=4:
        print("Your date format is no good use this format dd/mm/yyyy")
        dob = input("Your birth date in this format dd/mm/yyyy: ")
        yourDob = f"{dob}"
        newDob = yourDob.split('.')



    if "." in yourDob:
            print("incorrect")
            dob = input("Your birth date in this format dd/mm/yyyy: ")
            yourDob = f"{dob}"
    else:
       check = False
print("next")





a = [22, 22, 9000]

print(len(str(a[0])))