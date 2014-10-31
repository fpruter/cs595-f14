#!/usr/bin/env python

"""
Data file from:
http://igraph.org/python/doc/tutorial/tutorial.html

Reference:
as_clustering():
    http://stackoverflow.com/questions/22046499/community-detection-with-igraph-in-python

"""

from igraph import *

karate = Graph.Read_GraphML("karate.GraphML")

layout=karate.layout('kk')
karate.vs["label"] = karate.vs["name"]


karate_actual_MrHi = []
karate_actual_John = []


#Community Edge Betweenness cluster=2
karate_ceb = karate.community_edge_betweenness(clusters=2, directed=False, weights=karate.es["weight"]).as_clustering()

#Community Edge Betweenness cluster=3
karate_ceb3 = karate.community_edge_betweenness(clusters=3, directed=False, weights=karate.es["weight"]).as_clustering()

#Community Edge Betweenness cluster=4
karate_ceb4 = karate.community_edge_betweenness(clusters=4, directed=False, weights=karate.es["weight"]).as_clustering()

#Community Edge Betweenness cluster=5
karate_ceb5 = karate.community_edge_betweenness(clusters=5, directed=False, weights=karate.es["weight"]).as_clustering()

for x in range(0,34):
  if (karate.vs[x]["Faction"] == 1.0):
     karate_actual_MrHi.append(x)
  if (karate.vs[x]["Faction"] == 2.0):
     karate_actual_John.append(x)


#Initial
plot(karate, "graphs/beforesplit.pdf", layout = layout, margin = 20)

#Community Edge Betweenness
plot(karate_ceb, "graphs/predictedsplit.pdf", layout = layout, margin = 20)

#Community Edge Betweenness, cluster = 3
plot(karate_ceb3, "graphs/predictedsplit3.pdf", layout = layout, margin = 20)

#Community Edge Betweenness, cluster = 4
plot(karate_ceb4, "graphs/predictedsplit4.pdf", layout = layout, margin = 20)

#Community Edge Betweenness, cluster = 5
plot(karate_ceb5, "graphs/predictedsplit5.pdf", layout = layout, margin = 20)


#accuracy  
diff = list(set(karate_actual_MrHi) - set(karate_ceb[0])) + list(set(karate_ceb[0]) - set(karate_actual_MrHi))

diff.sort()

accuracy = round(((34-len(diff))/34.0)*100, 1)

print "Actual Mr. Hi:\t", karate_actual_MrHi
print "Predic Mr. Hi:\t", karate_ceb[0]


print "Actual John:\t", karate_actual_John
print "Predic John:\t", karate_ceb[1]
print "\nDifference:\t", diff
print "Accuracy: \t",  accuracy


