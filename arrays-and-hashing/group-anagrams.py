# N = number of strings in strs
# K = average length of each string
# Time:   O(N * K)
# Space:  O(N * K)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            count = tuple(count)
            if count in d:
                d[count].append(s)
            else:
                d[count] = [s]

        return list(d.values())
