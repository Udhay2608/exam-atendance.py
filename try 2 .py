try :
    num1=int(input("Enter a number"))
    num2=int(input("Enter a number"))
    result = num1/num2
    print("The result is",result)
    print("The result is", result1)

except ZeroDivisionError:
    print("Division by zero isn't allowed")
except ValueError:
    print("Please enter a numerical number")
except NameError as ex:
    print("The exception is",ex)
except:
    print("Some error occured")
finally:
    print("I will execute no matter what")