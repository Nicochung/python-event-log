from helper import parseEventString, binarySearch, searchLog

# Test case for finding the tag and separating them
Q_1 = "I just won a lottery #update @all"  
A_1 = {'category': ['update'], 'person': ['all']}

Q_2 = "#Test #task is difficult"
A_2 = {'category': ['Test', 'task'], 'person': []}

Q_3 = "@team we have #race_condition in chat service, @John fyi"
A_3 = {'category': ['race_condition'], 'person': ['John', 'team']}

Q_4 = "I have no tag in this log"
A_4 = {'category': [], 'person': []}

assert parseEventString(Q_1) == A_1
assert parseEventString(Q_2) == A_2
assert parseEventString(Q_3) == A_3
assert parseEventString(Q_4) == A_4

# Test case for binarySearch
tempList = ["Alice", "Bob", "Cat"]
Q_1 = "Alice"
A_1 = True

Q_2 = "John"
A_2 = False

assert binarySearch(tempList, Q_1) == A_1
assert binarySearch(tempList, Q_2) == A_2
