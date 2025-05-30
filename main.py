# a python file for my externship

def main():
    print("select your choice fro the following options: ")
    print("1: Factorial")
    print("2: Fionacci")
    print("3: fun shape")
    print("4: exit")
    selection = int(input("what is your choice: "))
    if selection == 1:
        i = input("enter a number to find it's factorial: ")
        print("the factorial of " + str(i) + " is " + str(factorial(int(i))))
    
    elif selection == 2:
        i = input("enter a number to find it's fibonacci: ")
        print("the fibonacci of " + str(i) + " is " + str(fibonacci(int(i))))
    elif selection == 3:
        print("heres a fun triangle")
        print_recursive(20, 0)
    else:
        print("exiting! have a nice day")
    



# find the factorial of a given number recusively
def factorial(n: int):
    if n == 1:
        return 1        # base case: n == 1
    else:
        return n * factorial(n - 1)     # recursive case: n > 1

# fibonacci function
def fibonacci(n: int):
    if n == 0:
        return 0        # base case
    elif n == 1:
        return 1        # base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)    # recusive case
    


# print a recursive triangle
def print_recursive(n, width):
    if n != 0:
        print_recursive(n - 1, width + 1)           # print a recursive triangle
        s = ""
        val = ""
        for i in range(0,int(width / 2)):
            s += " "    
        for i in range(0, n):
            val += "*"
        print(s + val)                              # print the current level



# driver code
main()