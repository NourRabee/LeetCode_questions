class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
            List = []
            if s not in t:
                for i in s:
                    if i in t and (s.count(i) <= t.count(i)):
                        List.append(i)
                    else:
                        return False
                myList=[x for x in t if x in List]

                hashmap = {}
                for i in List:
                    hashmap[i] = List.count(i)

                hashmap2 = {}
                for i in myList:
                    hashmap2[i] = myList.count(i)

                x = dict(zip(hashmap.keys(), hashmap2.keys()))
                y = dict(zip(hashmap.values(), hashmap2.values()))

                for (key, value) in x.items():
                    if value == key:
                        pass
                    else:
                        return False
                for (key, value) in y.items():
                    if value >= key:
                        pass
                    else:
                        return False
                return True
            else:
                return True
