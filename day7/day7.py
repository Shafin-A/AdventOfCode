import itertools

f = open("input.txt", "r")

input_list = f.readline().split(",")
input_list = list(map(int, input_list))

class IntCode:
    def __init__(self, program, input_code=None):
        self.ip = 0
        self.program = program
        self.halted = False
        self.input_code = input_code
        
    def get_ABCDE(self, instruction):
        DE = instruction % 100
        C = instruction // 100 % 10
        B = instruction // 1000 % 10
        A = instruction // 10000 % 10
        return [DE, C, B, A]

    def param_mode(self, ABCDE, idx):
        param1 = self.program[idx + 1] if ABCDE[1] == 0 else (idx+1)
        param2 = self.program[idx + 2] if ABCDE[2] == 0 else (idx+2)

        return param1, param2

    def compute(self):
        output = 0
        
        while(True):
            ABCDE = self.get_ABCDE(self.program[self.ip])
            op = ABCDE[0]
            
            if (self.ip + 2) > len(self.program):
                self.halted = True
                break
            
            param1, param2 = self.param_mode(ABCDE, self.ip)

            if op == 1:
                self.program[self.program[self.ip + 3]] = self.program[param1] + self.program[param2]
                self.ip += 4
            elif op == 2:
                self.program[self.program[self.ip + 3]] = self.program[param1] * self.program[param2]
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
                    self.program[self.program[self.ip+3]] = 1
                else:
                    self.program[self.program[self.ip+3]] = 0
                self.ip += 4
            elif op == 8:
                if self.program[param1] == self.program[param2]:
                    self.program[self.program[self.ip + 3]] = 1
                else:
                    self.program[self.program[self.ip + 3]] = 0
                self.ip += 4            
            elif op == 99:
                #print("Halted")
                self.halted = True
                break
            else:
                print("Unexpected opcode")
                break

        return output

def amplifiers():
    outputs = []
    
    for phases in itertools.permutations([0, 1, 2, 3, 4]):
        A = IntCode(input_list.copy(), [phases[0], 0]).compute()
        B = IntCode(input_list.copy(), [phases[1], A]).compute()
        C = IntCode(input_list.copy(), [phases[2], B]).compute()
        D = IntCode(input_list.copy(), [phases[3], C]).compute()
        E = IntCode(input_list.copy(), [phases[4], D]).compute()
        
        outputs.append(E)
        
    return max(outputs)

def feedback_amplifiers():
    outputs = []

    for phases in itertools.permutations([5, 6, 7, 8, 9]):
        A, B, C, D, E = [IntCode(input_list.copy(), [p]) for p in phases]
        e = 0
        
        while(True):
            if E.halted:
                outputs.append(e)
                break
            
            A.input_code.append(e)
            a = A.compute()

            B.input_code.append(a)
            b = B.compute()

            C.input_code.append(b)
            c = C.compute()

            D.input_code.append(c)
            d = D.compute()

            E.input_code.append(d)
            e = E.compute()

    return max(outputs)

print(amplifiers())
print(feedback_amplifiers())
