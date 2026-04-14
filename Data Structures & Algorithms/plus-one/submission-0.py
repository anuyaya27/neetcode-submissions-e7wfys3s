class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      num = int("".join(map(str, digits)))
      one = num + 1
      result = [int(x) for x in str(one)]

      return result
