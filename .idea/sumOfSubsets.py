# Name: Parin Shah
# Roll No: E029
# Experiment No.9 - Sum of Subsets Problem

class sos:
    def __init__(self):
        self.n = 0
        self.elements = []
        self.m = 0
        self.solutions = list()

        self.n = int(input('Enter number of elements: '))
        print('Enter the set: ')
        self.elements = list(map(int, input().split(' ')))
        self.m = int(input('Enter sum: '))

        self.mains()

    def mains(self):
        tree = [[0]]

        for i in range(len(self.elements) + 1):
            a = []

            for j in range(len(tree[i])):
                if i != len(self.elements):
                    x = tree[i][j] + self.elements[i]
                    a.append(x)
                    a.append(tree[i][j])

                if tree[i][j] == self.m:
                    p = i
                    q = j
                    w = []

                    while tree[p][q] != 0:
                        if tree[p][q] - tree[p - 1][q // 2] != 0:
                            w.append(tree[p][q] - tree[p - 1][q // 2])
                        p -= 1
                        q = q // 2
                    w.reverse()

                    if w not in self.solutions:
                        self.solutions.append(w)

            if i != len(self.elements):
                tree.append(a)

        c = 1
        for i in tree:
            print('Row', c)

            for j in i:
                print(j, end=' ')

            print()
            c = c + 1

        print("\nSets:")
        for i in self.solutions:
            print(set(i))

obj = sos()

