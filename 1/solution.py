# day 1 
import collections

filename = "input.txt"

## part 1
list1 =[]
list2=[]
with open(filename, 'r') as f:
    for line in f.readlines():
        num1, num2 = line.split()

        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()

total_distance = 0 
for num1, num2 in zip(list1, list2):
    diff = abs(int(num1)-int(num2))
    total_distance +=diff

print(total_distance)

coll1 = collections.Counter(list1)
coll2 = collections.Counter(list2)


sim_count =0
for num in coll1.keys():
    if num in coll2.keys():
        sim_count += coll1[num] * coll2[num] * int(num)

print(sim_count)




