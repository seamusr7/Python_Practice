#negative, positive, or 0 checker
n = int(input("enter a number "))

def check_sign(n):
    if n < 0:
        print("Negative number")
        return
    elif n > 0:
        print("Positive number")
        return
    else:
        print("zero")
        return
check_sign(n)