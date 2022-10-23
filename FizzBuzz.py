#for number in range 1 to 20:
#    if number divide by 3 and 5 have remainder 0
#        Display "FizzBuzz"
#    elif number divide by 3 have remainder 0
#        Display "Fizz"
#    elif number divide by 5 have remainder 0
#        Display "Buzz"
#    else:
#         Display "number"





for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)