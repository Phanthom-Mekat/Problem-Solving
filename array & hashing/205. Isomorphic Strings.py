class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_map_1={}
        dict_map_2={}
        for a,b in zip(s,t):
            if a in dict_map_1 :
                if dict_map_1[a]!=b :
                    return False
            elif b in dict_map_2:
                if dict_map_2[b]!=a :
                    return False
            else:
                dict_map_1[a]=b
                dict_map_2[b]=a
        return True