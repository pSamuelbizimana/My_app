import json

tests = [] # creating the room or store or list keep our data

def print_main_menu():
    print('\nMain Menu')
    print('1. Perform tests')
    print('2. Create questions')
    print('3. Save questions')
    print('4. Quit')

def perform_tests(): # perfoming a test method
    name = input('Enter your name before you proceed: ').upper()
    print(f"\nWelcome to O'Genius Priority LTD dear, {name}")
    
    while True:
        print('Select an option:')
        print('1. Monday')
        print('2. Tuesday')
        print('3. Wednesday')
        print('4. Thursday')
        print('5. Friday')
        print('n. Next')

        choice = input('Make your choice: ')

        if choice == '1':
            print("It's meeting at 10 AM sharp")
        elif choice == '2':
            print('On Tuesday we have the meeting')
        elif choice == '3':
            print('On Wednesday we have the meeting')
        elif choice == '4':
            print('On Thursday we have the meeting')
        elif choice == '5':
            print('On Friday we have the meeting')
        elif choice == 'n':
            break
        else:
            print('Invalid input. Please try again!!')
# function that will help the user to create questions
def create_question():
    user_input = input('Create your question: ')
    tests.append(user_input)
    print('Created questions:')
    
    for i, test in enumerate(tests, start=1): #  to outline the user input on the termonal
        print(f'{i}. {test}')

def save_tests(filename='tests.json'):
    with open(filename, 'w') as file:
        json.dump(tests, file) # we are storing the file into json formated string

valid_input= '*3400#'
def main():
    print("Session initiated. Enter '*3400#' to begin.")
    user_input = input('ENTER A USSD CODE TO BEGIN: ')

    if user_input == valid_input: # HERE WE HAVE A RECOMENDED USSD CODE, IF NOT OUR TASK CAN NOT BE INITIATED
        while True:  # JUST TO MAKE OUR PROGRAM TO CONTINUE EXCUTING AND INTERACT WITH A USER
            print_main_menu()
            choice = input('Enter your choice: ')

            if choice == '1':
                perform_tests()
            elif choice == '2':
                create_question()
            elif choice == '3':
                save_tests()
            elif choice == '4':
                break
            else:
                print('Invalid input. Please try again!!')

if __name__ == '__main__':     # To make sure if the scripts is being run directly by py interpreter
    main() 