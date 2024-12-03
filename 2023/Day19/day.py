import array
import re

filename = "input.txt"


def parse_input(filename):
    with open(filename, 'r') as file:
        workflows: dict[str, str] = {}
        ratings: list[str] = []

        for line in file:
            line = line.strip()
            if line:
                if line.startswith('{'):
                    ratings.append(line[1:-1])
                else:
                    pattern = re.compile(r'([a-zA-Z]+)\{([^}]+)\}')

                    matches = pattern.findall(line)

                    for key, values in matches:
                        value_list = values.split(',')
                        workflows[key] = value_list

        return workflows, ratings


workflows, ratings = parse_input(filename)


A_ratings = 0

arr = [1, 1, 1, 1]
max_value = 4000
combination_number = 0
total_combinations = max_value ** len(arr)

for _ in range((max_value ** len(arr))):
    combination_string = f"Combination {combination_number + 1}/{total_combinations}: {arr}"

    print(combination_string, end='\r', flush=True)

    for i in range(len(arr) - 1, -1, -1):
        x_rating = arr[0]
        m_rating = arr[1]
        a_rating = arr[2]
        s_rating = arr[3]

        key = 'in'
        while (True):
            if key == 'R':
                break
            elif key == 'A':
                A_ratings += 1
                break

            workflow = workflows[key]

            for flow in workflow:
                if ':' in flow:
                    rule, workflow_key = flow.split(':')

                    if '<' in rule:
                        rating_compared, compared_value = rule.split('<')
                        compared_value = int(compared_value)

                        if rating_compared == 'x':
                            if x_rating < compared_value:
                                key = workflow_key
                                break
                        if rating_compared == 'm':
                            if m_rating < compared_value:
                                key = workflow_key
                                break
                        if rating_compared == 'a':
                            if a_rating < compared_value:
                                key = workflow_key
                                break
                        if rating_compared == 's':
                            if s_rating < compared_value:
                                key = workflow_key
                                break

                    elif '>' in rule:
                        rating_compared, compared_value = rule.split('>')
                        compared_value = int(compared_value)

                        if rating_compared == 'x':
                            if x_rating > compared_value:
                                key = workflow_key
                                break
                        if rating_compared == 'm':
                            if m_rating > compared_value:
                                key = workflow_key
                                break
                        if rating_compared == 'a':
                            if a_rating > compared_value:
                                key = workflow_key
                                break
                        if rating_compared == 's':
                            if s_rating > compared_value:
                                key = workflow_key
                                break

                else:
                    key = flow

        arr[i] += 1
        if arr[i] > max_value:
            arr[i] = 1
        else:
            break

        combination_number += 1

print()
print(A_ratings)
