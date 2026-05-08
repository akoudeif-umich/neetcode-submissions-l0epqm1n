class Solution:
    def isAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        dict1, dict2 = defaultdict(int), defaultdict(int)

        for i in range(len(s1)):
            dict1[s1[i]] += 1
            dict2[s2[i]] += 1

        return dict1 == dict2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        visited = [False for i in strs]

        res = []

        for i, curr in enumerate(strs):
            if visited[i] == True:
                continue
            visited[i] == True
            temp = [curr]
            for j in range(i + 1, len(strs)):
                if not visited[j] and self.isAnagram(curr, strs[j]):
                    temp.append(strs[j])
                    visited[j] = True
            res.append(temp)
        return res