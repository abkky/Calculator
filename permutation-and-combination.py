from fractions import *


def factorial(a):
    num = 1
    for i in range(a):
        num = (i + 1) * num
    return num


def permutation(n, r):
    return factorial(n) / factorial(n - r)


def combination(n, r):
    return factorial(n) / (factorial(n - r) * factorial(r))


# def fractionCheck(x):
#     temp=str(x)
#     temp=temp.split('.')
#     if(int(temp[1])!=0):
#         return Fraction(x)
#     else:
#         return x

print("*** Calculate Permutation and Combination ***")
i = 1
while (i != 0):
    print("\n----Choices-----\n1.\t Permutaion\n2.\tCombination\n0.\tExit\n---------------")
    choice = input("Enter Your Choice : ")
    if (choice == '0'):
        print('Exiting..')
        i = 0
        break
    elif (choice == '1' or choice == '2'):
        n = int(input("Enter the value of n: "))
        r = int(input("Enter the value of r: "))
        if (n >= r):
            if (choice == '1'):
                res = permutation(n, r)
            elif (choice == '2'):
                res = combination(n, r)
            print(Fraction(res))
        else:
            print("Math Error")
    else:
        print("Invalid Choice")
