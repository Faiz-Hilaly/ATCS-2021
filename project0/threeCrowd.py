a = ['amy', 'ben', 'connor', 'daisy']
def crowd_test(a):
    if(len(a) > 3):
        print(' room is crowded')

crowd_test(a)
a.pop()
a.pop()
crowd_test(a)