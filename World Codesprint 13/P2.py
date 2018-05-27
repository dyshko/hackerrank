#!/bin/python3

import os
import sys

# Complete the membersInTheLargestGroups function below.
def membersInTheLargestGroups(n, m, a, b, f, s, t):
    grade = {}
    group_list = [[] for i in range(n)]
    group = {}
    size1 = {}
    size2 = {}
    size3 = {}
    
    names = []
    for i in range(n):
        name, g = input().split()
        g = int(g)
        grade[name] = g
        names.append(name)
        group_list[i] = [name]
        the_group = group_list[i]
        h = str(id(the_group))
        size1[h] = 1 if g == 1 else 0
        size2[h] = 1 if g == 2 else 0
        size3[h] = 1 if g == 3 else 0
        group[name] = the_group
    
    for _ in range(m):
        n1, n2 = input().split()
        
        group1 = group[n1]
        group2 = group[n2]
        
        if group1 == group2:
            continue
        
        h1 = str(id(group1))
        h2 = str(id(group2))
        if ( size1[h1] + size1[h2] <= f ) and \
           ( size2[h1] + size2[h2] <= s ) and \
           ( size3[h1] + size3[h2] <= t ) and \
           ( len(group1) + len(group2) <= b ):
                #merge
                size1[h1] += size1[h2]
                size2[h1] += size2[h2]
                size3[h1] += size3[h2]
                for _name in group2:
                    group[_name] = group1
                group1 += group2
                group2 = {}
        
        #print(n1,n2)
        #print(" ".join(str(id(group[name])) for name in names))
        #print(" ".join(str( size1[str(id(group[name]))] ) for name in names))
        
        
    maxgroupsize = max([len(gr) for gr in group_list])
    if maxgroupsize < a:
        print("no groups")
    else:
        res = []
        for gr in group_list:
            if len(gr) == maxgroupsize:
                res += gr
        res.sort()
        for name in res:
            print(name)
        
        
                
        
    
    
    # Print the names of the students in all largest groups or determine if there are no valid groups.

if __name__ == '__main__':
    nmabfst = input().split()

    n = int(nmabfst[0])

    m = int(nmabfst[1])

    a = int(nmabfst[2])

    b = int(nmabfst[3])

    f = int(nmabfst[4])

    s = int(nmabfst[5])

    t = int(nmabfst[6])

    membersInTheLargestGroups(n, m, a, b, f, s, t)