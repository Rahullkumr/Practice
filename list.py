# DIAMOND urf BARFI

def up_diamond(n):
    for i in range(0,n):
        for k in range(n-i-1,0,-1):
            print(" ",end="")
        for j in range(0,i+1):
            print('*', end=' ')
        print()

def down_diamond(m):
    for i in range(0,m):
        for k in range(i+1):
            print(" ",end="")
        for j in range(4,i,-1):
            print('*', end=' ')
        print()

up_diamond(5)
down_diamond(4)