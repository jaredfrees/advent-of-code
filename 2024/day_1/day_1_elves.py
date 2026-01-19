

# each item is total calories for one elf
elf_calorie_list  = list()
with open('input.txt') as file:
    one_elf_calories = 0
    for line in file:
        # print(line)
        
        if line.strip() == '':
            elf_calorie_list.append(one_elf_calories)
            one_elf_calories = 0
        else:
            one_elf_calories += int(line)

# print(max(elf_calorie_list))

top_three = sorted(elf_calorie_list)[-3:]

print(sum(top_three))
