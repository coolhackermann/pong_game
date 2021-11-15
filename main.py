with open('assets/main2.txt', 'r') as f:
    x = f.read()
    #print(x)



    with open('assets/main2.txt', 'w') as f2:
            if x == '0':
                f2.write('1')
                from assets import pong
            elif x == '1':
                f2.write('2')
                from assets import pong
            elif x == '2':
                f2.write('3')
                from assets import pong
            elif x == '3':
                f2.write('4')
                from assets import pong
            elif x == '4':
                f2.write('0')
                from assets import emoji

with open('assets/main2.txt', 'r') as check:
    x = check.read()
    print(x)


