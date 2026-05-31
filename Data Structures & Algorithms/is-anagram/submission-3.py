class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        hashmap = {}

        # Initialize the hashmap with the frequency of the string
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        # print(f'hashmap: {hashmap}')
            
        for char2 in t:
            if char2 in hashmap:
                hashmap[char2] -= 1

        # print(f'hashmap after t: {hashmap}')
        final_freq = 0
        
        for val in hashmap.values():
            if val < 0:
                return False
            final_freq += val

        if final_freq == 0: return True
        return False