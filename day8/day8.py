def make_layers(image, width, height):
    layer_dict = {}
    layers = []

    for i in range(0, len(image), width):
        layers.append(image[i : i +width])

    dict_idx = 1
    for i in range(len(layers)):
        layer_dict.setdefault(dict_idx, [])
        layer_dict[dict_idx].append(layers[i])
        
        if (i+1) % height == 0:
            dict_idx += 1
        
    return layer_dict

def least_zeroes_ones_twos_mult(layer_dict):
    min_zeroes = 999
    idx = -1
    
    for key, val in layer_dict.items():
        num_zeroes = 0
        for v in val:
            num_zeroes += v.count('0')
        if num_zeroes < min_zeroes:
            min_zeroes = num_zeroes
            idx = key

    layer = layer_dict[idx]

    num_ones = 0
    num_twos = 0
    for l in layer:
        num_ones += l.count('1')
        num_twos += l.count('2')

    return num_ones*num_twos

def decode_image(layer_dict, width, height):
    decoded_image_list = ['2'] * width * height
    for i in range(1, len(layer_dict) + 1):
        layer = [item for sublist in layer_dict[i] for item in sublist] #flatten
        for j in range(0, len(layer)):
            if layer[j] != '2' and decoded_image_list[j] == '2':
                decoded_image_list[j] = layer[j]

    decoded_image = ""
    for i in range(len(decoded_image_list)):
        if i % width == 0:
            decoded_image += "\n"
        if decoded_image_list[i] == '0':
            decoded_image += ' + '
        elif decoded_image_list[i] == '1':
            decoded_image += ' O '
        else:
            decoded_image += "   "
    return decoded_image

f = open("input.txt", "r")
image = f.readline()
layer_dict = make_layers(image, 25, 6)

print(least_zeroes_ones_twos_mult(layer_dict))
print(decode_image(layer_dict, 25, 6))

