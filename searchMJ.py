import os
import csv

RELATIVE_DATA_PATH: str = "MidjourneyCSV-Kaggle"
DATASET_NAME: str = "midjourney_2022_250k.csv"
DATAFILE_PATH = RELATIVE_DATA_PATH + "/" + DATASET_NAME

def COMPLETE_MIDJOURNEY_URL(id:str) -> str:
    return "https://cdn.midjourney.com/" + id + "/0_0.webp"


def downloadDataScript() -> None:
    os.system("chmod +x downloadData.sh")
    os.system("./downloadData.sh")

def matchSearch(strings_list:list, main_string:str) -> bool:   
    for substring in strings_list:
        if substring not in main_string:
            return False
    return True

def fetchURLs(searchCriteria:list, terms:int, csv_file:str = DATAFILE_PATH) -> list:
    searchResult:list = []
    DESCRIPTION_INDEX = 6
    IMAGE_URL_INDEX = 5
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if(len(searchResult) >= terms and terms > 0):
                break
            if(matchSearch(searchCriteria, row[DESCRIPTION_INDEX])):
                searchResult.append(COMPLETE_MIDJOURNEY_URL(row[IMAGE_URL_INDEX]))
    return searchResult




