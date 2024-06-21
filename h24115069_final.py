def get_matrix(matrix_name):
    matrix = {}
    while True:
        try:
            matrix_str = input(f"Enter matrix {matrix_name} : ")
            rows = matrix_str.split("|")
            for row_index, row in enumerate(rows):
                matrix[row_index] = [float(x) for x in row.split(",")]
            return matrix
        except ValueError:
            print("Invalid matrix format. Please enter a comma-separated list of numbers for each row, separated by pipes (|) between rows.")

if __name__ == "__main__":
    matrix_u = {}
    while True:
        try:
            matrix_str = input("Enter matrix U: ")
            rows = matrix_str.split("|")
            for row_index, row in enumerate(rows):
                matrix_u[row_index] = [float(x) for x in row.split(",")]
            break
        except ValueError:
            print("Invalid matrix format. Please enter a comma-separated list of numbers for each row, separated by pipes (|) between rows.")

    matrix_v = {}
    while True:
        try:
            matrix_str = input("Enter matrix V: ")
            rows = matrix_str.split("|")
            for row_index, row in enumerate(rows):
                matrix_v[row_index] = [float(x) for x in row.split(",")]
            break
        except ValueError:
            print("Invalid matrix format. Please enter a comma-separated list of numbers for each row, separated by pipes (|) between rows.")

    if len(matrix_u) != len(matrix_v):
        print("Error: Matrices U and V must be of the same size.")
    else:
        n = len(matrix_u)

        result_matrix = {}
        for i in range(n):
            result_matrix[i] = {}
            for j in range(n):
                result_matrix[i][j] = sum(matrix_u[i][k] * matrix_v[k][j] for k in range(n))

        print("M = U X V")
        for i in range(n):
            row = [result_matrix[i][j] for j in range(n)]
            print(','.join(map(str, row)))
