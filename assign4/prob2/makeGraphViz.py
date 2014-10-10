import tld #used to get the domain from a uri.  used as a label

def getLabel(link):
  try:
    return tld.get_tld(link, as_object=True).domain
  except:
    return link

with open("graph.gv", "w+") as fout:
  fout.write("digraph graphName {\n")

  for x in range(1,101):
      print x
      links = []
      with open('links/'+str(x), "r") as f:
          links = f.readlines()

      numNodes = len(links) - 3

      head = links[1].rstrip('\n')

      ctr = 3
      while (ctr < len(links)):
        link = links[ctr].rstrip('\n')
        fout.write("\t\"" + head + "\" -> \"" + link + "\"\n")
        fout.write("\t\"" + head + "\" [label=\"" + getLabel(head).rstrip('\n') + "\"];\n")
        fout.write("\t\"" + link + "\" [label=\"" + getLabel(links[ctr]).rstrip('\n') + "\"];\n")
        ctr = ctr+1


  fout.write("}")
