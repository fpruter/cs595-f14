# tfidfScore.py
# Author: Francis Pruter
#
# This python script processes the output of the queryTerm bash script
#  and calculated the TFIDF, TF, and IDF for each URI that was found
#  

from decimal import *
from operator import itemgetter #used to sort list of lists
import math

PRECISION=3

#This function computes and returns the IDF
# IDF is log2(total docs in corpus / docs with term)
def computeIDF(f):
  numFoundPages = fin.readline()
  numFoundPages = numFoundPages.rstrip('\n').split('\t')[1]

  numGooglePages = fin.readline()
  numGooglePages = numGooglePages.rstrip('\n').split('\t')[1]

  return math.log( Decimal(numGooglePages)/Decimal(numFoundPages), 2 )

# This function computers and returns the TF
#  TF is occurrence in doc / words in doc
def computeTF(x):
  return float(x[2])/float(x[1])

#used to output the array in tfidfScore.dat
def displayTen(array):
  with open('tfidfScore.dat', 'w+') as fout:
    fout.write( "TFIDF\tTF\tIDF\tURI\n" )
    fout.write( "-----\t--\t---\t---\n" )

    ctr = 0
    for x in array:
      if (ctr < 10):
         fout.write( str(x[0]) + "\t" + str(x[1])  + "\t" + str(x[2]) + "\t" +x[3])
         ctr = ctr+1

#This function returns the URI based on the num requested
def getURI(num):
  with open('uniqueURI', 'r') as fURI:
    x = fURI.readlines()
    num = num -1
    return x[num]
      


#Main body of the program
with open('pageRank.dat', 'r') as fin:
  tfidfArray = []
  IDF = round(computeIDF(fin),5)
  
  

  fin.readline() #read next line of headers

  for x in fin:
    x=x.rstrip('\n').split('\t')
    TF = round(computeTF(x), PRECISION)

    TFIDF = round((TF*IDF), PRECISION)
    tfidfArray.append([ TFIDF, TF, IDF, getURI(int(x[0])) ])


  tfidfArray=sorted(tfidfArray, key= itemgetter(0), reverse=True)
  
  displayTen(tfidfArray)


    

































