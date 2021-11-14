with open('main.txt', 'r') as f:
    x = f.read()
    #print(x)



    with open('main', 'w') as f2:
            if x == '0':
                f2.write('1')
                import pong.py
            elif x == '1':
                f2.write('2')
                import pong.py
            elif x == '2':
                f2.write('3')
                import pong.py
            elif x == '3':
                f2.write('4')
                import pong.py
            elif x == '4':
                f2.write('0')
                import emoji.py

with open('main', 'r') as check:
    x = check.read()
    print(x)


if __name__ == "__main__":
    main()
