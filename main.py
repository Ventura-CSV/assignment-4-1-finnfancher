def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        if((start.isalpha() and end.isalpha()) and (ord(start) < ord(end))):
            break
        else:
            print("Input Error.")

    """
    ########################################
    Code Your Program here
    ########################################
    """
    

    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
