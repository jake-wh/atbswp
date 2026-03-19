from pathlib import Path
# ----------------------------------------

# Generate test txt files

if __name__ == '__main__':
    path = Path.cwd()
    texts = [
        'The ADJECTIVE cat jumped over the NOUN and then VERB. A nearby NOUN was unaffected by these events.',
        'My ADJECTIVE friend bought a NOUN and decided to VERB. The NOUN in the corner remained silent.',
        'A ADJECTIVE scientist discovered a NOUN and began to VERB. The nearby NOUN showed no reaction.',
        'The ADJECTIVE chef prepared a NOUN and started to VERB. A dusty NOUN sat on the shelf.',
        'An ADJECTIVE wizard summoned a NOUN and proceeded to VERB. The ancient NOUN nearby glowed faintly.',
        'The ADJECTIVE robot found a NOUN and attempted to VERB. A broken NOUN lay in the corner.',
        'My ADJECTIVE neighbor carried a NOUN and wanted to VERB. The old NOUN next door stayed quiet.',
        'A ADJECTIVE dragon guarded a NOUN and refused to VERB. The shiny NOUN underneath sparkled brightly.',
        'The ADJECTIVE detective examined the NOUN and chose to VERB. A mysterious NOUN remained hidden.',
        'An ADJECTIVE pirate discovered a NOUN and decided to VERB. The wooden NOUN on deck creaked softly.'
    ]

    for i in range(len(texts)):
        with open(f'text_{i}.txt', 'w', encoding='UTF-8') as file:
            file.write(texts[i])
    
