class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = ["*" , "+" , "-" , "/"]
        for t in tokens:
            if t in signs:
                # get the last 2 values from the list
                b = stack.pop()
                a = stack.pop()
                # print(a , b , t)
                if t == "*":res = a * b
                elif t == "/": res = int(a / b)
                elif t == "+": res = a + b
                else: res = a - b
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]
