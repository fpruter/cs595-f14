#!/usr/bin/env python

"""
Data file from:
http://igraph.org/python/doc/tutorial/tutorial.html
http://vlado.fmf.uni-lj.si/pub/networks/data/ucinet/zachary.dat

Reference:
numpy():
http://stackoverflow.com/questions/11905899/how-to-import-a-matrix-from-a-text-file-in-python

"""

from igraph import *
import numpy

karate = Graph.Read_GraphML("karate.GraphML")

layout=karate.layout('kk')
karate.vs["label"] = karate.vs["name"]

with open("graph.json", "w") as f:
  f.write('{\n')
  f.write(' "nodes": [\n')

  for x in range(0,33):
    f.write('  {\n')
    f.write('   "Faction": ' + str(karate.vs['Faction'][x]) + ', ')
    f.write('   "id": "' + str(karate.vs['id'][x]) + '", ')
    f.write('   "name": "' + str(karate.vs['name'][x]) + '"')
    f.write('  },\n')

  f.write('  {\n')
  f.write('   "Faction": ' + str(karate.vs['Faction'][x]) + ', ')
  f.write('   "id": "' + str(karate.vs['id'][x]) + '", ')
  f.write('   "name": "' + str(karate.vs['name'][x]) + '"\n')
  f.write('  }\n')
  f.write(' ],\n')
  f.write(' "links": [\n')

  weight = numpy.loadtxt("karatematrix.dat")

  xloc = 0  
  for x in weight:
    yloc = 0
    for y in x:
      if (y == 0):
        yloc = yloc+1
        continue
      
      f.write('  {\n')
      f.write('   "source": ' + str(xloc) + ', ')
      f.write('   "target": ' + str(yloc) + ', ')
      f.write('   "weight": ' + str(y) + ',\n')
      f.write('  },\n')
      yloc = yloc+1
    xloc = xloc+1
  f.write(' ]\n}')
























  
