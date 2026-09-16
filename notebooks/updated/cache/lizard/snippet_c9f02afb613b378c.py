def prompt_4_yes_no(question):
    while True:
        sys.stdout.write(question + ' (y/n)? ')
        try:
            choice = raw_input().lower()
        except:
            choice = input().lower()
        if choice == 'yes' or choice == 'y':
            return True
        elif choice == 'no' or choice == 'n':
            return False
        else:
            printError(
                "'%s' is not a valid answer. Enter 'yes'(y) or 'no'(n)." %
                choice)