from msvcrt import getch
while True:
    keypress = ord(getch())
    print(keypress)
    if keypress == 13:
        break
