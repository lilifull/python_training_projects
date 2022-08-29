list_f = [0]
num_f = int(input('How many numbers of the fibonacci sequence do you want to see ? : '))

if num_f >= 1:

    for a in range(num_f - 1):
        if a == 0:
            list_f.append(1)
        else:
            list_f.append(sum(list_f[-2:]))

    print(*list_f)

    if len(list_f) == 1:
        print("This is the first number in Fibonacci sequence.")
    else:
        print("These are the {} first numbers in Fibonacci sequence.".format(num_f))

