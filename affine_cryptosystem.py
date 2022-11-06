# -*- coding: utf-8 -*-

import sys
from affine_classes import *  

"""
  Example of use:

  python3 affine_cryptosystem.py encipheringText.txt 21 13 0 (in order to enciphering)

  python3 affine_cryptosystem.py plainText.txt 21 13 1 (in order to deciphering)

  anyone of the following attacks with ChiSquare method, since
  len(sys.argv) != 5 occurs:

  python3 affine_cryptosystem.py encipheringText.txt 21 13 
  python3 affine_cryptosystem.py encipheringText.txt 21
  python3 affine_cryptosystem.py encipheringText.txt (the best)

  if (sys.argv[2],26) != 1, the deciphering gives a string of A since
  _invMod() is specilly designed for this.

  The alphabet is set to 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; with another alphabet
  test ChiSquared don't work properly, but yes ciphering and deciphering.

"""

def readTxt(fichero):
    with open(fichero,'r') as f:
        lines = f.readlines()
    accum = [k[:-1] for k in lines]
    return ''.join(accum)

if __name__ == "__main__":
    
    T = readTxt(sys.argv[1])
    if len(sys.argv) == 5:
        P = Encipher(T,int(sys.argv[2]),int(sys.argv[3]))
        mode = bool(int(sys.argv[4]))
        E = P.affine(mode)
        print(E)
    else:
        C = ChiSquareAttack(T)
        S = C.chiSquaredTest()
        print(S[:3])
