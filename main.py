import sys


def test():
    input_file = "./input_files/test_input_1.txt"
    expected_output_file = "./input_files/test_expected_output_1.txt"
    output_file = "./results/test_output_1.txt"

    my_main(input_file, output_file)

    with open(output_file, 'r') as f:
        generated_output = f.read()
    with open(expected_output_file, 'r') as f:
        expected_output = f.read()

    if generated_output != expected_output:
        print(f"Test case 1 failed: Output = {generated_output}, Expected = {expected_output}")
        sys.exit(1)

    print("All test cases pass")


def parse_in(input_file_name):
    matrix = []
    with open(input_file_name, "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            row = [char for char in line.strip() if char != ' ']
            matrix.append(row)

    num_rows = len(matrix)
    num_columns = len(matrix[0]) if matrix else 0

    return num_rows, num_columns, matrix


def parse_out(output_file_name, num_rows, num_columns, sol_matrix):
    with open(output_file_name, 'w') as file:
        file.write(f"{num_rows} {num_columns}\n")
        for row in sol_matrix:
            file.write(' '.join(row) + '\n')


def solve(num_rows, num_columns, matrix):
    # Function to calculate minesweeper numbers
    def calculate_number(matrix, row, col):
        count = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < num_rows and 0 <= new_col < num_columns:
                if matrix[new_row][new_col] == 'x':
                    count += 1
        return str(count) if count > 0 else 'o'

    for i in range(num_rows):
        for j in range(num_columns):
            if matrix[i][j] == 'o':
                matrix[i][j] = calculate_number(matrix, i, j)

    return matrix


def my_main(input_file_name, output_file_name):
    (num_rows, num_columns, matrix) = parse_in(input_file_name)

    sol_matrix = solve(num_rows, num_columns, matrix)

    parse_out(output_file_name, num_rows, num_columns, sol_matrix)


if __name__ == '__main__':
    # 1. We use as many input arguments as needed
    input_file_name = "./input_files/input_1.txt"
    output_file_name = "./results/output.txt"

    if (len(sys.argv) > 1):
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]

    test()
    my_main(input_file_name, output_file_name)
