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
    print("Part 1: " + part1_answer)

def part2(input_text):
    # Code goes here
    print("Part 2: " + part2_answer)

with open("../input/Day"+{day}) as input:
    # Code goes here
    part1(input)
    part2(input)
""".format(day=day)
    currentdir = os.getcwd()
    print(currentdir)
    os.mkdir(currentdir + "/Day" + day)
    with open(currentdir + "/Day" + day + "/run.py", "w") as file:
        file.write(s)
    print("Success")