t = int(input())
for testcase in range(t):
	n, m = map(int, input().split())
	ans = "NO"
	for tile in range(n):
		a = input().split()
		b = input().split()
		if a[1]==b[0]:
			ans = "YES"
	if m%2 != 0:
		ans = 'NO'

	print(ans)

	
'''
B. Symmetric Matrix
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Masha has n
types of tiles of size 2×2

. Each cell of the tile contains one integer. Masha has an infinite number of tiles of each type.

Masha decides to construct the square of size m×m

consisting of the given tiles. This square also has to be a symmetric with respect to the main diagonal matrix, and each cell of this square has to be covered with exactly one tile cell, and also sides of tiles should be parallel to the sides of the square. All placed tiles cannot intersect with each other. Also, each tile should lie inside the square. See the picture in Notes section for better understanding.

Symmetric with respect to the main diagonal matrix is such a square s
that for each pair (i,j) the condition s[i][j]=s[j][i] holds. I.e. it is true that the element written in the i-row and j-th column equals to the element written in the j-th row and i

-th column.

Your task is to determine if Masha can construct a square of size m×m

which is a symmetric matrix and consists of tiles she has. Masha can use any number of tiles of each type she has to construct the square. Note that she can not rotate tiles, she can only place them in the orientation they have in the input.

You have to answer t

independent test cases.
Input

The first line of the input contains one integer t
(1≤t≤100) — the number of test cases. Then t

test cases follow.

The first line of the test case contains two integers n
and m (1≤n≤100, 1≤m≤100

) — the number of types of tiles and the size of the square Masha wants to construct.

The next 2n

lines of the test case contain descriptions of tiles types. Types of tiles are written one after another, each type is written on two lines.

The first line of the description contains two positive (greater than zero) integers not exceeding 100
— the number written in the top left corner of the tile and the number written in the top right corner of the tile of the current type. The second line of the description contains two positive (greater than zero) integers not exceeding 100

— the number written in the bottom left corner of the tile and the number written in the bottom right corner of the tile of the current type.

It is forbidden to rotate tiles, it is only allowed to place them in the orientation they have in the input.
Output

For each test case print the answer: "YES" (without quotes) if Masha can construct the square of size m×m

which is a symmetric matrix. Otherwise, print "NO" (withtout quotes).
Example
Input
Copy

6
3 4
1 2
5 6
5 7
7 4
8 9
9 8
2 5
1 1
1 1
2 2
2 2
1 100
10 10
10 10
1 2
4 5
8 4
2 2
1 1
1 1
1 2
3 4
1 2
1 1
1 1

Output
Copy

YES
NO
YES
NO
YES
YES

Note

The first test case of the input has three types of tiles, they are shown on the picture below.
https://espresso.codeforces.com/521648cb320937492fbb7fedba40922e296ec498.png
Masha can construct, for example, the following square of size 4×4 which is a symmetric matrix:
https://espresso.codeforces.com/cfc50e2c1169502ac7bad6d4797c9a949f8073b2.png
'''