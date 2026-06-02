class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:

            sorted_str = ''.join(sorted(word))

            result[sorted_str].append(word)

        return list(result.values())