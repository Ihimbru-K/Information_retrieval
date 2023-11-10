import os

def search_files(folder_path, keyword):
    matches = []
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root,file) #list of files in the directory
                with open(file_path, 'r') as f:
                    content = f.read()
                    if keyword in content:
                        matches.append(file_path)
        return matches


folder_path = r'C:\Users\IHIMBRU\Desktop\search'
keyword = input("Enter keyword to search")

results = search_files(folder_path,keyword)

if len(results) >0:
    print("Matching file")
    for file_path in results:
        print(file_path)

else:
    print("No matching files found")
