f = open("input.txt", "r")

input_list = f.readline().split(",")
input_list = list(map(int, input_list))

input_list[1] = 12
input_list[2] = 2

i = 0
while(True):
    if input_list[i] == 1:
        input_list[input_list[i+3]] = input_list[input_list[i+1]] + input_list[input_list[i+2]]
        i += 4
    elif input_list[i] == 2:
        input_list[input_list[i+3]] = input_list[input_list[i+1]] * input_list[input_list[i+2]]
        i += 4
    elif input_list[i] == 99:
        print(input_list)
        break
    else:
        print("ERROR!!!!!!")
        break


