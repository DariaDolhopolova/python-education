numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

for i in range(1,4):
    numbers.append(i)

strings.append("hello")
strings.append("world")
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)