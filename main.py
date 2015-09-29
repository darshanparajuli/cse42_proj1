from pathlib import Path

def search_by_name(root:str, file_name:str, result):
    files = Path(root).iterdir()
    for f in files:
        if (f.is_dir()):
            search_by_name(f.resolve(), file_name, result)
        else:
            if (f.name == file_name):
                result.append(f)
                

def function_NES(root:str, first_letter:str, last_part:str):
    if first_letter == 'N':
        result = []
        search_by_name(root, last_part, result)
        print(result)

def main():
    root = input()
    while not Path(root).is_dir():
        print("ERROR")
        root = input()

    flag = input()
    
    first_letter = flag[0]
    last_part = flag[2:]
    # print(first_letter, last_part)
    function_NES(root, first_letter, last_part)
        

if __name__ == '__main__':
    main()
