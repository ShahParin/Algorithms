# Name: Parin Shah
# Roll No: E029
# Experiment No.8 - Matrix Chain Multiplication

class mat:
    def __init__(self):
        self.p = list(map(int, input("Enter the p array: ").split(' ')))
        self.n = len(self.p)-1
        self.x = 0
        self.m = [[0 for x in range(self.n)] for x in range(self.n)]
        self.s = [[0 for x in range(self.n)] for x in range(self.n)]
        self.MatrixChain()
        self.ans()
        self.print_paren(0, self.n-1)

    def MatrixChain(self):
        for i in range(1, self.n):
            self.m[i][i] = 0

        for L in range(2, self.n):
            for i in range(1, self.n-L + 1):
                j = i + L-1
                self.m[i][j] = 10000

                for k in range(i, j):
                    q = self.m[i][k] + self.m[k + 1][j] + self.p[i-1]*self.p[k]*self.p[j]
                    if q < self.m[i][j]:
                        self.m[i][j] = q
                        self.s[i][j] = k
        self.x = self.m[1][self.n-1]

    def ans(self):
        print("M: ")
        self.lprint(self.m)
        print("S: ")
        self.lprint(self.s)
        print("Minimum number of multiplications is ", self.x)

    def lprint(self, x):
        for i in x:
            for j in i:
                print(j, end=' ')
            print()

    def print_paren(self, i, j):
        if(i ==j):
            print('A' + str(i), end =" ")
        else:
            print('(', end =" ")
            self.print_paren(i, self.s[i][j])
            self.print_paren(self.s[i][j]+1, j)
            print(')', end =" ")
mat()