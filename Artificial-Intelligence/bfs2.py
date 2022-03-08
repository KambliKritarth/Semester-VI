''' bfs for 8 puzzle
'''
start_matrix = [[1,2,3],[7,0,6],[4,5,8]]
goal_matrix = [[1,2,3],[4,5,6],[7,8,0]]
def up(matrix0,a,b):
    temp = matrix0[a][b]
    matrix0[a][b] = matrix0[a-1][b]
    matrix0[a-1][b] = temp
    return matrix0

def left(matrix1,a,b):
    temp = matrix1[a][b]
    matrix1[a][b] = matrix1[a][b-1]
    matrix1[a][b-1] = temp
    return matrix1
    

def right(matrix2,a,b):
    temp = matrix2[a][b]
    matrix2[a][b] = matrix2[a][b+1]
    matrix2[a][b+1] = temp
    return matrix2

def down(matrix,a,b):
    temp = matrix[a][b]
    matrix[a][b] = matrix[a+1][b]
    matrix[a+1][b] = temp
    return matrix

#print("Starting state is:")
matrix_list =[]

def zero_indicator(matrix):
    row = 0
    for i in matrix:
        column = 0
        for j in i:
            #print(j,end = ",")

            if j == 0:
                print(row)
                print(column)
                if row!=0:
                    mat1 = up(matrix,row,column)
                    print("After swapping matrix is:")
                    for k in mat1:
                        for l in k:
                            print(l,end = ",")
                        print("\n")
                    matrix_list.append(mat1)
                    print(matrix_list)
                matrix_list.append(mat1)
                if column!=0:
                    mat2 =left(matrix,row,column)
                    print("After swapping matrix is:")
                    for k in mat2:
                        for l in k:
                            print(l,end = ",")
                        print("\n")
                    matrix_list.append(mat2)
                if row!=2:
                    mat3 = down(matrix,row,column)
                    print("After swapping matrix is:")
                    for k in mat3:
                        for l in k:
                            print(l,end = ",")
                        print("\n")
                    matrix_list.append(mat3)
                if column!=2:
                    mat4 = right(matrix,row,column)
                    print("After swapping matrix is:")
                    for k in mat4:
                        for l in k:
                            print(l,end = ",")
                        print("\n")
                    matrix_list.append(mat4)
                    print(matrix_list)
            column = column + 1
        row = row + 1
        
    '''for matrice in matrix_list:
        if matrice != goal_matrix:
            zero_indicator(matrice)
        else:
            print("Goal State Reached")'''

zero_indicator(start_matrix)
