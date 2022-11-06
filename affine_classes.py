# -*- coding: utf-8 -*-

from math import gcd
from itertools import chain, groupby
from affine_alphabet import *

class Message:

    # global alphSpecials
    
    def _flatten(self,listOfLists):
        """Flatten one level of nesting"""
        return chain.from_iterable(listOfLists)
    
    def _rBlanks(self,strng):
        """Removes blanks of a string strng and converts to uppercase"""
        return ''.join(strng.split()).upper()
    
    def _normalize(self,strng):
        """
        Removes blanks spaces of the string 'strng'; then removes accents
        according to 'alphSpecials'. If character 'ñ' occurs in 'strng' then
        'GN' appears in 'accum' as an entry, therefore '_flatten' is needed.
        """
        s = self._rBlanks(strng)
        accum = []
        for ch in s:
            if ch in alphSpecials:
                accum.append(alphSpecials[ch])
            else:
                accum.append(ch)
        return filter(lambda x: x in alphabet,self._flatten(accum))
        #return [c for c in self._flatten(accum) if c in alphabet]

    def __init__(self,strng):
        x = self._normalize(strng)
        self.content = ''.join(x)
        self.length = len(self.content)
        
    def __str__(self):
        return self.content


class Encipher(Message):

    # global n, m, f, chNum, numCh

    def _invMod(self,a:int,n:int) -> int:
        """Return multiplicative inverse of a modulo n.
           If the integers a and n are not coprime, then return 0."""
        try:
            x, g = pow(a,-1,n), 1
        except ValueError:
            g = 0
        return int(g==1 and x)
    
    def _translation(self,c,a,b):
            return numCh[format((a*int(chNum[c])+b)%len(alphabet),f)]
    
    def __init__(self,strng,a=1,b=0):
        Message.__init__(self,strng)
        self.decimation = a
        self.displacement = b
    
    def affine(self,mode=True):
        """Memoization based code mode: True for deciphering"""       
        mem, accum = {}, []
        if mode:
            a = self._invMod(self.decimation,len(alphabet))
            b = -a*self.displacement
        else:
            a, b = self.decimation, self.displacement
        for ch in self.content:
            if ch in mem:
                accum.append(mem[ch])
            else:
                mem[ch]=self._translation(ch,a,b)
                accum.append(mem[ch])
        return ''.join(accum)


class ChiSquareAttack(Encipher):

    # global alphFreq
    
    def __init__(self,strng):
        Encipher.__init__(self,strng)
    
    def rfrec(self, strng):
        return {k:len(list(g))/len(strng) for k, g in groupby(''.join(sorted(strng)))}
    
    def chiSquared(self, strng):
        inventory = dict.fromkeys(alphabet,0)
        inventory.update(self.rfrec(strng))
        chDegree =[(len(strng)*(inventory[ch]-alphFreq[ch]))**2/alphFreq[ch] for ch in inventory]
        return sum(chDegree)

    def chiSquaredTest(self) -> list:
        # n = len(alphabet)
        candidates = []
        for a in range(1, n):
            if gcd(a,n) == 1:
                for b in range(n):
                    T = Encipher(self.content,a,b)
                    dec = T.affine(True)
                    candidates.append((a, b, self.chiSquared(dec)))
        return sorted(candidates, key = lambda x: x[2])
