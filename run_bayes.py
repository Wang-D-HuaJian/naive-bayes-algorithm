import sys
sys.path.append("F:/pythonTest")
from naive_bayes.bayes import *
import feedparser

#listOPosts, listClasses = loadDataSet()
#myVocabList = createVocabList(listOPosts)
#print(myVocabList)
#print(listOPosts[0])
#result1 = setOfWords2Vec(myVocabList, listOPosts[0])
#print(result1)
#trainMat=[]
#for postinDoc in listOPosts:
#    trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
#p0V,p1V,pAb = trainNB0(trainMat, listClasses)
#print(pAb)
#print(p0V)
#print(p1V)
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')

#vocabList,pSF,pNY = localWords(ny, sf)
getTopWords(ny, sf)


