class Solution:
    def countVowelPermutation(self, n: int) -> int:
        k = int(1e9)+7
        vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        for i in range(n - 1):
            new_vowels = {'a': vowels['e'] + vowels['i'] + vowels['u'],
               'e': vowels['a'] + vowels['i'],
               'i': vowels['e'] + vowels['o'],
               'o': vowels['i'],
               'u': vowels['i'] + vowels['o']}
            vowels = new_vowels

        return sum(vowels.values())%k
            
        