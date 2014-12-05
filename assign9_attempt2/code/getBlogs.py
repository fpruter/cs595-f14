#!/usr/bin/python
import requests

next_blog = "https://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"

ATOMlink = "/feeds/posts/default"

blogs=[]

blogs.append("http://f-measure.blogspot.com/")
blogs.append("http://ws-dl.blogspot.com/")

#get 100 unique blogs
while len(blogs) < 100:
    try:
      #verify blog URI still works
      r = requests.get(next_blog)
      if r.status_code == 200:
        if not r.url in blogs:
          blogs.append(r.url[:len(r.url)-17])
          print len(blogs)
    except requests.ConnectionError:
      pass

with open("blogURI", "w+") as fout:
    for uri in blogs:
      fout.write(uri+'\n')




















