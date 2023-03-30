'''

You are given a string .
contains alphanumeric characters only.
Your task is to sort the string
in the following manner:
    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.
Input Format
A single line of input contains the string
.
Constraints
Output Format
Output the sorted string
.
Sample Input
Sorting1234
Sample Output
ginortS1324

'''

# Answer

# Enter your code here. Read input from STDIN. Print output to STDOUT

Answer = sorted(input())

lower = ''
upper = ''
odd = ''
even = ''
for i in Answer:
    if i.islower():
        lower = lower+i
    if i.isupper():
        upper = upper + i
    if i.isdigit() and int(i) % 2 == 1:
        odd = odd + i
    if i.isdigit() and int(i) % 2 == 0:
        even = even + i

print(lower+upper+odd+even)
