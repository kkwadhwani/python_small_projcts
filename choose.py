songs = """Welcome, please select a select a song from this top 10 songs:

1. Baby by Bieber
2. Hotline Bling by Drake
3. Flawless by Beyonce
4. Fall by Eminem...
"""

print(songs)

select = True
while select:

    selectSong = input("Select which song you want to listen type a number: ")

    if selectSong==3:
        print("""You chose Flawless by Beyonce. Here you go:
    
    ------- Flawless by Beyonce ------------
    I'm out that H, town coming coming down
    I'm coming down, drippin' candy on the ground
    H, Town, Town, I'm coming down, coming down
    Drippin' candy on the ground...
        
        """)

    selectAnother= input("Type * if you want to see other songs: ")
    print(songs)
    selectSong = input("Select which song you want to listen type a number: ")

