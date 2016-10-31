#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:48:18 2016

@author: karl
"""

import pandas as pd
import numpy as np
import timeit


quickSortArray100 = np.array(pd.read_csv('100.txt', header = None))
listQuickSortArray100 = [figure[0] for figure in quickSortArray100]

quickSortArray10 = np.array(pd.read_csv('10.txt', header = None))
listQuickSortArray10 = [figure[0] for figure in quickSortArray10]

listTest = [3,4,2,1,5]
listTest2 = [3,4,2,1,5]
listTest3 = [1,2,4,5,6,3]

##Quik sort using first element of array as pivot
def quickSort(listToSort):
    sizeList = len(listToSort)
    nbComparaison = 0
    if sizeList == 1:
        return listToSort, 0
    elif sizeList > 0:
        pivot = listToSort[0]
        i = 0
        j = 1
        while j < sizeList:
            if listToSort[j] < pivot:
                i += 1
                tmp = listToSort[i]
                listToSort[i] = listToSort[j]
                listToSort[j] = tmp
            j += 1 
        tmp = listToSort[i]
        listToSort[i] = pivot
        listToSort[0] = tmp
        if len(listToSort[:i]) > 0:
            listToSort[:i], nbComparaisonSs1 = quickSort(listToSort[:i])
            nbComparaison += len(listToSort[:i]) + nbComparaisonSs1
        if len(listToSort[i+1:]) > 0:
            listToSort[i+1:], nbComparaisonSs2 = quickSort(listToSort[i+1:])
            nbComparaison += len(listToSort[i+1:]) + nbComparaisonSs2
        return listToSort, nbComparaison

##Quik sort using last element of array as pivot
def quickSort2(listToSort):
    sizeList = len(listToSort)
    nbComparaison = 0
    if sizeList == 1:
        return listToSort, 0
    elif sizeList > 0:
        tmp = listToSort[-1]
        listToSort[-1] = listToSort[0]
        listToSort[0] = tmp
        pivot = listToSort[0]
        i = 0
        j = 1
        while j < sizeList:
            if listToSort[j] < pivot:
                i += 1
                tmp = listToSort[i]
                listToSort[i] = listToSort[j]
                listToSort[j] = tmp
            j += 1 
        tmp = listToSort[i]
        listToSort[i] = pivot
        listToSort[0] = tmp
        if len(listToSort[:i]) > 0:
            listToSort[:i], nbComparaisonSs1 = quickSort2(listToSort[:i])
            nbComparaison += len(listToSort[:i]) + nbComparaisonSs1
        if len(listToSort[i+1:]) > 0:
            listToSort[i+1:], nbComparaisonSs2 = quickSort2(listToSort[i+1:])
            nbComparaison += len(listToSort[i+1:]) + nbComparaisonSs2
        return listToSort, nbComparaison

##Quik sort using median element of array as pivot
def quickSort3(listToSort):
    sizeList = len(listToSort)
    nbComparaison = 0
    if sizeList == 1:
        return listToSort, 0
    elif sizeList > 0:
        listCandidat = []

        #odd case
        if (sizeList % 2 == 0):
            mid = (sizeList/2)-1
        #even case
        else: 
            mid = sizeList/2
        #low
        listCandidat.append(listToSort[0])
        #mid
        listCandidat.append(listToSort[mid])
        #high
        listCandidat.append(listToSort[-1])
        iMedian = np.argsort(listCandidat)[len(listCandidat)//2]
        if (iMedian == 0):
            tmp = listToSort[0]
            listToSort[0] = listToSort[0]
            listToSort[0] = tmp
        elif (iMedian == 1):
            tmp = listToSort[mid]
            listToSort[mid] = listToSort[0]
            listToSort[0] = tmp
        elif (iMedian == 2):
            tmp = listToSort[-1]
            listToSort[-1] = listToSort[0]
            listToSort[0] = tmp
        pivot = listToSort[0]
        i = 0
        j = 1
        while j < sizeList:
            if listToSort[j] < pivot:
                i += 1
                tmp = listToSort[i]
                listToSort[i] = listToSort[j]
                listToSort[j] = tmp
            j += 1 
        tmp = listToSort[i]
        listToSort[i] = pivot
        listToSort[0] = tmp
        if len(listToSort[:i]) > 0:
            listToSort[:i], nbComparaisonSs1 = quickSort3(listToSort[:i])
            nbComparaison = nbComparaison + (len(listToSort[:i]) + nbComparaisonSs1)
        if len(listToSort[i+1:]) > 0:
            listToSort[i+1:], nbComparaisonSs2 = quickSort3(listToSort[i+1:])
            nbComparaison = nbComparaison + (len(listToSort[i+1:]) + nbComparaisonSs2)
        return listToSort, nbComparaison
        
# Reading data, I'm sure there is a better way but it's just convenient here
quickSortArray = np.array(pd.read_csv('QuickSort.txt', header = None))
listQuickSortArray = [figure[0] for figure in quickSortArray]
A = quickSort(listQuickSortArray)[1]
quickSortArray = np.array(pd.read_csv('QuickSort.txt', header = None))
listQuickSortArray = [figure[0] for figure in quickSortArray]
B = quickSort2(listQuickSortArray)[1]
quickSortArray = np.array(pd.read_csv('QuickSort.txt', header = None))
listQuickSortArray = [figure[0] for figure in quickSortArray]
C = quickSort3(listQuickSortArray)[1]
