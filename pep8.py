import sys


text = 'abcdefghijklmnop'


def main():

    temp = text.replace('a', 'TURD').replace('d', 'TURD').replace('j', 'TURD')
    .replace('o', 'TURD')
    print temp

if __name__ == '__main__':
    main()
