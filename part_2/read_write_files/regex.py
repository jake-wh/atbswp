from pathlib import Path
import re
# ----------------------------------------

def main(path):
    user_regex = input("Enter your regex here: ")
    pattern = re.compile(repr(user_regex)[1:-1])
    for file in path.glob('*.txt'):
        with open(file, 'r', encoding='UTF-8') as f:
            text = f.read()
            result = pattern.findall(string=text, pos=1, endpos=5)
            print(result)


if __name__ == '__main__':
    path = Path.cwd()
    main(path)
