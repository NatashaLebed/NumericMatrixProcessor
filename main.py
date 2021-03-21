def add_matrices():
    n, m, a = input_matrix(matrix_number="first")
    q, k, b = input_matrix(matrix_number="second")

    # Check if matrices have the same dimensions
    if n != q and m != k:
        print('The operation cannot be performed.')
    else:
        c = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]
        print_matrix(c)


def scalar_multiplication(a, n, m, scalar):
    # multiply every item of matrix A(n x m) by a scalar
    b = [[scalar * float(a[i][j]) for j in range(m)] for i in range(n)]
    return b


def multiply_matrices():
    n, m, a = input_matrix(matrix_number="first")  # matrix A(n x m)
    q, k, b = input_matrix(matrix_number="second")  # matrix B(q x k)

    # Check if matrices have the same dimensions
    if m != q:
        print('The operation cannot be performed.')
    else:
        result_matrix = []
        for i in range(n):
            result_row = []
            for j in range(k):
                dot_product = 0
                for t in range(m):
                    dot_product += a[i][t] * b[t][j]
                result_row.append(dot_product)
            result_matrix.append(result_row)
        print_matrix(result_matrix)


def transpose_matrix(n, m, a, choice='1'):
    if choice == '1':
        b = [[a[i][j] for i in range(n)] for j in range(m)]
    # range(n - 1, -1, -1) is reverse of range(n), from n - 1 to 0
    elif choice == '2':
        b = [[a[i][j] for i in range(n - 1, -1, -1)] for j in range(m - 1, -1, -1)]
    elif choice == '3':
        b = [[a[i][j] for j in range(m - 1, -1, -1)] for i in range(n)]
    elif choice == '4':
        b = [[a[i][j] for j in range(m)] for i in range(n - 1, -1, -1)]
    return b


def determinant(k, a):
    det = 0
    if k == 1:
        return a[0][0]
    if k == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    else:
        for j in range(k):
            sign = (-1) ** (0 + j)
            minor_matrix = [row[:j] + row[j + 1:] for row in a[1:k]]
            det += sign * a[0][j] * determinant(k-1, minor_matrix)
        return det


def inverse_matrix(n, m, a):
    det = determinant(n, a)
    if det == 0:
        print("This matrix doesn't have an inverse.")
    else:
        c = []
        for i in range(n):
            c_row = []
            for j in range(m):
                sign = (-1) ** (i + j)
                minor_matrix = [row[:j] + row[j + 1:] for row in a[:i] + a[i+1:]]
                c_row.append(sign * determinant(len(minor_matrix), minor_matrix))
            c.append(c_row)
        k = len(c)
        c_transpose = transpose_matrix(k, k, c)
    return scalar_multiplication(c_transpose, k, k, 1 / det)


def input_matrix(matrix_number=""):
    n, m = input(f'Enter size of {matrix_number} matrix:').split()
    print(f'Enter {matrix_number} matrix:')
    matrix = [[float(i) for i in input().split()] for _ in range(int(n))]
    return int(n), int(m), matrix


def print_matrix(matrix):
    print('The result is:')
    for row in matrix:
        print(*row)
    print()


def print_main_menu():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')


def print_transpose_menu():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')


while True:
    print_main_menu()
    menu_choice = input('Your choice:')

    if menu_choice == '0':
        break
    if menu_choice == '1':
        add_matrices()
    if menu_choice == '2':
        n, m, a = input_matrix()  # matrix A(n x m)
        scalar = float(input('Enter constant:'))
        result_matrix = scalar_multiplication(a, n, m, scalar)
        print_matrix(result_matrix)
    if menu_choice == '3':
        multiply_matrices()
    if menu_choice == '4':
        print_transpose_menu()
        choice = input('Your choice:')  # choose type of transposition
        n, m, a = input_matrix()  # matrix A(n x m)
        result_matrix = transpose_matrix(n, m, a, choice)
        print_matrix(result_matrix)
    if menu_choice == '5':
        n, m, matrix = input_matrix()  # matrix A(n x m)
        print('The result is:')
        print(determinant(n, matrix))
    if menu_choice == '6':
        n, m, a = input_matrix()  # matrix A(n x m)
        print_matrix(inverse_matrix(n, m, a))