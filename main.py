from pathlib import Path
import os

ACTIONS = {'N': True, 'E': True, 'S': True, 'P': False, 'F': False, 'D': False, 'T': False}

search_result = []

def verify_action(action: str, arg: str) -> bool:
    if action == None:
        return False
    
    available_actions = ACTIONS.keys()
    if action in available_actions:
        if ACTIONS[action]:
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
            return True
    else:
        return False

def search_by_name(root: str, file_name: str) -> None:
    files = Path(root).iterdir()
    for f in files:
        if (f.is_dir()):
            search_by_name(str(f.resolve()), file_name)
        else:
            if (f.name == file_name):
                search_result.append(f)
                
def search_by_ext(root:str, file_ext:str) -> None:
    files = Path(root).iterdir()
    for f in files:
        if (f.is_dir()):
            search_by_ext(str(f.resolve()), file_ext)
        else:
            if (f.suffix == file_ext):
                search_result.append(f)


def search_by_size(root:str, file_size:int) -> None:
    files = Path(root).iterdir()
    for f in files:
        file_path = str(f.resolve())
        if (f.is_dir()):
            search_by_size(file_path, file_size)
        else:
            if os.path.getsize(file_path) > file_size:
                search_result.append(f)
                
def handle_search(root:str, action:str, arg:str) -> None:
    if action == 'N':
        search_by_name(root, arg)
    elif action == 'E':
        search_by_ext(root, arg)
    elif action == 'S':
        search_by_size(root, int(arg))
    
def main() -> None:
    root = input().strip()
    while not Path(root).is_dir():
        print("ERROR")
        root = input().strip()

    second_line = input().strip()

    action = None
    arg = None
    if len(second_line) > 0:
        action = second_line[0]
        arg = second_line[2:] if len(second_line) > 2 else None

    while not verify_action(action, arg):
        print("ERROR")
        second_line = input().strip()

        if len(second_line) > 0:
            action = second_line[0]
            arg = second_line[2:] if len(second_line) > 2 else None
        else:
            action = None

    handle_search(root, action, arg)
    print(search_result)

if __name__ == '__main__':
    main()
