documents = ["This is the first document.", "Information retrieval is important.", "Search for keywords in documents."]

postings = {}
for docid in range(len(documents)):
    for word in documents[docid]:
        if(word in postings):
            postings[word].append(docid)
        else:
            postings[word]=[]
            postings[word].append(docid)
print(postings)