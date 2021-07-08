from pubmed_lookup import PubMedLookup
from pubmed_lookup import Publication

import requests



idlist=[]

with open("idcol") as f:
    for i in f:
        id=i.strip()

        if(id not in idlist):
            idlist.append(id)


print(idlist)
print(len(idlist))

print(idlist.index("17928686"))

R1A = idlist[:len(idlist)//2]
print(len(R1A))
A=R1A[:len(R1A)//2]
print(len(A))
B=R1A[len(R1A)//2:]
print(len(B))
R1B = idlist[len(idlist)//2:]
C=R1B[:len(R1B)//2]
print(len(C))
D=R1B[len(R1B)//2:]

print((D))
E=['3264152', '9559809', '10390233', '15326193', '9371686', '8504817', '15611104', '9671516', '16792995', '7213621', '11085979', '7350914', '15067523', '15850394', '12731879', '12568655', '1980064', '16567409', '16962986', '15752689']

email = 'xiang.zhou@vanderbilt.edu'
url=''

newidlist=[]
B.remove("18051592")
#D.remove("8910410")


for i in E:

    url = 'http://www.ncbi.nlm.nih.gov/pubmed/'+ str(i)
    print(i)

    lookup = PubMedLookup(url, email)
    publication = Publication(lookup)
    if "mechanism" in repr(publication.abstract):
        print(i)
        newidlist.append(i+"\n")
        print(
    """

    URL:\n{url}\n

    ABSTRACT:\n{abstract}\n
    """
    .format(**{
    'title': publication.title,
    'authors': publication.authors,
    'journal': publication.journal,
    'year': publication.year,
    'month': publication.month,
    'day': publication.day,
    'url': publication.url,
    'pubmed': publication.pubmed_url,
    'citation': publication.cite(),
    'mini_citation': publication.cite_mini(),
    'abstract': repr(publication.abstract),
    }))


newid=open("newid","r+")
newid.writelines(newidlist)
newid.close()
