# This is the repository of the attempting to build a Rest Client in Python

## Workflow

1. Identify the incoming string and extract the tags in the string
2. Construct the object with extracted tags and add timestamp
3. Append the object to a list

## Assumptions

1. Each word in the event string is separate by a space
2. All inputs are valid
3. There is enough memory to store all the logs in memory
4. Tags are case-sensitive
5. The log will be stored in the following format
   ```js
    {
        "timeStamp": "23/05/2022 10:50:02",
        "log": "I just won a lottery #update @all",
        "tagObj": {
            "category": [
                "update"
            ],
            "person": [
                "all"
            ]
        }
    },
   ```

### Note

- A "Tag" is the word followed by when the category symbol "#" or "@"
