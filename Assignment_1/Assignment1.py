#Create lower triangular, upper triangular and pyramid containing the "*" character.

def lower_triangular(n):
    print("Lower Tiangular Pattern : \n")
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()

def upper_triangular(n):
    print("Upeer Triangular Pattern : \n")
    for i in range(n):
        for j in range(n):
            if j<i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()

def pyramid_pattern(n):
    print("Pyramid Pattern : \n")
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()

n = int(input("Enter the number of Rows : "))
lower_triangular(n)
upper_triangular(n)
pyramid_pattern(n)