# Welcome to my GitHub page :)
## Here I will be showcasing important parts of my code, mainly from the PRAW and PsycoPG2 libraries and showing you how they work.
***

### Initialising a Reddit instance

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

***

### Storing and using the Subreddit variable

```python
subreddit = reddit.subreddit(config.subreddit)
```

Whenever you want to use certain actions like `subreddit.mod.stream.log()` **you must always include your subreddit in the `subreddit` section of that string.** If you do not store it like that, then whenever you want to use that function, you will have to use `reddit.subreddit(config.subreddit).mod.stream.log()` **which is annoying, increases the chances of making mistakes and looks like complete garbage.** Instead, the rule of thumb is to **store it in the `subreddit` variable.**
