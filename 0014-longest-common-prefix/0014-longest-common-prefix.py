class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        # Compare prefix with every other word
        for word in strs[1:]:

            # Reduce prefix until it matches the start of 'word'
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
