from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)

        pushes = 0
        for i, f in enumerate(freq):
            pushes += f * ((i // 8) + 1)

        return pushes
        return pushes
        