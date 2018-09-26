class Solution:
    def dictionaryMatching(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: List[str]
        """
        def trieAdd(word):
            '''
            Expend Trie with word, Trie has root s0
            :param word: string
            :return: None
            '''
            if len(word) == 0:
                return None
            snum = 0#state number of root
            for item in list(word):
                s = trie[snum]
                num = (s['son']).get(item)
                if num != None:# son jumping to by char already exists
                    snum = num
                else:# build a new state and add into trie as a son of s
                    s1 = {}
                    trie.append(s1)#???
                    s1['son'] = {}
                    s1['suffix_snum'] = 0
                    s1['string'] = s['string'] + item
                    s1['indict']=False
                    num = len(trie)-1
                    # add to father's son
                    (s['son'])[item] = num
                    s1['father']= snum
                    snum = num
            s = trie[snum]
            s['indict'] = True

        def trieBildsuffix():
            #using broad-first search to build longest suffix for each state in trie
            snum = 0
            next = []
            next.append(snum)
            while next != []:
                snum = next[0]
                next = next[1:]
                s = trie[snum]
                stringNow = s['string']
                if len(stringNow)!=0:
                    charNow =stringNow[len(stringNow)-1]
                else:
                    charNow = ''
                father = s['father']
                father_suffix = (trie[father])['suffix_snum']
                if father != father_suffix: # root and sons of root are excluded
                    while True:
                        sf_s = trie[father_suffix]
                        suffix = sf_s['son'].get(charNow)
                        if suffix == None:
                            if father_suffix == 0:
                                s['suffix_snum'] = 0
                                break
                            else:
                                father_suffix = sf_s['suffix_snum']
                        else:
                            s['suffix_snum'] = suffix
                            break
                for item in (s['son']).values():
                    next.append(item)

        # each state is stored as a dictionary
        # state0:{'son':{next char:next state num}, 'father': state num,
        #          'suffix_snum': longest suffix in Trie(state num), 'string':string matching until now,
        #          'indict': is_in_dict}
        s0={'son':{},'father':0, 'suffix_snum':0,'string': '', 'indict':False}
        trie = []
        trie.append(s0)
        for item in words:
            trieAdd(item)
        trieBildsuffix()
        snum = 0
        for i in range(len(S)):
            #Current stata num is snum, next input char is S[i]
            charNow = S[i]
            s = trie[snum]
            sons = s['son']#{_:_,_:_,...}
            while sons.get(charNow) == None:
                if s['string'] == '':# s is root
                    snum = 0
                    break
                else:
                    snum = s['suffix_snum']
                    s = trie[snum]
                    sons = s['son']#{_:_,_:_,...}
            else:
                snum = sons.get(charNow)
            snum1= snum# snum should be kept for next input chat
            while snum1 != 0 :
                s = trie[snum1]
                if s['indict']:
                    print(s['string']+' ', end='')
                snum1 = s['suffix_snum']

if __name__ == '__main__':
    Solution().dictionaryMatching('aaabca',['ca','bc','bcd'])



