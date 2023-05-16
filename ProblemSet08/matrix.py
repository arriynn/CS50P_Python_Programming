def main():
    mat1= matrix1()
    mat2=matrix2()
    print(mat1[0]+mat2[0], mat1[1]+ mat2[1], mat1[2]+mat2[2])

def matrix1():
    matrix= []
    while len(matrix)<3:
        number= int(input("Number for 1st matrix: "))
        matrix.append(number)
        print("Matrix1= ", matrix)
    return matrix
def matrix2():
    matrix= []
    while len(matrix)<3:
        number= int(input("Number for 2nd matrix: "))
        matrix.append(number)
        print("Matrix2= ", matrix)
    return matrix

if __name__== "__main__":
    main()