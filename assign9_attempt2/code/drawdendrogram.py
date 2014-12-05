#!/usr/bin/python

import clusters
blognames, words, data = clusters.readfile('blogdata1.txt')
clust=clusters.hcluster(data)

#Question 2
clusters.printclust(clust, labels=blognames)
clusters.drawdendrogram(clust, blognames, jpeg='dengrogram.jpg')



#Question 3
print "K = 5"
kclust5 = clusters.kcluster(data, k=5)
print "\nK = 10"
kclust10 = clusters.kcluster(data, k=10)
print "\nK = 20"
kclust20 = clusters.kcluster(data, k=20)



#Question 4

coords=clusters.scaledown(data)
clusters.draw2d(coords, blognames, jpeg='MDS.jpg')

