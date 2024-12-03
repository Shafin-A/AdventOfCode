import os


def find_next_day_number():
    # Get a list of existing folders
    existing_folders = [
        folder for folder in os.listdir() if os.path.isdir(folder)]

    # Find the highest day number in the existing folders
    existing_day_numbers = [
        int(folder[3:]) for folder in existing_folders if folder.startswith("Day")]
    next_day_number = max(existing_day_numbers, default=0) + 1

    return next_day_number


def create_day_folder(day_number):
    # Create folder name
    folder_name = f"Day{day_number:02}"

    # Create folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create day.py file content
    day_py_content = f"""filename = "input.txt"

with open(filename) as file:
    for line in file:
        pass
"""

    # Create day.py file
    day_py_path = os.path.join(folder_name, "day.py")
    with open(day_py_path, 'w') as day_py_file:
        day_py_file.write(day_py_content)

    # Create input.txt file (empty for now)
    input_txt_path = os.path.join(folder_name, "input.txt")
    open(input_txt_path, 'a').close()

    print(f"Folder '{folder_name}' created with day.py and input.txt.")


if __name__ == "__main__":
    # Automatically find the next available day number
    day_number = find_next_day_number()

    # Call the function to create the folder structure
    create_day_folder(day_number)
