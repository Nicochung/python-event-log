# This is the repository of the attempting to build a Rest Client in Python

## Workflow

1. Identify the incoming string and extract the tags in the string
2. Construct the object with extracted tags and add timestamp
3. Append the object to a list

## Assumptions

1. Each word in the event string is separate by a space
2. There is enough memory to store all the logs in memory
3. Tags are case-sensitive

### Note

- A "Tag" is the word followed by when the category symbol "#" or "@"
