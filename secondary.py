import praw
import psycopg2
import config

# Login Procedure

reddit = praw.Reddit(client_id=config.client_id,
                    client_secret=config.client_secret,
                    password=config.password,
                    username=config.username,
                    user_agent=config.user_agent)


subreddit = reddit.subreddit(config.subreddit)

print('Starting Comment Bot (regulars)')

def updateTableRemovals(removalModsName, RegularsRemovals):
    try:
        connection = psycopg2.connect(user=config.sql_username,
                                      password=config.sql_password,
                                      host=config.sql_hostname,
                                      port=config.sql_port,
                                      database=config.sql_database)

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from "ModStats" where "Mod_Name" = %s"""
        cursor.execute(sql_select_query, (removalModsName, ))
        record = cursor.fetchone()
        print(record)

        if record is not None:
            current_regular_removals = record[2]
            RegularsRemovals = RegularsRemovals + current_regular_removals

        else:
            RegularsRemovals = 1

        # Update single record now
        sql_update_query = """Update "ModStats" set "Regular_Removals" = %s where "Mod_Name" = %s"""
        cursor.execute(sql_update_query, (RegularsRemovals, removalModsName))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from "ModStats" where "Mod_Name" = %s"""
        cursor.execute(sql_select_query, (removalModsName,))
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

def countremovals(reddit):

    for postremoval in subreddit.mod.stream.log(action='removelink', skip_existing=True):

        removalModName = str(postremoval._mod.lower())

        if removalModName == config.username:
            print(f'skipping SQL query because name regular = {removalModName}')

        else:
            print(f'running SQL query with name regular {removalModName}')
            updateTableRemovals(removalModName, RegularRemovals)

countremovals(reddit)
