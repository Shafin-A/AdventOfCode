f = open("input.txt", "r")

input_list = f.readline().split(",")
input_list = list(map(int, input_list))

def get_ABCDE(instruction):
    DE = instruction % 100
    C = instruction // 100 % 10
    B = instruction // 1000 % 10
    A = instruction // 10000 % 10
    return [DE, C, B, A]

def param_mode(input_list, ABCDE, idx):
    param1 = input_list[idx + 1] if ABCDE[1] == 0 else (idx+1)
    param2 = input_list[idx + 2] if ABCDE[2] == 0 else (idx+2)

    return param1, param2

def compute(input_list):
    i = 0

    while(True):
        ABCDE = get_ABCDE(input_list[i])
        op = ABCDE[0]
        param1, param2 = param_mode(input_list, ABCDE, i)

        if op == 1:
            input_list[input_list[i+3]] = input_list[param1] + input_list[param2]
            i += 4
        elif op == 2:
            input_list[input_list[i+3]] = input_list[param1] * input_list[param2]
            i += 4
        elif op == 3:
            input_list[param1] = int(input("Input = "))
            i += 2
        elif op == 4:
            output = input_list[param1]
            print(output)
            i += 2
        elif op == 5:
            if input_list[param1] != 0:
                i = input_list[param2]
            else:
                i += 3
        elif op == 6:
            if input_list[param1] == 0:
                i = input_list[param2]
            else:
                i += 3
        elif op == 7:
            if input_list[param1] < input_list[param2]:
                input_list[input_list[i+3]] = 1
            else:
                input_list[input_list[i+3]] = 0
            i += 4
        elif op == 8:
            if input_list[param1] == input_list[param2]:
                input_list[input_list[i+3]] = 1
            else:
                input_list[input_list[i+3]] = 0
            i += 4            
        elif op == 99:
            print("Halted")
            break
        else:
            print("Unexpected opcode")
            break

    return input_list

compute(input_list)

