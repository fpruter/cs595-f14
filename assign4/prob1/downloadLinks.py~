import urllib2
import requests
from bs4 import BeautifulSoup

def testURI(link):
 try:
  if (len(link) == 0):
    return [False, ""]
  if (link[0].isalpha()):
    try:
      r = requests.head(link, allow_redirects=True)
      if r.status_code == 200:
          #print r.url
          return [True, r.url]
      return [False, ""]
    except requests.ConnectionError:
      return [False, ""]
  else:
    return [False, ""]
 except:
  return [False, ""]

with open('uris', 'r') as f:
    uriList=f.readlines()
            
fileNumber = 1


for uri in uriList:
  if (fileNumber == 101):
    break
  try:
      uri = testURI(uri)
      if (uri[0]):
         uri = uri[1]
      else:
         continue
      uriFile = urllib2.urlopen(uri)
      uriHTML = uriFile.read()
      uriFile.close()
  except Exception as e:
      print e
      continue

  soup = BeautifulSoup(uriHTML)
  linksList = []
  try:
      for links in soup.find_all('a'):
          uriLink = links.get('href')
          l = testURI(uriLink)
          #print l
          if (l[0]):
              if (l[1] not in linksList):
                  linksList.append(l[1])
          else:
              continue
  except Exception as e:
      print e
      continue


  if (len(linksList) == 0):
     continue
  with open('links/'+str(fileNumber), 'w') as fout:
      fout.write('Site:\n'+uri+'\nLinks:\n')
      for links in linksList:
       try:
         fout.write(links+'\n')
       except:
         print "error"
  print fileNumber
  fileNumber = fileNumber + 1

























