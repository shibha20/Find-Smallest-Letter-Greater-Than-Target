class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for item in letters:
            if item > target:
                output = item
                break
            else:
                output = letters[0]
        
        return output