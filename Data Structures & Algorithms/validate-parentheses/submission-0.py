class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        count = []

        for char in s:
            if char in mapping:
                if count and count[-1] == mapping[char]:
                    count.pop()
                else:
                    return False
            else:
                count.append(char)
        return count == []