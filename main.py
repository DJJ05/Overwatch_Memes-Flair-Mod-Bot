#Moderation Bot (Overwatch_Memes)

import praw
import prawcore
import psycopg2

'''

+———————————————————————————————————————+

MANDATORY CREDIT STATEMENTS PROVIDED
UNDER THE GNU GENERAL PUBLIC LICENSE

+———————————————————————————————————————+

ALL OF THE FOLLOWING CODE WAS ORIGINALLY
MADE BY U/DEVILJAMJAR ON REDDIT AND
DEVILJAMJAR ON GITHUB.

THIS BOT WAS MADE FOR R/OVERWATCH_MEMES
AND WAS MADE OPEN SOURCE.

IF YOU INTEND TO USE THIS CODE THEN YOU
MUST LEAVE THIS CREDIT SECTION INTACT AND
LIST ALL CHANGES YOU MAY MAKE IN THE
SECTION BELOW, AS SHOWN BY THE GNU GENERAL
PUBLIC LICENSE TERMS.

+———————————————————————————————————————+

CHANGES MADE :

- EXAMPLE CHANGE

- EXAMPLE CHANGE

- EXAMPLE CHANGE

+———————————————————————————————————————+

'''


# Login Procedure


reddit = praw.Reddit(client_id='**********',
                    client_secret='*****************',
                    password='*******************',
                    username='Overwatch_MemesBot',
                    user_agent='Overwatch Moderation Bot by u/DevilJamJar')


subreddit = reddit.subreddit('Overwatch_Memes')

print('Starting Comment Bot')

def updateTable(ModName, FlairRemovals):
    try:
        connection = psycopg2.connect(user="*********",
                                      password="******",
                                      host="***********",
                                      port="***********",
                                      database="************")

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from "ModStats" where "Mod_Name" = %s"""
        cursor.execute(sql_select_query, (ModName, ))
        record = cursor.fetchone()
        print(record)

        if record is not None:
            current_flair_removals = record[1]
            FlairRemovals = FlairRemovals + current_flair_removals

        else:
            FlairRemovals = 1

        # Update single record now
        sql_update_query = """Update "ModStats" set "Flair_Removals" = %s where "Mod_Name" = %s"""
        cursor.execute(sql_update_query, (FlairRemovals, ModName))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from "ModStats" where "Mod_Name" = %s"""
        cursor.execute(sql_select_query, (ModName,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def flair_mod_stream(reddit, iteration=1):
    print('flair mod stream started')

    try:
        for flair_edit in subreddit.mod.stream.log(action='editflair', skip_existing=True):
            check_flair = True

            # skip non-submission flair edits
            if not flair_edit.target_fullname.startswith('t3_'):
                check_flair = False

            if check_flair:
                flair_edit_submission = reddit.submission(flair_edit.target_fullname.lstrip('t3_'))

                if hasattr(flair_edit_submission, 'link_flair_template_id'):
                    flair_id = flair_edit_submission.link_flair_template_id
                    remove = False

                    if flair_id == '952ed81e-cdaa-11e9-afbf-0ebcf4122044':
                        # rule 1: not overwatch related
                        remove = True
                        removal_reason = ('''Thank you for submitting content,  
But your post has been removed for the following reason(s):
- [Rule 1: ](https://www.reddit.com/r/Overwatch_Memes/about/rules/) The Post is not Overwatch Related 

If you feel this was an Error please [contact the mods via Modmail](https://www.reddit.com/message/compose?to=%2Fr%2FOverwatch_Memes).''')
                    if flair_id == 'e555b9e0-7f0f-11ea-b86d-0ece6f022e4f':
                        # rule 2: not respecting of others
                        remove = True
                        removal_reason = ('''Thank you for submitting content,  
But your post has been removed for the following reason(s):
- [Rule 2: ](https://www.reddit.com/r/Overwatch_Memes/about/rules/) No insulting, harrassing, racism, sexism, etc. We do not tolerate this type of behaviour here. In general, just follow Reddiquette.

If you feel this was an Error please [contact the mods via Modmail](https://www.reddit.com/message/compose?to=%2Fr%2FOverwatch_Memes).''')
                    if flair_id == '9aea2056-cdaa-11e9-a391-0ebe0c91506c':
                        # rule 3: not a direct link
                        remove = True
                        removal_reason = ('''Thank you for submitting content,  
But your post has been removed for the following reason(s):
- [Rule 3](https://www.reddit.com/r/Overwatch_Memes/about/rules/): Direct Links Only

If you feel this was an Error please [contact the mods via Modmail](https://www.reddit.com/message/compose?to=%2Fr%2FOverwatch_Memes).''')
                    if flair_id == 'efec34de-90ad-11e9-a4ea-0e4e852142da':
                        # rule 4: no overly sexual content
                        remove = True
                        removal_reason = ('''Thank you for submitting content,  
But your post has been removed for the following reason(s):
- [Rule 4: ](https://www.reddit.com/r/Overwatch_Memes/about/rules/) No NSFW or Gross content

If you feel this was an Error please [contact the mods via Modmail](https://www.reddit.com/message/compose?to=%2Fr%2FOverwatch_Memes).''')
                    if flair_id == 'f5c8af7c-90ad-11e9-b737-0eecc98b8520':
                        # rule 5: no reposts
                        remove = True
                        removal_reason = ('''Thank you for submitting content,  
But your post has been removed for the following reason(s):
- [Rule 5: ](https://www.reddit.com/r/Overwatch_Memes/about/rules/) No Reposts

If you feel this was an Error please [contact the mods via Modmail](https://www.reddit.com/message/compose?to=%2Fr%2FOverwatch_Memes).''')
                    if flair_id == 'fc401322-90ad-11e9-933c-0e09e79daed4':
                        # rule 6: no gameplay videos
                        remove = True
                        removal_reason = ('''Thank you for submitting content,  
But your post has been removed for the following reason(s):
- [Rule 6: ](https://www.reddit.com/r/Overwatch_Memes/about/rules/) No Gameplay Videos

If you feel this was an Error please [contact the mods via Modmail](https://www.reddit.com/message/compose?to=%2Fr%2FOverwatch_Memes).''')
                    if flair_id == 'd2b9df32-90ae-11e9-b456-0e1f4d9a4418':
                        #rule 7: no title memes
                        remove = True
                        removal_reason = ('''Thank you for submitting content,  
But your post has been removed for the following reason(s):
- [Rule 7: ](https://www.reddit.com/r/Overwatch_Memes/about/rules/) No "Title Memes"

If you feel this was an Error please [contact the mods via Modmail](https://www.reddit.com/message/compose?to=%2Fr%2FOverwatch_Memes).''')
                    if flair_id == '5fbcf2ea-ad2c-11e9-bca5-0eb90f2fb4a6':
                        # rule 1: not a meme
                        remove = True
                        removal_reason = ('''Thank you for submitting content,  
But your post has been removed for the following reason(s):
- [Rule 1: ](https://www.reddit.com/r/Overwatch_Memes/about/rules/) Post not a Meme

If you feel this was an Error please [contact the mods via Modmail](https://www.reddit.com/message/compose?to=%2Fr%2FOverwatch_Memes).''')

                    if remove:

                        # remove the submission and leave a comment
                        removal_comment = flair_edit_submission.reply(removal_reason)

                        removal_comment.mod.distinguish(how='yes', sticky=True)
                        removal_comment.mod.lock()

                        flair_edit_submission.mod.remove()
                        flair_edit_submission.mod.lock()

                        print(f'submission by u/{flair_edit_submission.author} removed by u/{flair_edit._mod} via flair.')

                        ModName = str(flair_edit._mod.lower())
                        print(f'set sql search query to {ModName}')

                        updateTable(ModName, 1)

            else:
                print('flair_edit response skipped')

    except prawcore.exceptions.ServerError as error:
        print(f'skipping flair_edit due to PRAW error: {type(error)}: {error}')

    except prawcore.exceptions.ResponseException as error:
        print(f'skipping flair_edit due to PRAW error: {type(error)}: {error}')

    iteration += 1

    if iteration <= 10:
        flair_mod_stream(reddit, iteration)

    else:
        print('killing flair mod stream, >10 skipped logs')

flair_mod_stream(reddit)
