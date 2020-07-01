#!/usr/bin/env python3

__doc__: """
        List unique set of database combinations

    """

from itertools import permutations, chain, combinations, product
from math import ceil, log2


def powerset(s):
    """
    Return the powerset of a set
    """
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



def bitflip_db(db, positions):
    """
    Flip integers in db at positions
    """
    db2 = list(db)
    for pos in positions : 
        db2 = [ e^(1<<pos) for e in db2]

    return tuple(sorted(db2))



def shuffle(db, permutation):
    """
    Shuffle the binary of num with some position permutation

    :db: int, the number
    :permutation: tuple(int), the final permutation
    """
    db2 = []
    for num in db :
        num2 = 0
        for i, new_pos in enumerate(permutation):
            bit_at = (num & (1 << new_pos)) >> new_pos
            # updating from right to left 0xxx | j000
            num2 =  num2 | (bit_at << i)
        db2 += [num2]

    return tuple(sorted(db2))



def uniquedb(N):
    """
    Return the unique database with length N
    """
    n = ceil(log2(N))
    database = list(combinations(range(2**n), N))  
    for i,db in enumerate(database): 
        if db :
            complperm = product(powerset(range(n)), permutations(range(n)))
            equiv = set([shuffle(bitflip_db(db, c),p) for c, p in complperm])
            #future
            for j,d in enumerate(database[i+1:]) : 
                if d and d in equiv : 
                    database[i+1+j] = False

    return [d for d in database if d]
    

            






