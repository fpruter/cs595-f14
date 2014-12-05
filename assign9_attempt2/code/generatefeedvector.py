#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import re
import requests
from collections import OrderedDict


def getwordcounts(url):
  '''
  Returns title and dictionary of word counts for an RSS feed
<link rel='next' type='application/atom+xml' href='http://www.blogger.com/feeds/8028607259735637511/posts/default?start-index=26&amp;max-results=25'/>
  '''
  wc = {}
  next = True
  pagecount = 0
  
#continue until there are no next page
  while next:
    pagecount+=1
    next = False
    # Parse the feed
    d = feedparser.parse(url)
    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        # Extract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

#look for next page
    for link in  d['feed']['links']:
      if link['rel'] == 'next':
        url = link['href']
        #print url
        next = True

  return (d.feed.title, wc, pagecount)


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


ATOMlink = "/feeds/posts/default"

apcount = {}
wordcounts = {}
pagecount = []

ctr=0
feedlist = [line for line in file('blogURI')]
for feedurl in feedlist:
    ctr = ctr+1
    print ctr
    try:
        (title, wc, pc) = getwordcounts(feedurl.strip('\n')+ATOMlink)

        pagecount.append(pc)

        wordcounts[title] = wc
        for (word, count) in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
    except:
        print 'Failed to parse feed %s' % feedurl

wordlist = []

#for (w, bc) in apcount.items():
#    frac = float(bc) / len(feedlist)
#    if frac > 0.1 and frac < 0.5:
#        wordlist.append(w)

for w, bc in sorted(apcount.items(), key=lambda kv: kv[1], reverse=True):
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.5 and len(wordlist) < 500:
        wordlist.append(w)



out = file('blogdata1.txt', 'w+')
out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word.encode('utf-8'))
out.write('\n')
for (blog, wc) in wordcounts.items():
    print blog.encode('utf-8')
    out.write(blog.encode('utf-8'))
    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')

out.close()

with open('numpages', 'w+') as fout:
  for pc in pagecount:
    fout.write(str(pc) + '\n')

