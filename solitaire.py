# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 13:19:24 2015

@author: michar
"""
import random

class Deck(object):
    def __init__(self, in_list=None):
        if in_list is None:
            self.cards = [(n,t) for n in ['1','2','3','4','5','6','7','8','9','10','Q','J','K'] 
                            for t in 'ATLY']
        else:
            #assert(len(in_list) == 52)
            self.cards = in_list
    
    def randomize(self):
        random.shuffle(self.cards)
    def __str__(self):
        return str(self.cards)
    def __iter__(self):
        for card in self.cards:
            yield card
            
            
class Solitaire(object):
    def __init__(self, deck):
        self.deck = deck
        self.state = [[card] for card in self.deck]
        
    def solve(self):
        match_found = True
        while match_found:
            match_found = False
            for i in xrange(len(self.state)):
                try:
                    if self._match(self.state[i], self.state[i+2]):
                        self._contract(i)
                        match_found = True
                        break
                except IndexError:
                    pass
        return len(self.state)
    
    def _match(self, bump1, bump2):
        return bump1[0][0] == bump2[0][0] or bump1[0][1] == bump2[0][1]
    
    def _contract(self, i):
        self.state[i+1].extend(self.state[i])
        self.state[i] = self.state[i+1]
        del self.state[i+1]
        return
        
    def get_deck_by_bumps(self, from_end=False):
        singles = []
        bumps = []
        iterator = reversed(self.state) if from_end else iter(self.state)
        for b in iterator:
            if len(b) > 1:
                bumps.extend(b)
            else:
                singles.extend(b)
        bumps.extend(singles)
        return Deck(reversed(bumps))
    
    def get_bumps_deck(self, from_end=False):
        bumps = []
        iterator = reversed(self.state) if from_end else iter(self.state)
        for b in iterator:
            if len(b) > 1:
                bumps.extend(b)
            else:
                continue
        return Deck(reversed(bumps))
        
    def __str__(self):
        max_depth = max(self.state, key=lambda x:len(x))
        rep = ''
        for i in range(len(max_depth)):
            for b in self.state:
                if len(b) > i:
                    rep +=  b[i][0]+b[i][1]+',\t'
                else:
                    rep += '  \t, '
            rep += '\n'
        return rep
            
        
if __name__ == '__main__':
    f = open('out.txt','w')
    d = Deck()
    #print d
    d.randomize()
    print d
#    s = Solitaire(d)
#    print>>f, s
#    s.solve()
#    print>>f, s
#    d1 = s.get_deck_by_bumps(from_end=False)
    #assert(d1==d)
    l = 53
    l1 = 52
    for i in xrange(50):
        l = l1
        s = Solitaire(d)
        l1 = s.solve()
        print l
        d = s.get_deck_by_bumps(from_end=True)
        if l1 == 2:
            break
    print l1