#print(subs in documents[0])  #searching a substring in a document

#looping througth the document and retrieving its values and indices
# substring = "Is"
# for idx,item in enumerate(documents):
#     if substring.lower() in item.lower():
#         print(f'{idx}: {item}')
#
#
#
documents = ["This is the first document.", "Information retrieval is important.", "Search for keywords in documents."]
subs = "is"

def searchTxt(subst, doc):
    res = []
    for idx, item in enumerate(doc):
        if subst.lower() in item.lower():
            res.append((idx,item))
    return res

print(searchTxt(subs,documents))

searching = searchTxt(subs, documents)
if len(searching) > 0:
    print(f'the following document(s) satisfy the search query')
    for idx, doc in searchTxt(subs,documents):
        print(f'doc id :{idx} - {doc}')
else:
    print("oops document could not be found")
print()


