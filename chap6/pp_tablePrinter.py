tableData = [['apples', 'oranges', 'cherries', 'bannana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(liste):
    colWidths = [0] * len(liste)
    tab_cols = len(colWidths)
    max_rows = 0

    for i in range(len(liste)):

        if max_rows <= len(liste[i]):
            max_rows = len(liste[i])

        for n in range(len(liste[i])):

            item_len = len(liste[i][n])

            if colWidths[i] <= item_len:
                colWidths[i] = item_len

    for n in range(max_rows):
        text_row = ''
        for i in range(tab_cols):
            if not liste[i][n]:
                text_row = text_row + '-'.rjust(colWidths[i] + 1)
            else:
                text_row = text_row + liste[i][n].rjust(colWidths[i] + 1)
        print(text_row)


printTable(tableData)
