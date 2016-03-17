tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidth = [0] * len(table)

    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j + 1])




printTable(tableData)

