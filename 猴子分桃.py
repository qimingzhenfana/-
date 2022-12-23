i = 0
while 1:
    i += 1
    temp = i
    for j in range(5):
        if temp % 5 != 1:
            break
        else:
            temp = (temp - 1) / 5 * 4
        if j == 4:
            print(i)
            exit()
