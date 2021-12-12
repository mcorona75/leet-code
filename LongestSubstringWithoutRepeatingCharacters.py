# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Constraints:
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Start with the final substr and keep track of the current substr. Both start as empty.
        substr = ""
        curr_substr = ""

        #For each character in the string
        for c in s:
            #is the current character in the current substring?
            if c in curr_substr:
                #Yes it is, check to see if this is the biggest substring.
                if len(curr_substr) > len(substr):
                    #This is the longest new substr! 
                    substr = curr_substr
                #Make the current substr everything after this character.
                x = curr_substr.split(c,1)

                #Split indexing wasn't working when it's trying to split on the last char, special case for that.
                if curr_substr.endswith(c):
                    curr_substr = c
                else:
                    curr_substr = x[1] + c
            else:
                #Continue adding this to the current substr
                curr_substr+=c

        #Done parsing the string! Now compare the current against the largest known and return it!
        if len(substr) > len(curr_substr):
            return len(substr)
        else:
            return len(curr_substr)

sol = Solution
print(sol.lengthOfLongestSubstring(sol,"loddktdji"))