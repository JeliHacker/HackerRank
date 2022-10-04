# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT

stdin_input = input().split()


N = int(stdin_input[0])
M = int(stdin_input[1])

n_mid = N // 2
m_mid = (M - 3) // 2

for row in range(n_mid):
    dashes = m_mid - (3 * row)
    row_print = ("-" * dashes) + (".|." * (2 * row) + ".|.") + ("-" * dashes)
    print(row_print)
    
middle_dashes = "-" * ((M - 7) // 2)
print(middle_dashes + "WELCOME" + middle_dashes)

for row in range(n_mid - 1, -1, -1):
    dashes = m_mid - (3 * row)
    row_print = ("-" * dashes) + (".|." * (2 * row) + ".|.") + ("-" * dashes)
    print(row_print)
