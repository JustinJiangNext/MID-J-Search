import searchMJ

print("Midjourney search")
searchMJ.downloadDataScript()
criterias = input("terms(seperate by space) ")
limitSearch:int = 0
try:
    limitSearch = int(input("max URLs to return, type N for no restrictions "))
except:
    limitSearch = -1

searchResult = searchMJ.fetchURLs(criterias.split(' '), limitSearch)

for url in searchResult:
    print(url)