#Odd even number
# def oddEven(val):
#     val = int(input("Type any number: "))
#
#     if val % 2==0:
#         print("It is an even number")
#     else:
#         print("It is an odd number")
#
# oddEven(12)



#Word count

# def wordCount():
#
#     word = input("Type any word: ")
#     wordList= word.split()
#     print(wordList)
#     count = len(wordList)
#     print(count)
# wordCount()


#BioGraphy Summary

def bioGraphy():
    name = input("What is your name?")
    if len(name)<=2 and name == "*":
        print("Please type correct name")
        name = input("What is your name?")
    dob = input("Your date of birth in dd/mm/yyyy format: ")





    place = input("Your place of birth?: ")

    yourBio = f"My name is {name}, I am borth and brough up in {place}, It is a beautiful place" \
              f"i really like my neighbourhood. Oh yes my birth date is {dob}"
    print(yourBio)
bioGraphy()








