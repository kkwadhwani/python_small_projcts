a = input("Type your word to know if it is palindrom: ")

b = []
for i in a:
    b.append(str(i))
print(b)
c = b.copy()
c.reverse()
print(c)
