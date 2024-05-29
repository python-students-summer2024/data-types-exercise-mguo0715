"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """

    sales = int(input('Enter projected amount of total sales'))
    formatted_sales = format(sales * .23, ',.2f')
    print('Profit: $' + formatted_sales)




def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    num_1 = int(input('Enter first number'))
    num_2 = int(input('Enter second number'))
    quotient = num_1 // num_2
    remainder = num_1 % num_2
    print(str(num_2) + ' goes into ' + str(num_1) + ' a total of ' + str(quotient) + ' times with a remainder of ' + str(remainder))


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles = int(input('How many miles driven'))
    gas = int(input('How many gallons of gas used'))
    mpg = miles / gas 
    print('Miles driven: ' + str(miles))
    print('Gas used (gallons): ' + str(gas))
    print('Miles per gallon: ' + str(mpg))



def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60 
    """

    price_1 = int(input('Enter Price #1'))
    price_2 = int(input('Enter Price #2'))
    price_3 = int(input('Enter Price #3'))

    formatted_price_1a = format(price_1, '.2f')
    formatted_price_2a = format(price_2, '.2f')
    formatted_price_3a = format(price_3, '.2f')

    formatted_price_1b = format(formatted_price_1a, '>8s')
    formatted_price_2b = format(formatted_price_2a, '>8s')
    formatted_price_3b = format(formatted_price_3a, '>8s')

    print('Here are your prices!')

    print('Price #1: $' + formatted_price_1b)
    print('Price #2: $' + formatted_price_2b)
    print('Price #3: $' + formatted_price_3b)

                  
