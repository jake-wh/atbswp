from pathlib import Path
import re
# ----------------------------------------

# Mad libs program
def main(path):
    for file in path.glob('*.txt'):
        with open(file, 'r', encoding='UTF-8') as f:
            text = f.read()
            pattern = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
            replace = pattern.findall(text)

            adj = input('Enter an adjective: ')
            noun = input('Enter a noun: ')
            verb = input('Enter a verb: ')
            adv = input('Enter an adverb: ')

            for word in replace:
                match word:
                    case 'NOUN':
                        text = text.replace('NOUN', noun, 1)
                    case 'ADJECTIVE':
                        text = text.replace('ADJECTIVE', adj, 1)
                    case 'VERB':
                        text = text.replace('VERB', verb, 1)
                    case 'ADVERB':
                        text = text.replace('ADVERB', adv, 1)
            print(text)
            new_f = open(f'new_{file.stem}.txt', 'w', encoding='UTF-8')
            new_f.write(text)
            new_f.close()

if __name__ == '__main__':
    path = Path.cwd()
    main(path)
    
