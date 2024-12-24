import re

filename = "input.txt"


with open(filename, "r") as f:
    input_str = f.readlines()


rules_dict = {}
updates = []
for line in input_str:
    if re.findall("\d*\|\d*", line):
        if line[: line.find("|")] in rules_dict.keys():
            new_list = rules_dict[line[: line.find("|")]].append(
                int((line[line.find("|") + 1 :]).strip())
            )
        else:
            rules_dict[line[: line.find("|")]] = [
                int((line[line.find("|") + 1 :]).strip())
            ]
    elif line.strip() != "":
        instruc_list = line.strip().split(",")
        updates.append(instruc_list)


def check_compare_pos(rule_line, rule_list):
    for pos, num in enumerate(rule_line):
        for pos2, num2 in enumerate(rule_line):
            if (
                str(num) in rule_list.keys()
                and int(num2) in rule_list[str(num)]
                and pos2 < pos
            ):
                return False, pos, pos2
    return True, -1, -1


valid_lines = []
invalid_lines = []
for line in updates:
    check_pos, _, _ = check_compare_pos(line, rules_dict)
    if check_pos:
        valid_lines.append(line)
    else:
        invalid_lines.append(line)


sum_of_middle_number = 0
for line in valid_lines:
    middleIndex = (len(line) - 1) / 2
    sum_of_middle_number += int(line[int(middleIndex)])

print(sum_of_middle_number)


# part 2
fixed_lines = []
for line in invalid_lines:
    pos_check = False

    new_line = line
    while not pos_check:
        new_idx = []
        pos_check, pos1, pos2 = check_compare_pos(new_line, rules_dict)
        for pos, element in enumerate(new_line):
            if pos == pos1:
                new_idx.append(pos2)
            elif pos == pos2:
                new_idx.append(pos1)
            else:
                new_idx.append(pos)
        new_line = [new_line[i] for i in new_idx]
    fixed_lines.append(new_line)


sum_of_middle_number = 0
for line in fixed_lines:
    middleIndex = (len(line) - 1) / 2
    sum_of_middle_number += int(line[int(middleIndex)])

print(sum_of_middle_number)
