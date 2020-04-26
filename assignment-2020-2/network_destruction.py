import pprint
import argparse
from collections import deque
import sys

class Coronavirus:
    g = {}
    theInput = sys.argv[4]
    def ready(c):
        with open(theInput) as ginput:
            for line in ginput:
                n = [int(x) for x in line.split()]
                if len(nodes) != 2:
                    continue
                if n[0] not in g:
                    g[n[0]] = []
                if n[1] not in g:
                    g[n[1]] = []
                g[n[0]].append(n[1])
                g[no[1]].append(n[0])
        pprint.pprint(g)
     def search():
        dek = deque()
        visit = len() * [False]
        line = len() * [False]
        
   

        
