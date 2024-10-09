# Taking input a fpur digit number
num = int(input("Enter a four digit number: "))
original_num = num

# Program to reverse this number
new_num = ''
loop = len(str(num))
for digit in range(loop):
    last = num % 10
    num //= 10
    new_num += str(last)
    # print(new_num)

print(new_num)

# # Check if the reverse is True

if new_num == str(original_num):
    print("Reverse is True")
else:
    print("Reverse is not True")
