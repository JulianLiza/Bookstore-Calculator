import ArrayStack


class Calculator:
    def __init__(self):
        self.dict = None

    def balanced_parens(self, s: str) -> bool:
        """
        This function checks if the string s contains balanced parentheses
        :param s: str type; the string to be checked
        :return: bool type; True if the string s contains balanced parentheses
        """
        stack = ArrayStack.ArrayStack()
        matching = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching.values():
                stack.push(char)
            elif char in matching.keys():
                if stack.size() == 0 or stack.pop() != matching[char]:
                    return False

        return stack.size() == 0


