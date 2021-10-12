a = ['poker', 'chess', 'risk']
print("poker, chess, and risk are the games I like")
gameFav = input('Enter your favorite game ')
a.append(gameFav)

while(gameFav != "Q"):
    gameFav = input('Enter your favorite game (type "Q" to quit): ')
    a.append(gameFav)
for i in a:
    print(i)