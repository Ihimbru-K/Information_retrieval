documents = ["This is the first document.", "Information retrieval is important.", "Search for keywords in documents."]

dict = {}
for idx, item in enumerate(documents):
    dict[idx] = item.lower().split()
print(dict)

termIncidence = {}
keys = []
for key, item in dict.items():
    for word in item:
        keys.append(word)
print(keys)