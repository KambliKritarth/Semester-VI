''' bfs for 8 puzzle
'''
start_matrix = [[1,2,3],[7,4,6],[0,5,8]]
goal_matrix = [[1,2,3],[4,5,6],[7,8,0]]
def up(matrix0,a,b):
    temp = matrix0[a][b]
    matrix0[a][b] = matrix0[a-1][b]
    matrix0[a-1][b] = temp

def left(matrix1,a,b):
    temp = matrix1[a][b]
    matrix1[a][b] = matrix1[a][b-1]
    matrix1[a][b-1] = temp
    

def right(matrix2,a,b):
    temp = matrix2[a][b]
    matrix2[a][b] = matrix2[a][b+1]
    matrix2[a][b+1] = temp

def down(matrix,a,b):
    temp = matrix[a][b]
    matrix[a][b] = matrix[a+1][b]
    matrix[a+1][b] = temp

#print("Starting state is:")
matrix_list = []

def zero_indicator(matrix):
    row = 0
    for i in matrix:
        for j in i:
            #print(j,end = ",")
            column = 0

            if j == 0:
                print(row)
                print(column)
                if row!=0:
                    up(matrix,row,column)
                    print("After swapping matrix is:")
                    for k in matrix:
                        for l in k:
                            print(l,end = ",")
                        print("\n")
                    mat = matrix
                    matrix_list.append(mat)
                    up(matrix,row,column)
                if column!=0:
                    left(matrix,row,column)
                    print("After swapping matrix is:")
                    for k in matrix:
                        for l in k:
                            print(l,end = ",")
                        print("\n")
                    mat = matrix
                    matrix_list.append(mat)
                    left(matrix,row,column)
                if row!=2:
                    down(matrix,row,column)
                    print("After swapping matrix is:")
                    for k in matrix:
                        for l in k:
                            print(l,end = ",")
                        print("\n")
                    mat = matrix
                    matrix_list.append(mat)
                    down(matrix,row,column)
                if column!=2:
                    right(matrix,row,column)
                    print("After swapping matrix is:")
                    for k in matrix:
                        for l in k:
                            print(l,end = ",")
                        print("\n")
                    mat = matrix
                    
                    matrix_list.append(mat)
                    for m in matrix_list:
                        print(m)
                    right(matrix,row,column)
            column = column + 1
        row = row + 1
        
    '''for matrice in matrix_list:
        if matrice != goal_matrix:
            zero_indicator(matrice)
        else:
            print("Goal State Reached")'''

zero_indicator(start_matrix)