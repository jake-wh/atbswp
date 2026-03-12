# A REVIEW OF REGEX SYMBOLS

# This chapter has covered a lot of notation so far, so here’s a quick review of what you’ve learned about basic regular expression syntax:

# The ? matches zero or one instance of the preceding qualifier.
# The * matches zero or more instances of the preceding qualifier.
# The + matches one or more instances of the preceding qualifier.
# The {n} matches exactly n instances of the preceding qualifier.
# The {n,} matches n or more instances of the preceding qualifier.
# The {,m} matches 0 to m instances of the preceding qualifier.
# The {n,m} matches at least n and at most m instances of the preceding qualifier.
# {n,m}? or *? or +? performs a non-greedy match of the preceding qualifier.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# The \d, \w, and \s match a digit, word, or space character, respectively.
# The \D, \W, and \S match anything except a digit, word, or space character, respectively. [abc] matches any character between the square brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the square brackets.
# (Hello) groups 'Hello' together as a single qualifier.
# ----------------------------------------
import re, pyperclip

phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # Area code (optional)
    (\s|-|\.)? # Separator
    (\d{3}) # First 3 digits
    (\s|-|\.) # Separator
    (\d{4}) # Last 4 digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # Extention (optional)
    )''', re.VERBOSE
)

# Create email regex.

email_re = re.compile(
    r'''(
    [a-zA-Z0-9._%+-]+ # Username
    @ # @ Symbol
    [a-zA-Z0-9.-]+ # Domain name
    (\.[a-zA-Z]{2,4}) # Dot-something
    )''', re.VERBOSE
)

# Find matches in clipboard text.

text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)

for groups in email_re.findall(text):
    matches.append(groups[0])


# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')