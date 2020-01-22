# Name: Parin Shah
# Roll No: E029
# Experiment No.7 - Longest Common Substring

x1 = input("Enter String 1: ")
y1 = input("Enter String 2: ")
x = "0" + x1
y = "0" + y1

m = len(x)
n = len(y)
lcs = [[0 for  i in range(n)] for j in range(m)]
trav = [["z" for  i in range(n)] for j in range(m)]
ans = []

for i in range(m):
    lcs[i][0] = 0
for j in range(n):
    lcs[0][j] = 0

for i in range(m):
    for j in range(1,n):
        if x[i] == y[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
            trav[i][j] = "d"
        elif lcs[i-1][j] >= lcs[i][j-1]:
            lcs[i][j] = lcs[i-1][j]
            trav[i][j] = "u"
        else:
            lcs[i][j] = lcs[i][j-1]
            trav[i][j] = "l"
lcs_len = lcs[m-1][n-1]

i = m-1
j = n-1
while(i!=0 and j!=0):
    if(trav[i][j]=="d"):
        ans.append(x[i])
        i-=1
        j-=1
    elif(trav[i][j]=="u"):
        i-=1
    elif(trav[i][j]=="l"):
        j-=1
    else:
        pass

for i in lcs:
    print(i)
for j in trav:
    print(j)
print("Length of LCS: " + str(lcs_len))
print(ans[::-1])
