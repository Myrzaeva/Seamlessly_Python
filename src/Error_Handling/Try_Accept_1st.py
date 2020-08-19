try :
    footbar
except:
    print("Problem!")
print("after the try")



while True:
    try:
        number = int(input("Enter a number"))
    except ValueError:
        print("That is not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("Runs no matter what!")
print("That is it!")


