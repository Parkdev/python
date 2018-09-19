import sys

def buy_item():
    print('buy item!')

def show_info():
    print('shop module')

if __name__ == '__main__':
    buy_item()
    print(__name)
    print(sys.argv)

