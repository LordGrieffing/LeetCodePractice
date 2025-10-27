class Solution:

    def longestSubRep(self, str):

        length = len(str)
        currentString = 1
        longestString = 1

        for i in range(length - 1):
            if str[i] == str[i+1]:
                currentString += 1

                if currentString > longestString:
                    longestString += 1

        return longestString
    
    def longestSubNoRep(self, str):

        if len(str) == 0 or len(str) == 1:
            return len(str)

        left = 0
        right = 0
        longest = 0

        visit = [False] * 26

        while right < len(str):


            while visit[ord(str[right]) - ord('a')] == True:
                visit[ord(str[left]) - ord('a')] = False
                left += 1

            visit[ord(str[right]) - ord('a')] = True
            
            longest = max(longest, right - left + 1)
            right += 1

        return longest