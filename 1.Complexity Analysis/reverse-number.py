# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N. Display the reverse of the given number N.
t = int(input(""))
for _ in range(t):
    n = (input(""))
    print(int(n[::-1]))