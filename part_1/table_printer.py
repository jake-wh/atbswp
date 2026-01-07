tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    col_width = [0] * len(tableData)
    for i in range(len(table)):
        col_width[i] = len(max(table[i], key=len))
    
    result = []
    col, word = 0, 0
    rows = min(len(row) for row in table)

    while True:
        while col < len(table):
            result.append(table[col][word].rjust(col_width[col]) + ' ')
            col += 1
        result.append('\n')
        print(result)
        word += 1
        col = 0
        if word == rows:
            break
    
    print(''.join(result))


print_table(tableData)


