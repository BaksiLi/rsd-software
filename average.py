#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Brusli and Baksi


def average(list_of_lists):
    """Averages the lists from a list.

    Args:
        list_of_lists: [[x,y],[i,j]].

    Return:
        A list of averages.
    """
    return [sum(x) / len(x) for x in list_of_lists]


# print(average([[1,2],[3,1]]))
