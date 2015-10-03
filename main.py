from pathlib import Path
import os

def verify_search_command(action: str, arg: str) -> bool:
    search_commands = ['N', 'E', 'S']

    if action == None:
        return False
    
    if action in search_commands:
        if arg == None or len(arg) == 0:
            return False
        else:
            if action != 'S':
                return True
            else:
                try:
                    int(arg)
                    return True
                except:
                    return False
    else:
        return False

def verify_action(action: str) -> bool:
    actions = ['P', 'F', 'D', 'T']
    return action in actions
    
def search_by_name(root: str, file_name: str, search_result: list) -> None:
    files = Path(root).iterdir()
    try:
        for f in files:
            if f.is_dir():
                search_by_name(str(f), file_name, search_result)
            elif f.exists():
                if (f.name == file_name):
                    search_result.append(f)
    except PermissionError:
        print("Access denied: {}".format(root))
                
def search_by_ext(root:str, file_ext:str, search_result: list) -> None:
    files = Path(root).iterdir()
    try:
        for f in files:
            if f.is_dir():
                search_by_ext(str(f.resolve()), file_ext, search_result)
            elif f.exists():
                if (f.suffix == file_ext):
                    search_result.append(f)
    except PermissionError:
        print("Access denied: {}".format(root))

def search_by_size(root:str, file_size:int, search_result: list) -> None:
    files = Path(root).iterdir()
    try:
        for f in files:
            file_path = str(f)
            if f.is_dir():
                search_by_size(file_path, file_size, search_result)
            elif f.exists():
                if os.path.getsize(file_path) > file_size:
                    search_result.append(f)
    except PermissionError:
        print("Access denied: {}".format(root))
                
def handle_search(root:str, action:str, arg:str) -> None:
    search_result = []
    
    if action == 'N':
        search_by_name(root, arg, search_result)
    elif action == 'E':
        search_by_ext(root, arg, search_result)
    else: # S
        search_by_size(root, int(arg), search_result)

    return search_result

def print_file_paths(search_result: list) -> None:
    for f in search_result:
        print(str(f))


def open_read_first_line(search_result:list) -> None:
    for file in search_result:
        opened_file = None
        try:
            opened_file = open(str(file), 'r')
            all_words = opened_file.readline()
            print(str(all_words))
        except:
            print('Could not open file {}'.format(str(file)))
        finally:
            if opened_file != None:
                opened_file.close()


def handle_actions(action: str, search_result: list) -> None:
    if action == 'P':
        print_file_paths(search_result)
    elif action == 'F':
        open_read_first_line(search_result)
    elif action == 'D':
        pass
    else: # T
        pass


    

def main() -> None:
    root = input().strip()
    while not Path(root).is_dir():
        print("ERROR")
        root = input().strip()

    second_line = input().strip()

    search_command = None
    arg = None
    if len(second_line) > 0:
        search_command = second_line[0]
        arg = second_line[2:] if len(second_line) > 2 else None

    while not verify_search_command(search_command, arg):
        print("ERROR")
        second_line = input().strip()

        if len(second_line) > 0:
            search_command = second_line[0]
            arg = second_line[2:] if len(second_line) > 2 else None
        else:
            search_command = None

    
    search_result = handle_search(root, search_command, arg)

    action = input()
    while not verify_action(action):
        print("ERROR")
        action = input()

    handle_actions(action, search_result)
        

if __name__ == '__main__':
    main()
