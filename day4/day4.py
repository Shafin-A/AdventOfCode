def num_passwords_p1(min, max):
    count = 0
    
    for i in range(min, max + 1):
        string_int = str(i)
        
        if len(string_int) > 6:
            continue
        
        doubles = False
        increase = True
        
        for i in range(1, len(string_int)):
            if string_int[i] == string_int[i-1]:
                doubles = True
            if string_int[i] < string_int[i-1]:
                increase = False
        if doubles and increase:
            count += 1

    return count

def num_passwords_p2(min, max):
    count = 0
    
    for i in range(min, max + 1):
        string_int = str(i)
        
        if len(string_int) > 6:
            continue
        
        doubles = False
        increase = True
        matchings = {}

        for i in range(1, len(string_int)):
            if string_int[i] == string_int[i - 1]:
                matchings.setdefault(string_int[i], set())
                matchings[string_int[i]].add(i)
                matchings[string_int[i]].add(i-1)
                
            if string_int[i] < string_int[i-1]:
                increase = False
                
        for k in matchings:
                if len(matchings[k]) == 2:
                    doubles = True
                    
        if doubles and increase:
            count += 1

    return count


print(num_passwords_p1(284639, 748759))
print(num_passwords_p2(284639, 748759))
              
    
