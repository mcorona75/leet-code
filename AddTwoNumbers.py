# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1sum=0
        l2sum=0
        output=[]
        digit = 1


        for num in l1:
            l1sum += num*digit
            digit *= 10
        
        digit=1
        for num in l2:
            l2sum += num*digit
            digit*=10
        
        total=l1sum+l2sum
        
        stotal = str(total)

        for char in stotal:
            output.append(char)

        return output

sol=Solution
sol.addTwoNumbers(sol,[2,4,3],[5,6,4])
