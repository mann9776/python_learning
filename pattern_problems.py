n = int(input("Enter a number: "))
for i in range(1,n+1):
    print("*"*i)
# Output
"""
Enter a number: 9
*
**
***
****
*****
******
*******
********
*********
"""

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*" * (n-i+1))
#Output
"""
Enter a number: 5
*****
****
***
**
*
"""

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(" "* (n-i), "*" * (2*i-1))
#Output
"""
Enter a number: 5
     *
    ***
   *****
  *******
 *********
 """

n = int(input("Enter a number: "))
for i in range(1, n+1):
        print(" "*(n-i), "*"*(2*i-1))
for i in range(n-1, 0, -1):
        print(" "*(n-i), "*"*(2*i-1))
#Output
"""
Enter a number: 5
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
"""

n = int(input("Enter a numner: "))
for i in range(n):
    print(" "*(n-i-1) + (chr(65+i)+" ")*(i+1))
#Output
"""
Enter a numner: 5
    A 
   B B 
  C C C 
 D D D D 
E E E E E 
"""

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(" "*(n-i)+(str(i)+" ")*i)
#Output
"""
Enter a number: 5
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 
"""

n = int(input("Enter a numner: "))
for i in range(1, n+1):
    if (i == 1) or (i == n):
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
#Output
"""
Enter a numner: 5
*****
*   *
*   *
*   *
*****
"""

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if (i==0) or (i==n-1) or (j==0) or (j==n-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
#Output
"""
Enter a numner: 5
*****
*   *
*   *
*   *
*****
"""

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(2*n -1):
        if j == n-i-1 or j == (n+i)-1 or i==n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#Output
"""
Enter a number: 5
    *    
   * *   
  *   *  
 *     * 
*********
"""

n = int(input("Enter a number: "))
for i in range(n+1,1, -1):
    print(" "*(n-i+1) +"*"*(2*i-3))
for i in range(n):
    print(" "*(n-i)+"*"*)
#Output
"""
Enter a number: 5
*********
 *******
  *****
   ***
    *
"""
