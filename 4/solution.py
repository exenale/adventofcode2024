import re

filename = "input.txt"

with open(filename, "r") as f:
    horizontal_lines = f.readlines()


def get_down_line(lines) -> list:
    down_lines = []
    for i in range(len(lines[0])):
        new_down_line = ""
        for line in lines:
            line.strip()
            new_down_line += line[i]
        down_lines.append(new_down_line)
    return down_lines


def get_slash_lines(lines) -> list:
    new_lines = []
    # max_len = len(lines[0])
    # line = lines[0]
    for line_pos, line in enumerate(lines):
        orig_pos = 0
        # print(line)
        for i in range(len(line)):
            pos = orig_pos
            new_line = ""
            if line_pos > 0 and i > 0:
                continue
            for candidate_lines in lines[line_pos:]:

                if len(candidate_lines) > pos:
                    new_line += candidate_lines.strip()[pos]
                pos += 1
            orig_pos += 1
            new_lines.append(new_line)
    return new_lines


regex = "XMAS|SAMX"


horizontal_lines = [line.strip() for line in horizontal_lines]
vertical_lines = get_down_line(horizontal_lines)
backslash_lines = get_slash_lines(horizontal_lines)
reverise_search = [line[::-1] for line in horizontal_lines]
frontslash_lines = get_slash_lines(reverise_search)

all_lines = [horizontal_lines, vertical_lines, backslash_lines, frontslash_lines]


count_xmas = 0
for line_lsts in all_lines:
    for line in line_lsts:
        xmas_instasnces = re.findall("SAMX", line)
        xmas_insces_2 = re.findall("XMAS", line)

        insiide_count = len(xmas_instasnces) + len(xmas_insces_2)
        count_xmas += insiide_count

print(count_xmas)


count_xmas = 0
all_lines = [horizontal_lines, vertical_lines, backslash_lines, frontslash_lines]

for line_count, line in enumerate(horizontal_lines):
    if line_count >= len(horizontal_lines) - 2:
        continue
    for pos, letter in enumerate(line):
        if pos >= len(line) - 2:
            continue

        if letter in ["M", "S"] and line[pos + 2] in ["M", "S"]:

            if horizontal_lines[line_count + 1][pos + 1] == "A":

                if (
                    horizontal_lines[line_count + 2][pos] in ["M", "S"]
                    and horizontal_lines[line_count + 2][pos] != line[pos + 2]
                ):

                    if (
                        horizontal_lines[line_count + 2][pos + 2] in ["M", "S"]
                        and horizontal_lines[line_count + 2][pos + 2] != letter
                    ):

                        count_xmas += 1

print(count_xmas)
