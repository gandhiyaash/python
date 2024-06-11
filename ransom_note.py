'''
Leetcode : 383
Problem Statement : https://leetcode.com/problems/ransom-note/description/
'''

from collections import defaultdict
# ransomNote = aa , magazine = aab

def canConstruct(ransomnote:str, magazine:str):
    d=defaultdict(int)
    for char in magazine:
        d[char] += 1
    for char in ransomnote:
        if char not in d and d[char] <= 0:
            return False
        d[char] -= 1
    return True




result = canConstruct(ransomnote = 'aacc', magazine = 'aab')
print(result)





