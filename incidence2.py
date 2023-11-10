documents = ["This is the first document.", "Information retrieval is important.", "Search for keywords in documents."]

#1 Get all words
words = []
for idx, item in enumerate(documents):
    words += item.lower().split()
print(words)

#2. Initialize term incidedence matrix for each word as a matrix of zeros
termIncidence = {}
for word in words:
    termIncidence[word]= [0 for i in range(len(documents))]
print(termIncidence)

#Step 3: fill the term incidence matrix
#(extract a key in term index and search for its occurence in the documents)
#If the word is available we put one]

for key in termIncidence:
    for i in range(len(documents)):
        if(key in documents[i].lower()):
            termIncidence[key][i] = 1
print(termIncidence)


def searchWord(word):
    if word in termIncidence:
        return termIncidence[word]
    else:
        for key in termIncidence:
            if word in key:
                return termIncidence[key]

        return [0 for i in range(len(documents))]
print(searchWord('document'))

searchtext = "information document"
searchtextp = searchtext.lower().split() #splitting word and getting their index matrix
results = []
for word in searchtextp:
    results.append(searchWord(word)) ##adding incidence matrix to results array
print(results)


finalResult = []
temp = results[0]
for it in range(1,len(results)):
    temp = [1 if (temp[i]== 1 and results[it][i] == 1) else 0 for  i in range(len(documents))]
print(temp)

for i in range(len(temp)):
    if(temp[i]==1):
        print("The following document satifiesy your query:")
        print(documents[i])