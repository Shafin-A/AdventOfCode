import math


def build_2d_trees_array(input):
    trees = []

    for i, line in enumerate(input):
        trees.append([])
        for num in line:
            if num == '\n':
                continue
            trees[i].append(int(num))

    return trees


trees = build_2d_trees_array(open("Day8Input.txt", "r").readlines())

numrows = len(trees)
numcols = len(trees[0])

count = 0
max_result = -1
for i in range(numcols):
    for j in range(numrows):
        tree = trees[i][j]

        if (i == 0 or i == numcols - 1) or (j == 0 or j == numrows - 1):
            count += 1
            continue

        right_range = trees[i][j+1:numrows]
        left_range = trees[i][0:j]
        up_range = [trees[k][j] for k in range(numcols) if k < i]
        down_range = [trees[k][j] for k in range(numcols) if k > i]

        ranges = [right_range, left_range[::-1], up_range[::-1], down_range]

        if all(range_var for range_var in ranges):
            right_max = max(right_range)
            left_max = max(left_range)
            up_max = max(up_range)
            down_max = max(down_range)
        else:
            # assign a default value of negative infinity
            right_max = float("-inf")
            # assign a default value of negative infinity
            left_max = float("-inf")
            # assign a default value of negative infinity
            up_max = float("-inf")
            # assign a default value of negative infinity
            down_max = float("-inf")

        if any(tree > max_val for max_val in [right_max, left_max, up_max, down_max]):
            count += 1

        num_elements_before_greater_than_tree = []

        for curr_range in ranges:
            counter = 0
            for val in curr_range:
                if val < tree:
                    counter += 1
                else:
                    counter += 1
                    break
            num_elements_before_greater_than_tree.append(counter)

        max_result = max(max_result, math.prod(
            num_elements_before_greater_than_tree))

print(count)  # p1
print(max_result)  # p2
