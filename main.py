from Bio import Entrez

from metapub import *
from metapub.pubmedcentral import *
from pubmed_lookup.test_pubmed_lookup import pmid
from pubmed_lookup import PubMedLookup

from pubmed_lookup import Publication
from metapub import FindIt
import metapub.convert
from metapub import UrlReverse


idlist=[]

with open("IDfinal") as f:
    for i in f:
        id=i.strip()
        if(id not in idlist):
            idlist.append(id)

idlist=idlist[400:]
print(idlist)
print(len(idlist))
#10.1186/s13568-014-0059-2
#IDfinal=open("IDfinal","r+")
#IDfinal.writelines(idlist)
#IDfinal.close()

from scidownl.scihub import *

#DOI = "10.1016/j.jmb.2004.10.035"
#out = 'paper'
#sci = SciHub(DOI, out).download(3)


#fetch = PubMedFetcher()

#urlrev = UrlReverse("https://link.springer.com/content/pdf/10.1007/s10529-010-0274-0.pdf")

#print(urlrev.doi)
email="xiang.zhou@vanderbilt.edu"
doilist=[]
for i in idlist:
    #src = FindIt(i)
    #print(src.url)
    print(i)
    url = 'http://www.ncbi.nlm.nih.gov/pubmed/' + str(i)
    lookup = PubMedLookup(url, email)
    publication = Publication(lookup)
    newurl = publication.url
    a=get_doi_for_otherid(i)
    #if (a!=None) and (a!="") and a!="10.1074/jbc.M113.540542" and a!="10.1021/bi801879z":
    try:
        print(a)
        DOI = a
        out = 'paper'
        sci = SciHub(DOI, out).download(3)
        doilist.append(a)
    except:
    #else:
       #try:
        a=metapub.convert.pmid2doi(i)
        print(a)

        DOI = a
        out = 'paper'
        sci = SciHub(DOI, out).download(3)
        doilist.append(a)
      # except:
       #    if newurl != None:
       #        urlrev = UrlReverse(newurl)
       #        a = urlrev.doi
       #        print(a)
       #        DOI = a
       #        out = 'paper'
       #        sci = SciHub(DOI, out).download(3)
       #        doilist.append(a)



print(doilist)
