# -*- coding: utf-8 -*-

from math import log

# Alphabet

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alphSpecials = {
            'Á' : 'A',
            'É' : 'E',
            'Í' : 'I',
            'Ó' : 'O',
            'Ú' : 'U',
            'Ä' : 'A',
            'Ë' : 'E',
            'Ï' : 'I',
            'Ö' : 'O',
            'Ü' : 'U',
            'Ñ' : 'GN'
            }


# Alphabet Parameters

n = len(alphabet)
m = int(log(len(alphabet),10))+1
f = '0{0}d'.format(str(m))
# chNum = dict(zip(alphabet,[format(i,f) for i,v in enumerate(alphabet)]))
chNum = {v:format(i,f) for i, v in enumerate(alphabet)}
numCh = {v:i for i, v in chNum.items()}

# Alphabet Frecuences for Spanish

alphFreq = {
    'A' : 12.53,
    'B' : 1.42,
    'C' : 4.68,
    'D' : 5.86,
    'E' : 13.68,
    'F' : 0.69,
    'G' : 1.01,
    'H' : 0.70,
    'I' : 6.25,
    'J' : 0.44,
    'K' : 0.02,
    'L' : 4.97,
    'M' : 3.15,
    'N' : 6.71,
    'O' : 8.68,
    'P' : 2.51,
    'Q' : 0.88,
    'R' : 6.87,
    'S' : 7.98,
    'T' : 4.63,
    'U' : 3.93,
    'V' : 0.90,
    'W' : 0.01,
    'X' : 0.22,
    'Y' : 0.90,
    'Z' : 0.52
    }
