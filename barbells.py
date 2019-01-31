# Writes down all combinations of plates
COMBINATIONS = [1.25, 2.5, 5, 10, 25]

# 1 kg is 2.20... pounds
KILOS_POUNDS_CONVERSION_RATE = 2.20462

# Function that asks for str input
def get_input_in_kilos():
    return input("Enter weight in kilos: ")

# function that converts punds to kilos
def convert_kilos_to_pounds(kilos):
    return kilos * KILOS_POUNDS_CONVERSION_RATE


def break_down_into_combinations(weight, options):
    # An empty list
    combination = []
    # Variable difference is the same as weight
    difference = weight
    # variable which sorts the options in reverse
    sorted_options = sorted(options, reverse=True)

    # variable which is equal to zero
    current_option_index = 0
    # while loop which will keep looping as long as current_option_index is bigger than length of sorted_options
    while current_option_index < len(sorted_options):
        # Variable which says current_option is 0 in the sorted list
        current_option = sorted_options[current_option_index]
        # if current_option is less than or equal the weight
        if current_option <= difference:
            # then remove and apply difference fomr current_option
            difference -= current_option
            # Then append to combination the current option
            combination.append(current_option)
        # Else just take add and apply 1 to current_option_index
        else:
            current_option_index += 1

    return combination


def main():
    kilos = int(get_input_in_kilos())
    pounds = convert_kilos_to_pounds(kilos)
    weights = break_down_into_combinations(pounds, COMBINATIONS)
    print(weights)

main()
