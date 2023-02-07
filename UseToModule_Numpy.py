import numpy as np
import re

A = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [1, 1, 1]
])

B = np.array([
    [3, 3, 3],
    [2, 2, 2],
    [3, 3, 3]
])

C = np.array([
    [5, 5, 5],
    [2, 2, 2],
    [5, 5, 5]
])

# ----------------- solve prat 1 => (A + B + C) -------------

A_add_B = np.add(A, B)
A_add_B_add_C = np.add(A_add_B, C)
print(A_add_B_add_C)

# ----------------- solve prat 2 => A * B==> Transepos(A) x B -------------

A_Tran = np.transpose(A)
lis = []

for i in range(len(B)):
    arr = []
    for j in range(len(A_Tran)):
        x = np.sum([np.multiply(A_Tran[i,], B[i,], )])
        arr.append(x)
    lis.append(arr)

A_prod_B = np.array(lis)
print(A_prod_B)

# ----------------- solve prat 3 => A mulit C (a11*c11, a12*c12....) -------------

A_multi_C = np.multiply(A, C)
print(A_multi_C)

# ----------------- solve prat 4 => A + 3-------------

# A_add_3 = np.sum(A, 3)
# print(A_add_3)

# چون عدد سه یک عدد است ماتریس نیست زمانیکه می خواهیم با ماتریس ضرب کنیم خطای
# AxisError: axis 3 is out of bounds for array of dimension 2
# یعنی بعد عدد سه با بعد ماتریس مساوی نیست

# ----------------- solve prat 5 => Matrix_Hamani multi B => (m11*b11, m12*b12,.....) -------------

Mat_Hamani = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])

B_Multi_Mat_Hamani = np.multiply(B, Mat_Hamani)
print(B_Multi_Mat_Hamani)

# ----------------- solve prat 6 => F * C => Transipos(F) x C -------------
# why Transipos(F)? becuse for multiply tow matrix we need to column and row. Row Transipos F = column F, new we can row * row

F = np.array([
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5],
])

F_Tran = np.transpose(F)
lis = []

for i in range(len(C)):
    arr = []
    for j in range(len(F_Tran)):
        x = np.sum([np.multiply(F_Tran[i,], C[i,])])
        arr.append(x)
    lis.append(arr)

F_prod_C = np.array(lis)
print(F_prod_C)

# ---------------- solve prat 7 => conut Transpose A, B, C and Find Multi (A_Trans,B_Trans,C_Trans)

A_Tran = np.transpose(A)
B_Tran = np.transpose(B)
C_Tran = np.transpose(C)

print(A_Tran, "\n")
print(B_Tran, "\n")
print(C_Tran, "\n")

A_Tran_multi_B_Tran = np.multiply(A_Tran, B_Tran)
A_Tran_mulit_B_Tran_multi_C_Tran = np.multiply(A_Tran_multi_B_Tran, C_Tran)

print(A_Tran_mulit_B_Tran_multi_C_Tran)


# ------> solve prat8   ===========>> solution system by cramer's law <==========


def findNumber(x):
    check = "[a-zA-Z' '=+]{1,}"

    str = ""
    lis = ""
    for i in x:
        if re.match(check, i):
            if str == '-':
                pass
            else:
                lis += str + ","
                str = ""
        else:
            str += i
    lis += str
    str = []
    listMe = lis.split(',')
    for x in listMe:
        if x != '':
            str.append(x)
    return str


def changeColumnAndFindDeter(A, B, index):
    temp = np.array(A)
    j = 0
    for i in range(len(B)):
        for ii in range(len(B)):
            if ii == index:
                temp[i][ii] = B[j]
                j += 1
    return np.linalg.det(temp)


n = int(input("enter n: "))
mylist = []
B = []
print("Pleas enter your system this form:  --->>  12a+3b-4c=9  <<---")

for i in range(n):
    x = input()
    y = findNumber(x)
    matrixA = []
    for i in range(len(y)):
        if i == len(y) - 1:
            B.append(float(y[i]))
        else:
            matrixA.append(float(y[i]))
    mylist.append(matrixA)

A = np.array(mylist)
B = np.array(B)
detA = np.linalg.det(A)
for i in range(len(B)):
    detx = round(changeColumnAndFindDeter(A, B, i), 3)
    detA = round(detA, 3)
    print(f"X{i}= ", detx, "/", detA, " =", round(detx / detA, 3))