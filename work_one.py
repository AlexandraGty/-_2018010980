#!/usr/bin/python3
"""
  Author:  Ty.Gu
  Purpose: Generate random data set.
  Created: 18/4/2020
"""

import random
import string

def create_set(datatype, datarange, num, strlen=8):
    old_set = set()
    for i in range(0,num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            old_set.add(item)
            continue

        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            old_set.add(item)
            continue

        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            old_set.add(item)
            continue
        else:
            continue
    return old_set


def select_set(old_set,datatype, datarange):
    new_set = set()
    for x in old_set:
        if datatype is int:
            it = iter(datarange)
            if next(it) <= x <= next(it):
                new_set.add(x)
            continue

        elif datatype is float:
            it = iter(datarange)
            if next(it) <= x <= next(it):
                new_set.add(x)
            continue

        elif datatype is str:
            if x.find(datarange) != -1:
                new_set.add(x)
            continue
        else:
            continue
    return new_set


def apply():
    base_str = string.ascii_letters + string.digits + string.punctuation
    old_set = create_set(str, base_str, 10)
    print(old_set)
    new_set = select_set(old_set,str,'at')
    print(new_set)

apply()
