## Welcome to my GitHub page :)
### Here I will be showcasing important parts of my code, mainly from the PRAW and PsycoPG2 libraries and showing you how they work.
***

```python
import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     password=config.password,
                     username=config.username,
                     user_agent=config.user_agent)
```

This initialises what's known as **an instance of Reddit**, and is important because it is what allows the client to **connect to Reddit in more than just read-only mode**. Without this instance, the client will only be in read-only mode, limiting it to the viewing and data collecting of elements of Reddit. When calling functions to do with the bot account being active, **you must always pass in Reddit** in order for the client to realise it has the ability to login and do useful things. (Data collection is also incredibly useful but you know what I mean.)
