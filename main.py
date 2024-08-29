from typing import List
from collections import defaultdict
from collections import Counter
class Solution:
    # https://leetcode.com/problems/contains-duplicate/
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset: return True
            hashset.add(n)
        return False
    # https://leetcode.com/problems/valid-anagram/
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
        return all(v == 0 for v in count.values())
    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in num_idx: return [i, num_idx[y]]
            num_idx[x] = i
        return []
    # https://leetcode.com/problems/group-anagrams/
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s: count[ord(c) - ord("a")] += 1 # Construct char counts as keys
            ret[tuple(count)].append(s)
        return ret.values()

def is_permutation(a: List[List[str]], b: List[List[str]]) -> bool:
    diff = 0
    for i in a:
        diff += 1
        for j in b:
            if Counter(i) == Counter(j):
                diff -= 1
                break
    return diff == 0

def check(b: bool):
    if not b: raise Exception("Wrong Answer")
    print("Accepted")
sol = Solution()
print("Contains Duplicate: ", end = '')
check(sol.containsDuplicate([1,2,3,1]) == True and
    sol.containsDuplicate([1,2,3,4]) == False and
    sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True)

print("Valid Anagram: ", end = '')
check(sol.isAnagram("anagram", "nagaram") == True and
    sol.isAnagram("rat", "car") == False)

print("Two Sum: ", end = '')
check(Counter(sol.twoSum([2,7,11,15], 9)) == Counter([0,1]) and
    Counter(sol.twoSum([3,2,4], 6)) == Counter([2,1]) and
    Counter(sol.twoSum([3,3], 6)) == Counter([1, 0]))

print("Group Anagrams: ", end = '')
check(is_permutation(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]]))
