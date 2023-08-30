# checking if an array of intergers contains duplicate
class Solution:
    def containsDuplicate(self,nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add (n)
        return False


# valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countS.get( t[i], 0 )

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True


# producing O(1) time complexity solution
# sorted order 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)



# Two sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index

        for i , n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i

        return


# group anagrams, catergorizing string by count
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # mapping charcount to list of anagrams

        for s in strs:
            count = [0] * 26 # a .... z

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.value()
        O(m*n)


#Top K frequent elements
# bucket sort
class Solution:
    def topKFrequennt(self, nums: list[int], k:int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]







