import sys
import subprocess

user_args = sys.argv

original_file_name = user_args[1]
new_file_name = user_args[2]

input_text = subprocess.run(
    [f"cat {original_file_name}"],
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True
).stdout

line_to_replace = 27
file_to_insert_to = "template.html"

lines = []

with open(file_to_insert_to, "r") as file:
    lines = file.readlines()
    lines[line_to_replace - 1] = input_text

with open(file_to_insert_to, "w") as file:
    for item in lines:
        file.writelines(item)
