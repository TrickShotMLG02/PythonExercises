def search_destroy(numbers, multiplier=2):
    # for each number in numbers, print number * multiplier
    # if you encounter a 0, abort and print "Encountered Zero Value"
    # if the loop is finished without an encounter, print "Survived Loop without seeing 0's"

    tmp = ""

    for number in numbers:
        if number == 0:
            print(tmp + "Encountered Zero Value")
            break
        else:
            tmp += str(number * multiplier) + "\n"
    else:
        print(tmp + "Survived Loop without seeing 0's")

    pass