with open('assets/main.txt', 'r') as f:
    x = f.read()
    #print(x)



    with open('assets/main.txt', 'w') as f2:
            if x == '0':
                f2.write('1')
                from assets import pong.py
            elif x == '1':
                f2.write('2')
                from assets import pong.py
            elif x == '2':
                f2.write('3')
                from assets import pong.py
            elif x == '3':
                f2.write('4')
                import pong.py
            elif x == '4':
                f2.write('0')
                from assets import emoji.py

with open('assets/main.txt', 'r') as check:
    x = check.read()
    print(x)


if __name__ == "__main__":
    main()
