
def find_marker(data, window_length):
    for i in range(len(data)):
        if len(set(data[i : i+window_length])) == window_length:
            return i+window_length, data[i : i + window_length]


input_data = open("Day6Input.txt", "r").readline()

print(find_marker(input_data, 4)) # p1
print(find_marker(input_data, 14)) # p2
