def a(n):
    if n == 0:
        return

    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num)
    a(n-1)


a(int(input("Enter a number: ")))