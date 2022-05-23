from datetime import datetime
import json
from helper import parseEventString, searchLog

INIT_FROM_FILE = True
WRITE_TO_FILE_WHEN_EXIT = True
CATEGORIES = ['time', 'category', 'person']

def main():
    logList = []
    if INIT_FROM_FILE:
        with open('init.txt', 'r') as f:
            data = json.load(f)
            logList = data
    command = input("Enter the event string or 'search' to search or 'exit' to exit\n")
    while command != "exit":
        if command == 'search':
            searchResult = None
            cat = input("Enter the search category, (time/category/person)\n")
            if cat not in CATEGORIES:
                print('Invalid category')
                continue
            if cat == 'time': 
                searchResult = searchLog(cat, None, logList)
            if cat == 'category' or cat == 'person':
                tag = input("Enter the tag\n")
                searchResult = searchLog(cat, tag, logList)
            print(searchResult)
        else:
            tagObj = parseEventString(command)
            logObj = {}
            logObj['timeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            logObj['log'] = command
            logObj['tagObj'] = tagObj
            logList.append(logObj)
            print(f"Event \"{command}\" logged")
        command = input("Enter the event string or 'search' to search or 'exit' to exit\n")
    else:
        if WRITE_TO_FILE_WHEN_EXIT:
            with open('log.txt', 'w', encoding='utf-8') as f:
                json.dump(logList, f, ensure_ascii=False, indent=4)
        print("Exiting")

main()