from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            # use sorted string as key
            sortedS= "".join(sorted(i))
            # it will check if we have this key before or not /n
            # if we didnot the word add as a new key , if we had it before added to the list
            res[sortedS].append(i)
        return list(res.values())