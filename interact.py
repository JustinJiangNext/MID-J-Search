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


download = input("Download Y/N (warning: large batches may result in IP ban): ")

if(download == "y" or download == 'Y'):
    searchMJ.downloadMidJourneyImages(searchResult, criterias)