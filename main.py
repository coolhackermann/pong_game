with open('main.txt', 'r') as f:
    x = f.read()
    #print(x)



    with open('main.txt', 'w') as f2:
            if x == '0':
                f2.write('1')
                import pong
            elif x == '1':
                f2.write('2')
                import pong
            elif x == '2':
                f2.write('3')
                import pong
            elif x == '3':
                f2.write('4')
                import pong
            elif x == '4':
                f2.write('0')
                import emoji

with open('main.txt', 'r') as check:
    x = check.read()
    print(x)


