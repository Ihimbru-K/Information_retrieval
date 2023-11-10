documents = ["This is the first document.", "Information retrieval is important.", "Search for keywords in documents."]

postings = {}
for docid in range(len(documents)):
    for word in documents[docid].lower().split():
        if(word in postings):
            postings[word].append(docid)
        else:
            postings[word]=[]
            postings[word].append(docid)
print(postings)


def searchPosting(searchwords):
    results = []
    for word in searchwords.lower().split():
        if word in postings:
            results.append(postings[word])
        else:
            for key in postings:
                if word in key:
                    results.append(postings[key])
        return results
sword = 'for documents'
results = searchPosting(sword)

final_results =  results[0]
print('results', results)
for i in range(1,len(results)):
    final_results = set(final_results).intersection(results)
print(final_results)

if final_results:
    print("The following are the results that satisfy our query")
    for docid in final_results:
        print(f'docid:{docid} - {documents[docid]}')