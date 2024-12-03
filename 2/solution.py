# day 1 
import collections

filename = "input.txt"


def check_level_safety(level_val:str) -> bool:
    level_val = level_val.strip()
    lvels = level_val.split()

    lvls1=lvels[0:len(lvels)-1]
    lvls2=lvels[1:len(lvels)]

    return validate_lvl(lvls1, lvls2)


def validate_lvl(lvls1, lvls2):
    base_dir = "dec"
    if int(lvls1[0])<int(lvls2[0]):
        base_dir= "inc"
    for val1, val2 in zip(lvls1,lvls2):
        diff = int(val1)-int(val2)
        if abs(diff) > 3 or diff==0:
            return False
        if diff < 0 and base_dir=="dec":
            return False
        if diff > 0 and base_dir=="inc":
            return False
    return True

def check_safety_with_dampener(level_val):
    level_val = level_val.strip()
    lvels = level_val.split()

    if not check_level_safety(level_val):
        for i in range(len(lvels)):
            new_list = lvels[:i]+lvels[i+1:]
            lvls1=new_list[0:len(new_list)-1]
            lvls2=new_list[1:len(new_list)]
            if validate_lvl(lvls1, lvls2):
                return True
        return False
    return True
            

## part 1
level_list =[]
with open(filename, 'r') as f:
    level_list= f.readlines()


count_safe =0
dampener_count_safe=0
for line in level_list:
    if check_level_safety(line):
        count_safe+=1
    dampener_count_safe += 1 if check_safety_with_dampener(line) else 0
print("No dampener: ", count_safe)
print("Dampener Active: ", dampener_count_safe)