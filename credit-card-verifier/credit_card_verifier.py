# Takes number and returns TRUE or FALSE based on length
def check_length(user_input):

    if user_input.isdigit() == True:
        if len(user_input) == 15 or 16:
            return(True)
        else:
            return(False)
    else:
        return(False)

# Determines card type based of starting numbers
def determine_card_type(user_input):

    first_digit = user_input[0:1]
    first_two_digits = user_input[0:2]
    first_four_digits = user_input[0:4]

    if first_digit in ["4"]:
        return("Visa")
    elif first_two_digits in ["51", "52", "53", "54"]:
        return("Mastercard")
    elif first_two_digits in ["37"]:
        return("Amex")
    elif first_four_digits in ["6011"]:
        return("Discover")
    else:
        return(False)

# Validates Luhn algorythm and returns TRUE or FALSE
def validate(user_input):
    total = 0
    num_digits = len(user_input)
    oddeven = num_digits & 1

    for number in range(0, num_digits):
        digit = int(user_input[number])

        if not (( number & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        total = total + digit

    return((total % 10) == 0)

# Runs entire program
def run_check():

    user_input = input("Write your credit card number:")

    if check_length(user_input) == True:
        if validate(user_input) == True:
            if not determine_card_type(user_input) == False:
                print("Valid {} card.".format(determine_card_type(user_input)))
            else:
                print("Invalid.")
        else:
            print("Invalid.")
    else:
        print("Invalid.")

run_check()
