class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
            "/": lambda x,y: int(x/y)
        }
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                _eval = ops[token](int(a),int(b))
                stack.append(_eval)
            else:
                stack.append(token)
        
        return int(stack[-1])
