import os
import sys

if len(sys.argv) != 2:
    print("Please specify which day to instantiate. E.g: python3 ./newday.py 1")
    sys.exit(1)

else:
    day = sys.argv[1]
    s = """\
import os

def part1(input_text):
    # Code goes here
    return ("Part 1: " + part1_answer)

def part2(input_text):
    # Code goes here
    return ("Part 2: " + part2_answer)

# TODO Make this cleaner, it makes me sad :(
with open("../input/Day1.txt", "r") as input:
    print(part1(input))

with open("../input/Day1.txt", "r") as input:
    print(part2(input))

""".format(day=day)
    currentdir = os.getcwd()
    print(currentdir)
    os.makedirs(currentdir + "/Challenges/2023/Day" + day)
    with open(currentdir + "/Challenges/2023/Day" + day + "/run.py", "w") as file:
        file.write(s)
    print("Success")