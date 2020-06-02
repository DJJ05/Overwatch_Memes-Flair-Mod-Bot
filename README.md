# Overwatch_Memes-Flair-Mod-Bot

## What is this?

This is the official moderation bot made especially for [/r/Overwatch_Memes](https://www.reddit.com/r/overwatch_memes) by me ([/u/DevilJamJar](https://www.reddit.com/u/DevilJamJar)).

This bot’s purpose is to react to flair changes by removing, locking and leaving a removal reason on them. It helps to make moderating much easier for mobile users and desktop users without access to toolbox. If you have any more questions, feel free to ask here or via my Reddit which is linked above.

## VERY IMPORTANT DISCLAIMER

This repository is licensed under the GNU General Public License v3.0. This is one of the most common licenses that is known for the freedom it provides the forker of the repo. However, contrary to common belief, there are a lot more terms to this agreement than you may think, [as demonstrated in this screenshot](https://i.imgur.com/WH7Ieir.jpg).

As you can see, I am happy for you to use my repo as long as you leave in the pre-built comment and print statement that gives me full credit for the script, as well as crediting me wherever you upload or share it. You also must state in the final script and to wherever you upload it the changes that you made, which effectively means you must either leave in my credit comment or remove it and tell people you removed it... your choice.

You must also use the same license that I used in any future uploads you make, which includes making everybody who uses your updated version credit me as the creator.

## How can I use this?

To use this repo exactly how it is intended to be used, you will need a Reddit account that you will create a personal use script on, a subreddit of which this account is a moderator on and a PostgreSQL server running the version specified in requirements.txt, alongside a database with a table set up with the same ModStats fields as are listed in main.py and a pip3 installation of the SQL module for ease of access when starting your database.

You will need to change all the variables in main.py with your own, as should be pretty obvious to you if you have decided to get this far. The IDs of the flairs can be accessed through the flairs list that is viewable to mods. IDs should be listed there. Client secret and ID are listed in your personal use script settings page, and the SQL server settings correspond with the running instance of your PostgreSQL server. If you are running this locally, then you can fill the host variable with 'localhost' and the port as the default.

If you encounter any errors from this point on, please feel free to DM on Reddit with the link above :)
