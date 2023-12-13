def max_do(tankha):
    max_no = tankha[0]
    for i in range(0,8):
        for j in (tankha[i], tankha[i+1]):
            # print(j)
            if j < tankha[i]:
                max_no = i
    print(max_no)

salary = [20, 15, 25, 50, 75, 27, -22]
max_do(salary)