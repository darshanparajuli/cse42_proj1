from pathlib import Path

def search_by_name(root, file_name):
    print('search by name')

#FLAGS = {'N': search_by_name}


#def N_Function(

def function_NES(first_letter:str, last_part:str):
    if first_letter == 'N':
        print('You typed N')

def main():
    while 1:
        root = input()
        while not Path(root).is_dir():
            print("ERROR")
            root = input()

        flag = input()

        first_letter = flag[0]
        last_part = flag[2:]
        print(first_letter, last_part)
        function_NES(first_letter, last_part)
        

if __name__ == '__main__':
    main()
