#Problem 3_4
def replace_color(matrix, x, y, k):
    z = matrix[x][y]
    rows = len(matrix)
    cols = len(matrix[0])
    visited = set() 
    
    def m(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] != z or (i,j) in visited:
            return
        matrix[i][j] = k
        visited.add((i,j))
        m(i-1, j)
        m(i+1, j)
        m(i, j-1)
        m(i, j+1)
    
   
    m(x, y)
    return matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):  
    row = input(f"Enter space-separated values for row {i}: ").split()
    matrix.append([int(x) for x in row])

x, y, k = input("Enter index x, y, k (separated by whitespace): ").split()
x, y, k = int(x), int(y), int(k)

print("q")

result = replace_color(matrix, x, y, k)

for row in result:
    print(" ".join([str(x) for x in row]))