# iterate through the arr of string
# isolate any ints in string
# isolate first and last ints in string
# combine them to make a two-digit num
# append two-digit num into a sum
# return sum

def trebuchet(arr):
    sum = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in arr:
        nums = []
        for chars in i:
            if chars in digits:
                nums.append(chars)
        first = nums[0]
        last = nums[-1]
        double_digits = str(first) + str(last)
        sum += int(double_digits)

    return sum

arr = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet'] # output 142
print(trebuchet(arr))