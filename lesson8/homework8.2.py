from pathlib import Path
first = 'haiku'
second = 'The frog and the cat'
third = 'croak and mew in fine duet'
fourth = 'All goes together'
current_path = Path(__file__)
current_dir = current_path.parent
print(current_dir)
current_file_name = current_path.stem
print(current_file_name)
with open(
    current_dir.joinpath("second_task.txt"),
    mode="w",
    encoding="utf-8"
) as write_file:
    # new_data = [
    #     first + '\n' + second
    # ]
    write_file.writelines(f'{first}\n {second}\n')
with open(
    current_dir.joinpath("second_task.txt"),
    mode="a",
    encoding="utf-8"
) as write_file:
    # new_data = [
    #     first + '\n' + second
    # ]
    write_file.writelines(f'{third}\n {fourth}')