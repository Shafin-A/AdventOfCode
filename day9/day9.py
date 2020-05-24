import itertools

f = open("input.txt", "r")

input_list = f.readline().split(",")
input_list = list(map(int, input_list))

class IntCode:
    def __init__(self, program, input_code=None):
        self.ip = 0
        self.relative_base = 0
        self.program = program.copy() + [0] * len(2*program.copy())
        self.halted = False
        self.input_code = input_code
        self.outputs = []
        
    def get_ABCDE(self, instruction):
        DE = instruction % 100
        C = instruction // 100 % 10
        B = instruction // 1000 % 10
        A = (instruction // 10000) % 10
        return [DE, C, B, A]

    def param_mode(self, ABCDE, idx, op):   
        param1, param2, param3 = None, None, None
        
        if op in (1, 2, 7, 8):
            param1 = self.program[idx + 1] if ABCDE[1] == 0 else (idx+1) if ABCDE[1] == 1 else (self.relative_base+self.program[idx+1])
            param2 = self.program[idx + 2] if ABCDE[2] == 0 else (idx+2) if ABCDE[2] == 1 else (self.relative_base+self.program[idx+2])
            param3 = self.program[idx + 3] if ABCDE[3] == 0 else (idx+3) if ABCDE[3] == 1 else (self.relative_base+self.program[idx+3])
        elif op in (3, 4, 9):
            param1 = self.program[idx + 1] if ABCDE[1] == 0 else (idx+1) if ABCDE[1] == 1 else (self.relative_base+self.program[idx+1])
        elif op in (5, 6):
            param1 = self.program[idx + 1] if ABCDE[1] == 0 else (idx+1) if ABCDE[1] == 1 else (self.relative_base+self.program[idx+1])
            param2 = self.program[idx + 2] if ABCDE[2] == 0 else (idx+2) if ABCDE[2] == 1 else (self.relative_base+self.program[idx+2])

        return param1, param2, param3

    def compute(self):
        output = 0
        
        while(True):
            ABCDE = self.get_ABCDE(self.program[self.ip])
            op = ABCDE[0]
            
            param1, param2, param3 = self.param_mode(ABCDE, self.ip, op)
        
            if op == 1:
                self.program[param3] = self.program[param1] + self.program[param2]
                self.ip += 4
            elif op == 2:
                self.program[param3] = self.program[param1] * self.program[param2]
                self.ip += 4
            elif op == 3:
                if self.input_code is None:
                    self.program[param1] = int(input("Input = "))
                elif len(self.input_code) == 0:
                    break
                else:
                    self.program[param1] = self.input_code[0]
                    self.input_code = self.input_code[1:]
                self.ip += 2
            elif op == 4:
                output = self.program[param1]
                self.outputs.append(output)
                self.ip += 2
            elif op == 5:
                if self.program[param1] != 0:
                    self.ip = self.program[param2]
                else:
                    self.ip += 3
            elif op == 6:
                if self.program[param1] == 0:
                    self.ip = self.program[param2]
                else:
                    self.ip += 3
            elif op == 7:
                if self.program[param1] < self.program[param2]:
                    self.program[param3] = 1
                else:
                    self.program[param3] = 0
                self.ip += 4
            elif op == 8:
                if self.program[param1] == self.program[param2]:
                    self.program[param3] = 1
                else:
                    self.program[param3] = 0
                self.ip += 4
            elif op == 9:
                self.relative_base += self.program[param1]
                self.ip += 2
            elif op == 99:
                self.halted = True
                break
            else:
                print("Unexpected opcode: " + str(op))
                break

        return self.outputs


print(IntCode(input_list, [1]).compute())
print(IntCode(input_list, [2]).compute())

