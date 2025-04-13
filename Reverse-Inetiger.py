x=1534236469
stack = []
stack1 =[]
stack2 = []
# print(str(x))
y = str(x)
c = "ABC"
for num in y:
    # print(num)
    stack.append(num)
print(len(stack))
stack_len = len(stack)
is_negative = False
if stack[0] == '-':
    is_negative = True
    stack.pop(0)  # Remove the minus sign
    stack_len = stack_len-1
print(stack)

i = 0
while i<stack_len:
        stack1.append(stack[i])
        i+=1
print(stack1)
if(stack1[stack_len-1]=='0'):
    stack1.pop()
    print(stack1)
for i in range(len(stack1)):
    c = stack1.pop()
    stack2.append(c)
print(stack2)
num_str = ''.join(stack2)
if is_negative:
    num_str = '-' + num_str
    reversed_num =  int(num_str)
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        print(0)
    else:
        print(reversed_num)


