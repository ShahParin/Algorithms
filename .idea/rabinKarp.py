# Name: Parin Shah
# Roll No: E029
# Experiment No.10 - Rabin Karp's Algorithm

from string import ascii_lowercase

s = input("Enter the string: ")
p = input("Enter the pattern: ")

s = list(s.lower())
p = list(p.lower())

# s = list(s)
# p = list(p)

a = {}
b = 1

for i in ascii_lowercase:
    a[i] = b
    b += 1

c = int(input('Prime Number: '))
h1 = 0
h2 = 0

for i in range(len(p)):
    h1 += a[s[i]]*(c**i)
    h2 += a[p[i]]*(c**i)

h = []
s1 = []
temp = ''
ip = 0
x = ''
j = 0
for i in s:
    if(ip < len(p)):
        x += i
        j += 1
h.append(h1)
s1.append(x)

if(h1 == h2):
    print('Subset is Present!')

else:
    while(len(s) > len(p)):
        X = h1 - a[s[0]]
        X = X // c
        h1 = X + a[s[len(p)]]*(c**(len(p)-1))

        h.append(h1)
        y = s1[i - 1]
        y = y[1:]
        y += s[len(p)]
        s1.append(y)

        if(h1 == h2):
            print('Subset is Present at ', i)
            break

        else:
            del(s[0])
            i += 1

    if(len(s) <= len(p)):
        print('Subset is not Present!')

# for i in range(len(s)):