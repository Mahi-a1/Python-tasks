import numpy as np

def get_matrix(prompt):
    print(f"\n{prompt}")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter matrix row-wise (separated by space):")
    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Column count mismatch. Try again.")
            return get_matrix(prompt)
        matrix.append(row)

    return np.array(matrix)

def print_matrix(matrix, label="Matrix"):
    print(f"\n{label}:")
    print(np.array2string(matrix, precision=2, separator=' ', suppress_small=True))

def menu():
    print("\n Matrix Operations Tool")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose a Matrix")
    print("5. Calculate Determinant")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("\nChoose an operation (1–6): ")

        if choice == '1':
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape != B.shape:
                print("Error: Shapes don't match for addition.")
            else:
                result = A + B
                print_matrix(result, "A + B")

        elif choice == '2':
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape != B.shape:
                print("Error: Shapes don't match for subtraction.")
            else:
                result = A - B
                print_matrix(result, "A - B")

        elif choice == '3':
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape[1] != B.shape[0]:
                print("Error: Incompatible shapes for multiplication.")
            else:
                result = A @ B
                print_matrix(result, "A × B")

        elif choice == '4':
            A = get_matrix("Matrix to Transpose")
            result = A.T
            print_matrix(result, "Transpose")

        elif choice == '5':
            A = get_matrix("Matrix (Square Only)")
            if A.shape[0] != A.shape[1]:
                print("Error: Matrix must be square to find determinant.")
            else:
                det = np.linalg.det(A)
                print(f"\nDeterminant: {det:.2f}")

        elif choice == '6':
            print("\nExiting Matrix Operations Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 6.")

if __name__ == "__main__":
    main()
