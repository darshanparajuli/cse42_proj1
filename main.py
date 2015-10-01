from pathlib import Path

ACTIONS = {'N':True, 'E':True, 'S':True, 'P':False, 'F':False, 'D':False, 'T':False}

def verify_action(action: str, arg: str) -> bool:
    if action == None:
        return False
    
    available_actions = ACTIONS.keys()
    if action in available_actions:
        if ACTIONS[action]:
            return arg != None and len(arg) != 0
        else:
            return True
    else:
        return False

def search_by_name(root: str, file_name: str, result: list) -> None:
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

def main() -> None:
    root = input().strip()
    while not Path(root).is_dir():
        print("ERROR")
        root = input().strip()

    second_line = input().strip()

    action = None
    arg = None
    if len(second_line) > 2:
        action = second_line[0]
        arg = second_line[2:] if len(second_line) > 2 else None

    while not verify_action(action, arg):
        print("ERROR")
        second_line = input().strip()
        
        if len(second_line) > 2:
            action = second_line[0]
            arg = second_line[2:] if len(second_line) > 2 else None
        else:
            action = None
    
    function_NES(root, action, arg)
        

if __name__ == '__main__':
    main()
