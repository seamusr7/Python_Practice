#number count down
n = int(input("enter a number "))
def count_down(n):
    while n > 0:
        print(n)
        n-= 1
count_down(n)