f = open("input.txt", "r")

input_list = f.readline().split(",")
input_list = list(map(int, input_list))

def compute(input_list, noun, verb):
    i = 0
    
    input_list[1] = noun
    input_list[2] = verb

    while(True):
        if input_list[i] == 1:
            input_list[input_list[i+3]] = input_list[input_list[i+1]] + input_list[input_list[i+2]]
            i += 4
        elif input_list[i] == 2:
            input_list[input_list[i+3]] = input_list[input_list[i+1]] * input_list[input_list[i+2]]
            i += 4
        elif input_list[i] == 99:
            break
        else:
            break

    return input_list[0]

for i in range(0, 100):
    for j in range(0, 100):
        copy = input_list.copy()
        if compute(copy, i, j) == 19690720:
            print(str(i) + ", " + str(j))

