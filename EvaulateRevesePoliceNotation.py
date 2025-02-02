tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token.lstrip('-').isdigit():  # Allow negative numbers
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(int(operand1 / operand2))
    return stack[0]

print(evalRPN(tokens))
