#!/usr/bin/env python
# coding: utf-8
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

 

Note:

    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# In[ ]:


# Accepted in Leetcode
class Solution(object):
    def intervalIntersection(self, A, B):
        result = []
        i = 0
        j = 0
        while (i < len(A) and j < len(B)):
            a = A[i]
            b = B[j]
            # Non Overlapping Cases
            if (a[1] < b[0]):
                i += 1
            elif (b[1] < a[0]):
                j += 1
            # Overlapping Cases
            else:
                start = max(a[0], b[0])
                end = min(a[1], b[1])
                result.append([start, end])
                if (a[1] < b[1]):
                    i += 1
                elif (a[1] > b[1]):
                    j += 1
                else:
                    i += 1
                    j += 1
        return result
        


# In[ ]:


# Python 3 Syntax - Accepted in Leetcode
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i = 0
        j = 0
        while (i < len(A) and j < len(B)):
            a = A[i]
            b = B[j]
            # Non Overlapping Cases
            if (a[1] < b[0]):
                i += 1
            elif (b[1] < a[0]):
                j += 1
            # Overlapping Cases
            else:
                start = max(a[0], b[0])
                end = min(a[1], b[1])
                result.append([start, end])
                if (a[1] < b[1]):
                    i += 1
                elif (a[1] > b[1]):
                    j += 1
                else:
                    i += 1
                    j += 1
        return result
        
        

