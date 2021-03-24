# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:51:27 2021

@author: Hyeungsuk Kim
"""
def selection(arr):
    for i in range(len(arr)-1):
        min_i = i

        for j in range(i+1,len(arr)):
            
            if arr[j] < arr[min_i]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i] , arr[i] 

    return arr

