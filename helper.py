from typing import Tuple
import time

def categorizeTag(word: str) -> tuple:
    # Remove case where there is only a symbol # or @ in the word
    if len(word) <= 1:
        return [None, word]
    if word.find('#') == 0:
        return ['category', word[1:]]
    if word.find('@') == 0:
        return ['person', word[1:]]
    return [None, word]
        
def parseEventString(eventString: str) ->  dict:
    wordList = eventString.split(" ")
    tagObj = {'category': [], 'person': []}
    for word in wordList:
        tag = categorizeTag(word)
        # Dont have tag
        if tag[0] is None:
            continue
        tagObj[tag[0]].append(tag[1])
    tagObj['category'].sort()
    tagObj['person'].sort()
    return tagObj

def binarySearch(targetList, target:str) -> bool:
    start = 0
    end = len(targetList) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if targetList[mid] == target:
            return True
        if targetList[mid] > target:
            # Search Left
            end = mid - 1
        else:
            # Search Right
            start = mid + 1
    return False

def searchLog(category: str, tag:str, logList: list) -> list:
    eventList = []
    eventCnt = 0
    if category == 'time':
        return logList[-10:]
    if category == 'category' or category == 'person':
        for log in reversed(logList):
            if eventCnt >= 10:
                break
            if binarySearch(log['tagObj'][category], tag):
                eventCnt = eventCnt + 1
                eventList.append(log)
    return eventList
    