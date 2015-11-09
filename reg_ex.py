import re

my_file = open('/home/zach/Downloads/actual_data.txt', 'r')
num_list = list()

for line in my_file:
	line = line.rstrip()
	numbers = re.findall('[0-9]+', line)
	if len(numbers) > 0:
		for num in numbers:
			num_list.append(int(num))

sum = 0
for number in num_list:
	sum += number

print sum
my_file.close()

