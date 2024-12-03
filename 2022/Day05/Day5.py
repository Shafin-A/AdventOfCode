
def get_nums_from_string(string):
    return [int(s) for s in string.split() if s.isdigit()]

def pop_and_push_to_stack(stack_being_popped: list, stack_to_pop_to: list, num_times_to_pop):
    for _ in range(num_times_to_pop):
        stack_to_pop_to.append(stack_being_popped.pop())

def pop_and_push_to_stack_reversed(stack_being_popped: list, stack_to_pop_to: list, num_times_to_pop):
    s = []
    for _ in range(num_times_to_pop):
        s.append(stack_being_popped.pop())
    
    stack_to_pop_to.extend(s[::-1])

def read_input_and_format_data():

    input_data = open("Day5Input.txt", "r").readlines()

    num_lists = int(len(input_data[0]) / 4) # '[' adds 1 , letter adds 1, ']' adds 1, '\n' adds 1 = 4

    col_num = 0 

    for line in input_data:
        
        if line == '\n':
            break
        
        col_num += 1

    stacks = [ [] for _ in range(num_lists) ] # create num_lists empty lists for storing all the stacks

    for i in range(col_num-2, -1 , -1):
        for j in range(1, num_lists*4, 4):
            if (input_data[i][j] != ' '):
                stacks[j // 4].append(input_data[i][j])

    return input_data[col_num+1:], stacks

moves, stacks = read_input_and_format_data()

def do_moves(moves, stacks, move_method):
    for move in moves:
        nums = get_nums_from_string(move)

        num_moving, move_from, move_to = nums

        move_method(stacks[move_from-1], stacks[move_to-1], num_moving)


def p1():
    do_moves(moves, stacks, pop_and_push_to_stack)
    
    for stack in stacks:
        print(stack[-1], end='')

def p2():
    do_moves(moves, stacks, pop_and_push_to_stack_reversed)
    
    for stack in stacks:
        print(stack[-1], end='')

#p1()
#p2()