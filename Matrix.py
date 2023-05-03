s = input('количество строк: ')
c = input('количсевто столбцов:')

# количество строк должно быть больше чем столбцов!

string = int(s) # строки
column = int(c) # столбцы

matrix = [[0] * column] * string
print('matrix =: ', matrix)

index = 0

for i in range(string):
    if i % 2 != 0:
        for j in range(column - 1, -1, -1):
            index = index + 1
            matrix[i][j] = index
        print(matrix[j])
    else:
        for j in range(column):
            index = index + 1
            matrix[i][j] = index
        print(matrix[j])