from pathlib import Path

def search_by_name(root, file_name):
    print('search by name')

FLAGS = {'N': search_by_name}

def main():
    while 1:
        root = input()
        while not Path(root).is_dir():
            print("ERROR")
            root = input()

        flag = input().split()
        

if __name__ == '__main__':
    main()
