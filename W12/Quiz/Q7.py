def PrintBoxByWidth(width):
    # Row 1
    for x in range(width):
        print("x", end='')
    print("")
    # Row 2
    for x in range(width):
        if x == 0 or x == (width - 1):
            print("x", end='')
        else:
            print(" ", end='')
    print("")
    # Row 3
    for x in range(width):
        if x == 0 or x == (width - 1):
            print("x", end='')
        else:
            print("o", end='')
    print("")
    # Row 4
    for x in range(width):
        if x == 0 or x == (width - 1):
            print("x", end='')
        else:
            print(" ", end='')
    print("")
    # Row 5
    for x in range(width):
            print("x", end='')


PrintBoxByWidth(60)