import re
filename = "input.txt"

with open(filename, 'r') as f:
    input_str= f.read()

valid_ins = re.findall("mul\(\d*,\d*\)", input_str)

sum_all =0 
for ins in valid_ins:
    num1, num2 = (ins[4:len(ins)-1]).split(",")
    sum_all += int(num1)*int(num2)
print(sum_all)


# part 2

valid_ins_2 = re.findall("mul\(\d*,\d*\)|don't\(\)|do\(\)", input_str)

sum_enabled = True
sum_all =0 
for ins in valid_ins_2:
    if ins == "do()":
        sum_enabled = True
        continue
    if ins =="don't()":
        sum_enabled = False
    if sum_enabled:
        num1, num2 = (ins[4:len(ins)-1]).split(",")
        sum_all += int(num1)*int(num2)

print(sum_all)

