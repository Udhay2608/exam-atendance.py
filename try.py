try:
    num=int(input("Enter a number"))
    print(num)
except ValueError as ex:
    print("Exception:",ex)


    print("i am outsiude of the try block")