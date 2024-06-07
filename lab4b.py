#!/usr/bin/env python3

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    tmp_set = set(l1) | set(l2)
    joined = list(tmp_set)
    return joined

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    tmp_set = set(l1) & set(l2)
    matched = list(tmp_set)
    return matched

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    tmp_set1 = set(l1) - set(l2)
    tmp_set2 = set(l2) - set(l1)
    tmp_set3 = tmp_set1 | tmp_set2
    diffed = list(tmp_set3)
    return diffed

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))