#Commit 1

#OneTwo.py
varOne = "This is a message"
print(varOne)
varOne = "This is a different message"
print(varOne)

#firstName.py
first_name = 'faiz'
print(first_name.title())
print(first_name.upper())

#order.py
print(4+5*3)
print((4+5)*3)


#Commit 2

#firstList.py
l = ['python','c','java']
print(*l)

#firstListLoop.py
l = ['python','c','java']
for x in range(len(l)):
	print(l[x])

#workingList.py
a = ['programmer', 'truck driver', 'teacher', 'athlete']
print(a.index('programmer'))

a.append('policeman')
a.insert(0, 'gangster')

for x in range(len(a)):
	print(a[x])

#alphaSlices.py
alphabet = ['a','b','c','d','e','f','g','h','i','j']
for i in alphabet[0:3]:
    print(i)
for i in alphabet[3:7]:
    print(i)
for i in alphabet[5:len(alphabet)]:
    print(i)

#firtTwenty.py
nums = []
for i in range(1, 21):
    nums.append(i)
    print(i)

#multTen.py
nums = []
for i in range(10, 110, 10):
    nums.append(i)
    print(i)


#Commit 3
#addCalc.py
def addition(num1, num2):
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))

addition(10, 20)
addition(100, 200)
addition(3, 4)

#Commit 4
#threeCrowd.py
a = ['amy', 'ben', 'connor', 'daisy']
def crowd_test(a):
    if(len(a) > 3):
        print(' room is crowded')

crowd_test(a)
a.pop()
a.pop()
crowd_test(a)

#Commit 5
#gamePref.py
a = ['poker', 'chess', 'risk']
print("poker, chess, and risk are the games I like")
gameFav = input('Enter your favorite game: ')
a.append(gameFav)
for i in a:
    print(i)

#manyGames.py
a = ['poker', 'chess', 'risk']
print("poker, chess, and risk are the games I like")
gameFav = input('Enter your favorite game ')
a.append(gameFav)

while(gameFav != "Q"):
    gameFav = input('Enter your favorite game (type "Q" to quit): ')
    a.append(gameFav)
for i in a:
    print(i)

#Commit 6
#petNames.py
dict = {}
dict['Clifford'] = 'dog'
dict['Manny'] = 'cat'
dict['Bentham'] = 'bird'

for key in dict.keys():
    print(key + ' is a ' + dict[key])

#mtnHeights.py
dict = {}
dict['Mount Everest'] = '29029'
dict['K2'] = '28251'
dict['Kanghenjunga'] = '28169'
dict['Lhotse'] = '27940'
dict['Makalu'] = '27838'

for key in dict.keys():
    print(key + ' is ' + dict[key] + ' feet tall')






