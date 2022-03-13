#!/usr/bin/env python
# coding: utf-8

# ### Ball Brick Zoho Assignment-1

# 
# * Ball brick is a game where there will be a ball at the ground level and with that ball you have
# to destroy all the bricks above it. 
# * For each hit the bricks will come closer to ground level.
# * When the ball touches the ground then you lose GAME OVER..!!
# * If you destroy all the bricks before the bricks touches the ground then you win HURRAY..!!
# 

# Instructions :
# * Consider the game in a NxN Matrix.The first ball starts from the middle of the bottom most row of the matrix.The ball can traverse in three directions. 
# * Straight(ST), Left Diagonal(LD) and Right Diagonal(RD). 
# * The user has to enter the direction in which the ball has to traverse.
# * After getting the input from the user the ball will traverse in that direction and hit the brick/wall on its way. 
# * The bricks can be arranged in any manner and the bricks strength will be denoted by a number.

# The below code represents the working of ball brick * Question1

# In[1]:


print("**********************************************")
print("Question 1")
print("**********************************************")
print("")
print("Enter size of the NxN matrix:")
n=int(input())
l=[]
c="Y"
while c=="Y":
    print("Enter the brick's position and the brick type:")
    l.append(list(map(int,input().split())))
    print("Do you want to continue(Y or N)?")
    c=input()
print("Enter ball Count")
ball=int(input())
matrix=[]
index=0

def display(matrix,n,ball):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                print(end=" ")
            else:
                print(matrix[i][j], end="")
            print(end=" ")
        print("")
    print("Ball count is", ball)

for i in range(n):
    row=[]
    for j in range(n):
        checker=True
        if i==0 or j==0 or j==(n-1):
            row.append("W")
            checker=False
        elif i==(n-1) and (j!=0 or j!=(n-1)) and j!=(n-1)//2:
            row.append("G")
            checker = False
        elif i==(n-1) and j==(n-1)//2:
            row.append("o")
            b=j
            checker = False
        for k in l:
            if i==k[0] and j==k[1]:
                row.append(l[index][2])
                index+=1
                checker = False
                break
        if checker:
            row.append(0)
    matrix.append(row)

display(matrix, n, ball)


# Question 2
# 

# In[3]:


print("**********************************************")
print("Question 2")
print("**********************************************")
print("")
print("Enter size of the NxN matrix:")
n=int(input())
l=[]
c="Y"
while c=="Y":
    print("Enter the brick's position and the brick type:")
    l.append(list(map(int,input().split())))
    print("Do you want to continue(Y or N)?")
    c=input()
print("Enter ball Count")
ball=int(input())
matrix=[]
index=0

def display(matrix,n,ball):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                print(end=" ")
            else:
                print(matrix[i][j], end="")
            print(end=" ")
        print("")
    print("Ball count is", ball)

for i in range(n):
    row=[]
    for j in range(n):
        checker=True
        if i==0 or j==0 or j==(n-1):
            row.append("W")
            checker=False
        elif i==(n-1) and (j!=0 or j!=(n-1)) and j!=(n-1)//2:
            row.append("G")
            checker = False
        elif i==(n-1) and j==(n-1)//2:
            row.append("o")
            b=j
            checker = False
        for k in l:
            if i==k[0] and j==k[1]:
                row.append(l[index][2])
                index+=1
                checker = False
                break
        if checker:
            row.append(0)
    matrix.append(row)

display(matrix, n, ball)


# Question 3

# In[1]:


print("**********************************************")
print("Question 3")
print("**********************************************")
print("")
print("Enter size of the NxN matrix:")
n=int(input())
l=[]
c="Y"
while c=="Y":
    print("Enter the brick's position and the brick type:")
    l.append(list(map(int,input().split())))
    print("Do you want to continue(Y or N)?")
    c=input()
print("Enter ball Count")
ball=int(input())
matrix=[]
index=0

def display(matrix,n,ball):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                print(end=" ")
            else:
                print(matrix[i][j], end="")
            print(end=" ")
        print("")
    print("Ball count is", ball)

for i in range(n):
    row=[]
    for j in range(n):
        checker=True
        if i==0 or j==0 or j==(n-1):
            row.append("W")
            checker=False
        elif i==(n-1) and (j!=0 or j!=(n-1)) and j!=(n-1)//2:
            row.append("G")
            checker = False
        elif i==(n-1) and j==(n-1)//2:
            row.append("o")
            b=j
            checker = False
        for k in l:
            if i==k[0] and j==k[1]:
                row.append(l[index][2])
                index+=1
                checker = False
                break
        if checker:
            row.append(0)
    matrix.append(row)

display(matrix, n, ball)


# Question 4

# In[2]:


print("**********************************************")
print("Question 4")
print("**********************************************")
print("")
print("Enter size of the NxN matrix:")
n=int(input())
l=[]
c="Y"
while c=="Y":
    print("Enter the brick's position and the brick type:")
    l.append(list(map(str,input().split())))
    print("Do you want to continue(Y or N)?")
    c=input()
print("Enter ball Count")
ball=int(input())
matrix=[]
index=0

def display(matrix,n,ball):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "0":
                print(end=" ")
            else:
                print(matrix[i][j], end="")
            if matrix[i][j]=="DE" or matrix[i][j]=="DS":
                print(end=" ")
            else:
                print(end="  ")
        print("")
    print("Ball count is", ball)

for i in range(n):
    row=[]
    for j in range(n):
        checker=True
        if i==0 or j==0 or j==(n-1):
            row.append("W")
            checker=False
        elif i==(n-1) and (j!=0 or j!=(n-1)) and j!=(n-1)//2:
            row.append("G")
            checker = False
        elif i==(n-1) and j==(n-1)//2:
            row.append("o")
            b=j
            checker = False
        for k in l:
            if i==int(k[0]) and j==int(k[1]):
                row.append(l[index][2])
                index+=1
                checker = False
                break
        if checker:
            row.append("0")
    matrix.append(row)

display(matrix, n, ball)


double_check=True
while ball>0:
    ch = True
    print("Enter the direction in which the ball needs to travese:")
    dir = input()
    if dir=="ST":
        n_1=n-2
        while n_1>=0:
            if matrix[n_1][b]=="W":
                display(matrix,n,ball)
                break
            if ord(matrix[n_1][b][0]) in range(49,58) :
                matrix[n_1][b]=str(int(matrix[n_1][b])-1)
                display(matrix,n,ball)
                break
            elif matrix[n_1][b]=="DE":
                for bricks in range(1,n-1):
                    matrix[n_1][bricks]="0"
                display(matrix, n, ball)
                break
            elif matrix[n_1][b]=="DS":
                if ord(matrix[n_1-1][b-1][0]) in range(49,58):
                    matrix[n_1 - 1][b - 1]="0"
                    matrix[n_1 - 1][b] = "0"
                    matrix[n_1 - 1][b+1] = "0"
                if ord(matrix[n_1+1][b-1][0]) in range(49,58):
                    matrix[n_1 + 1][b - 1] = "0"
                    matrix[n_1 + 1][b] = "0"
                    matrix[n_1 + 1][b + 1] = "0"
                matrix[n_1][b - 1] = "0"
                matrix[n_1][b] = "0"
                matrix[n_1][b + 1] = "0"
                display(matrix, n, ball)
                break
            n_1-=1
    elif dir=="LD":
        if matrix[n-1][b-1]=="W":
            che=True
            for e in range(1,n-1):
                if ord(matrix[n-2][e][0]) in range(49,58):
                    matrix[n - 2][e] =str(int(matrix[n - 2][e])-1)
                    matrix[n-1][e]="o"
                    matrix[n-1][b]="G"
                    che = False
                    if e!=b:
                        ball-=1
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b]=="DE":
                    for bricks in range(1,n-1):
                        matrix[n_1][bricks]="0"
                    matrix[n - 1][e] = "o"
                    matrix[n - 1][b] = "G"
                    che = False
                    if e != b:
                        ball -= 1
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DS":
                    if ord(matrix[n_1 - 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 - 1][b - 1] = "0"
                        matrix[n_1 - 1][b] = "0"
                        matrix[n_1 - 1][b + 1] = "0"
                    if ord(matrix[n_1 + 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 + 1][b - 1] = "0"
                        matrix[n_1 + 1][b] = "0"
                        matrix[n_1 + 1][b + 1] = "0"
                    matrix[n_1][b - 1] = "0"
                    matrix[n_1][b] = "0"
                    matrix[n_1][b + 1] = "0"
                    matrix[n - 1][e] = "o"
                    matrix[n - 1][b] = "G"
                    che = False
                    if e != b:
                        ball -= 1
                    display(matrix, n, ball)
                    break

            if che:
                b-=1
                matrix[n - 1][b]="G"
                matrix[n-1][(n-1)//2]="o"
                b=(n-1)//2
                display(matrix, n, ball)
        else:
            matrix[n-1][b-1]="o"
            matrix[n-1][b]="G"
            ball-=1
            b=b-1
            n_1 = n - 2
            while n_1 >= 0:
                if ord(matrix[n_1][b][0]) in range(49,58):
                    matrix[n_1][b] = str(int(matrix[n_1][b])-1)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DE":
                    for bricks in range(1, n - 1):
                        matrix[n_1][bricks] = "0"
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DS":
                    if ord(matrix[n_1 - 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 - 1][b - 1] = "0"
                        matrix[n_1 - 1][b] = "0"
                        matrix[n_1 - 1][b + 1] = "0"
                    if ord(matrix[n_1 + 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 + 1][b - 1] = "0"
                        matrix[n_1 + 1][b] = "0"
                        matrix[n_1 + 1][b + 1] = "0"
                    matrix[n_1][b - 1] = "0"
                    matrix[n_1][b] = "0"
                    matrix[n_1][b + 1] = "0"
                    display(matrix, n, ball)
                    break
                if matrix[n_1][b] == "W":
                    display(matrix, n, ball)
                    break
                n_1-=1
    elif dir=="RD":
        if matrix[n-1][b+1]=="W":
            checking=True
            for e in range(n-1,0,-1):
                if ord(matrix[n-2][e][0]) in range(49,58):
                    matrix[n - 2][e] =str(int(matrix[n - 2][e])-1)
                    matrix[n-1][e]="o"
                    matrix[n-1][b]="G"
                    checking=False
                    if e!=b:
                        ball-=1
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DE":
                    for bricks in range(1, n - 1):
                        matrix[n_1][bricks] = "0"
                    matrix[n - 1][e] = "o"
                    matrix[n - 1][b] = "G"
                    che = False
                    if e != b:
                        ball -= 1
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DS":
                    if ord(matrix[n_1 - 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 - 1][b - 1] = "0"
                        matrix[n_1 - 1][b] = "0"
                        matrix[n_1 - 1][b + 1] = "0"
                    if ord(matrix[n_1 + 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 + 1][b - 1] = "0"
                        matrix[n_1 + 1][b] = "0"
                        matrix[n_1 + 1][b + 1] = "0"
                    matrix[n_1][b - 1] = "0"
                    matrix[n_1][b] = "0"
                    matrix[n_1][b + 1] = "0"
                    matrix[n - 1][e] = "o"
                    matrix[n - 1][b] = "G"
                    che = False
                    if e != b:
                        ball -= 1
                    display(matrix, n, ball)
                    break
            if checking:
                b-=1
                matrix[n - 1][b]="G"
                matrix[n-1][(n-1)//2]="o"
                b=(n-1)//2
                display(matrix, n, ball)
        else:
            matrix[n-1][b+1]="o"
            matrix[n-1][b]="G"
            ball-=1
            b=b+1
            n_1 = n - 2
            while n_1 >= 0:
                if ord(matrix[n_1][b][0]) in range(49, 58):
                    matrix[n_1][b] = str(int(matrix[n_1][b]) - 1)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DE":
                    for bricks in range(1, n - 1):
                        matrix[n_1][bricks] = "0"
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DS":
                    if ord(matrix[n_1 - 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 - 1][b - 1] = "0"
                        matrix[n_1 - 1][b] = "0"
                        matrix[n_1 - 1][b + 1] = "0"
                    if ord(matrix[n_1 + 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 + 1][b - 1] = "0"
                        matrix[n_1 + 1][b] = "0"
                        matrix[n_1 + 1][b + 1] = "0"
                    matrix[n_1][b - 1] = "0"
                    matrix[n_1][b] = "0"
                    matrix[n_1][b + 1] = "0"
                    display(matrix, n, ball)
                    break
                if matrix[n_1][b] == "W":
                    display(matrix, n, ball)
                    break
                n_1-=1
    for iter in matrix:
        if "1" in iter:
            ch=False
            break
    if ch:
        double_check=False
        print("You Win Hurray")
        break
check=True
for iter in matrix:
    if "1" in iter and ball==0:
        print("game over")
        check=False
        break
if check  and double_check:
    print("You Win Hurray")


# Question 5

# In[4]:


print("**********************************************")
print("Question 5")
print("**********************************************")
print("")
print("Enter size of the NxN matrix:")
n=int(input())
l=[]
c="Y"
while c=="Y":
    print("Enter the brick's position and the brick type:")
    l.append(list(map(str,input().split())))
    print("Do you want to continue(Y or N)?")
    c=input()
print("Enter ball Count")
ball=int(input())
matrix=[]
index=0

def display(matrix,n,ball):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "0":
                print(end=" ")
            else:
                print(matrix[i][j], end="")
            if matrix[i][j]=="DE" or matrix[i][j]=="DS":
                print(end=" ")
            else:
                print(end="  ")
        print("")
    print("Ball count is", ball)

for i in range(n):
    row=[]
    for j in range(n):
        checker=True
        if i==0 or j==0 or j==(n-1):
            row.append("W")
            checker=False
        elif i==(n-1) and (j!=0 or j!=(n-1)) and j!=(n-1)//2:
            row.append("G")
            checker = False
        elif i==(n-1) and j==(n-1)//2:
            row.append("o")
            b=j
            checker = False
        for k in l:
            if i==int(k[0]) and j==int(k[1]):
                row.append(l[index][2])
                index+=1
                checker = False
                break
        if checker:
            row.append("0")
    matrix.append(row)

display(matrix, n, ball)

base=0
power=[]
double_check=True
while ball>0:
    ch = True
    print("Enter the direction in which the ball needs to travese:")
    dir = input()
    if dir=="ST":
        n_1=n-2
        while n_1>=0:
            if matrix[n_1][b]=="W":
                display(matrix,n,ball)
                break
            if ord(matrix[n_1][b][0]) in range(49,58) :
                matrix[n_1][b]=str(int(matrix[n_1][b])-1)
                display(matrix,n,ball)
                break
            elif matrix[n_1][b]=="DE":
                for bricks in range(1,n-1):
                    matrix[n_1][bricks]="0"
                display(matrix, n, ball)
                break
            elif matrix[n_1][b]=="DS":
                if ord(matrix[n_1-1][b-1][0]) in range(49,58):
                    matrix[n_1 - 1][b - 1]="0"
                    matrix[n_1 - 1][b] = "0"
                    matrix[n_1 - 1][b+1] = "0"
                if ord(matrix[n_1+1][b-1][0]) in range(49,58):
                    matrix[n_1 + 1][b - 1] = "0"
                    matrix[n_1 + 1][b] = "0"
                    matrix[n_1 + 1][b + 1] = "0"
                matrix[n_1][b - 1] = "0"
                matrix[n_1][b] = "0"
                matrix[n_1][b + 1] = "0"
                display(matrix, n, ball)
                break
            elif matrix[n_1][b]=="B":
                matrix[n_1][b] ="0"
                if  base%2==0 and matrix[n-1][b+1]!="W":
                    matrix[n-1][b+1]="_"
                    power.append(b+1)
                    base+=1
                    display(matrix, n, ball)
                elif base%2!=0 and matrix[n-1][b-1]!="W":
                    matrix[n - 1][b - 1] = "_"
                    power.append(b - 1)
                    base += 1
                    display(matrix, n, ball)
                break
            n_1-=1
    elif dir=="LD":
        if matrix[n-1][b-1]=="W":
            che=True
            for e in range(1,n-1):
                if ord(matrix[n-2][e][0]) in range(49,58):
                    matrix[n - 2][e] =str(int(matrix[n - 2][e])-1)
                    matrix[n-1][e]="o"
                    matrix[n-1][b]="G"
                    che = False
                    if e!=b and e not in power :
                        ball-=1
                    if e in power:
                        power.remove(e)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b]=="DE":
                    for bricks in range(1,n-1):
                        matrix[n_1][bricks]="0"
                    matrix[n - 1][e] = "o"
                    matrix[n - 1][b] = "G"
                    che = False
                    if e != b and e not in power:
                        ball -= 1
                    if e in power:
                        power.remove(e)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DS":
                    if ord(matrix[n_1 - 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 - 1][b - 1] = "0"
                        matrix[n_1 - 1][b] = "0"
                        matrix[n_1 - 1][b + 1] = "0"
                    if ord(matrix[n_1 + 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 + 1][b - 1] = "0"
                        matrix[n_1 + 1][b] = "0"
                        matrix[n_1 + 1][b + 1] = "0"
                    matrix[n_1][b - 1] = "0"
                    matrix[n_1][b] = "0"
                    matrix[n_1][b + 1] = "0"
                    matrix[n - 1][e] = "o"
                    matrix[n - 1][b] = "G"
                    che = False
                    if e != b and e not in power:
                        ball -= 1
                    if e in power:
                        power.remove(e)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "B":
                    matrix[n_1][b] == "0"
                    matrix[n - 1][e] = "o"
                    matrix[n - 1][b] = "G"
                    if base % 2 == 0 and matrix[n - 1][e + 1] != "W":
                        matrix[n - 1][e + 1] = "_"
                        power.append(e + 1)
                        base += 1
                        display(matrix, n, ball)
                    elif base % 2 != 0 and matrix[n - 1][e - 1] != "W":
                        matrix[n - 1][e - 1] = "_"
                        power.append(e - 1)
                        base += 1
                        display(matrix, n, ball)
                    break

            if che:
                if (n-1)//2 not in power:
                    b-=1
                if (n-1)//2 in power:
                    power.remove((n-1)//2)
                matrix[n - 1][b]="G"
                matrix[n-1][(n-1)//2]="o"
                b=(n-1)//2
                display(matrix, n, ball)
        else:
            matrix[n-1][b-1]="o"
            matrix[n-1][b]="G"
            if b-1 not in power:
                ball -= 1
            if b-1 in power:
                power.remove(b-1)

            b=b-1
            n_1 = n - 2
            while n_1 >= 0:
                if ord(matrix[n_1][b][0]) in range(49,58):
                    matrix[n_1][b] = str(int(matrix[n_1][b])-1)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DE":
                    for bricks in range(1, n - 1):
                        matrix[n_1][bricks] = "0"
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DS":
                    if ord(matrix[n_1 - 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 - 1][b - 1] = "0"
                        matrix[n_1 - 1][b] = "0"
                        matrix[n_1 - 1][b + 1] = "0"
                    if ord(matrix[n_1 + 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 + 1][b - 1] = "0"
                        matrix[n_1 + 1][b] = "0"
                        matrix[n_1 + 1][b + 1] = "0"
                    matrix[n_1][b - 1] = "0"
                    matrix[n_1][b] = "0"
                    matrix[n_1][b + 1] = "0"
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "B":
                    matrix[n_1][b]="0"
                    if base % 2 == 0 and matrix[n - 1][b+1] != "W":
                        matrix[n - 1][b+1] = "_"
                        power.append(b+1)
                        base += 1
                        display(matrix, n, ball)
                    elif base % 2 != 0 and matrix[n - 1][b - 1] != "W":
                        matrix[n - 1][b - 1] = "_"
                        power.append(b - 1)
                        base += 1
                        display(matrix, n, ball)
                if matrix[n_1][b] == "W":
                    display(matrix, n, ball)
                    break
                n_1-=1
    elif dir=="RD":
        if matrix[n-1][b+1]=="W":
            checking=True
            for e in range(n-1,0,-1):
                if ord(matrix[n-2][e][0]) in range(49,58):
                    matrix[n - 2][e] =str(int(matrix[n - 2][e])-1)
                    matrix[n-1][e]="o"
                    matrix[n-1][b]="G"
                    checking=False
                    if e!=b and e not in power:
                        ball-=1
                    if e in power:
                        power.remove(e)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DE":
                    for bricks in range(1, n - 1):
                        matrix[n_1][bricks] = "0"
                    che = False
                    if e != b and e not in power:
                        ball -= 1
                    if e in power:
                        power.remove(e)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DS":
                    if ord(matrix[n_1 - 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 - 1][b - 1] = "0"
                        matrix[n_1 - 1][b] = "0"
                        matrix[n_1 - 1][b + 1] = "0"
                    if ord(matrix[n_1 + 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 + 1][b - 1] = "0"
                        matrix[n_1 + 1][b] = "0"
                        matrix[n_1 + 1][b + 1] = "0"
                    matrix[n_1][b - 1] = "0"
                    matrix[n_1][b] = "0"
                    matrix[n_1][b + 1] = "0"
                    che = False
                    if e != b:
                        ball -= 1
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "B":
                    matrix[n_1][b] == "0"
                    matrix[n - 1][e] = "o"
                    matrix[n - 1][b] = "G"
                    if base % 2 == 0 and matrix[n - 1][e + 1] != "W":
                        matrix[n - 1][e + 1] = "_"
                        power.append(e + 1)
                        base += 1
                        display(matrix, n, ball)
                    elif base % 2 != 0 and matrix[n - 1][e + 1] != "W":
                        matrix[n - 1][e - 1] = "_"
                        power.append(e + 1)
                        base += 1
                        display(matrix, n, ball)
            if checking:
                if (n - 1) // 2 not in power:
                    b -= 1
                if (n - 1) // 2 in power:
                    power.remove((n - 1) // 2)
                matrix[n - 1][b] = "G"
                matrix[n - 1][(n - 1) // 2] = "o"
                b = (n - 1) // 2
                display(matrix, n, ball)
        else:
            matrix[n-1][b+1]="o"
            matrix[n-1][b]="G"
            if b + 1 not in power:
                ball -= 1
            if b + 1 in power:
                power.remove(b + 1)
            b=b+1
            n_1 = n - 2
            while n_1 >= 0:
                if ord(matrix[n_1][b][0]) in range(49, 58):
                    matrix[n_1][b] = str(int(matrix[n_1][b]) - 1)
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DE":
                    for bricks in range(1, n - 1):
                        matrix[n_1][bricks] = "0"
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "DS":
                    if ord(matrix[n_1 - 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 - 1][b - 1] = "0"
                        matrix[n_1 - 1][b] = "0"
                        matrix[n_1 - 1][b + 1] = "0"
                    if ord(matrix[n_1 + 1][b - 1][0]) in range(49, 58):
                        matrix[n_1 + 1][b - 1] = "0"
                        matrix[n_1 + 1][b] = "0"
                        matrix[n_1 + 1][b + 1] = "0"
                    matrix[n_1][b - 1] = "0"
                    matrix[n_1][b] = "0"
                    matrix[n_1][b + 1] = "0"
                    display(matrix, n, ball)
                    break
                elif matrix[n_1][b] == "B":
                    matrix[n_1][b]="0"
                    if base % 2 == 0 and matrix[n - 1][b+1] != "W":
                        matrix[n - 1][b+1] = "_"
                        power.append(b+1)
                        base += 1
                        display(matrix, n, ball)
                    elif base % 2 != 0 and matrix[n - 1][b - 1] != "W":
                        matrix[n - 1][b - 1] = "_"
                        power.append(b - 1)
                        base += 1
                        display(matrix, n, ball)
                if matrix[n_1][b] == "W":
                    display(matrix, n, ball)
                    break
                n_1-=1
    for iter in matrix:
        if "1" in iter:
            ch=False
            break
    if ch:
        double_check=False
        print("You Win Hurray")
        break
check=True
for iter in matrix:
    if "1" in iter and ball==0:
        print("game over")
        check=False
        break
if check  and double_check:
    print("You Win Hurray")


# In[ ]:




