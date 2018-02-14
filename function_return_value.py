# This program uses the return value of a function

def main():
    # Get the user's age
    first_age = int(input('Enter your age: '))

    # Get the user's best friend's age
    second_age = int(input("Enter your best friend's age: "))

    # Get the sum of both ages
    total = sum(first_age, second_age)

    # Display the total age
    print('Together you are', total, 'years old.')

# The sum function accepts two numberic arguments
# returns the sum of those arguments
def sum(num1, num2):
    return num1 + num2 

# Call the main function
main()
