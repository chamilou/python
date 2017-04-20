'''
Created on 19 Dec 2016

@author: shamil
'''
def count(input, output):
    n=0
    for i in (input):
        print(n,i)
        n+=1
        if i == output:
            print(n)
    return n
count("mhgh","mhah")
    