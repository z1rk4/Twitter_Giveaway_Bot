# Twitter Giveaway Bot

A Twitter bot that can enter thousands of giveaways daily, interact accordingly based on the tweet's instructions, 

## Getting Started

This will just take a few minutes to install.

### Prerequisites

Things you need to have installed in order to be able to run the script.

```
Python 3.7
numpy
tweepy
```
###Installation
Install Python 3.7 from here: [download](https://www.python.org/downloads/). Then, run these two commands in a terminal or command shell:
```
pip install tweepy
pip install numpy
```
You should also download both scripts: ``main.py`` and ``config.py``. Preferably, put them in the same folder.

Once there, open the ``config.py`` file with a text editor; don't run it!
This file has all the variables the main script will use. Give each one of them the values you want, or just leave them by default.

#### Twitter App
This is meant to be a short guide on how to get the twitter credentials your bot will need. Here I assume you already have Twitter account, if you don't please make one now. 
##### Steps: 
* Enter to [Twitter Apps](https://apps.twitter.com/) and click the `Create New App` button
* Fill out all details and create the app
* Enter to the ``Keys and Access Token`` section and create a new access token. 
* Now copy ``Consumer Key``, ``Consumer Secret``, ``Access Token``, ``Access Token Secret`` and paste them into their right place inside
the ``config.py``'s ``access_tokens`` variable under the appropriate username. You can do this for as many usernames as you want.

If you've followed the steps correctly, now to start the bot you just need to run the ``main.py`` script. **Experiment with the variables at your own risk.**

### Setting up the ```config.py``` file

### How it works
This script uses Tweepy to automatically search through tweets that match a specified keyword. The bot then filters out irrelevant tweets, then processes each tweet to look for tags within the tweet for it to perform the appropriate action.

For example, if a tweet contained the tag *retweet*, then the bot will retweet the tweet from your account.
If the tweet asked for you to tag two friends, the bot will reply with two users to tag from the users specified in the ```config.py``` file.

After every iteration, to ensure that the account does not get ratelimited by Twitter, the bot sleeps for 150 seconds (can be modified on the user's own risk) before combing through another set of tweets. This process is repeated until the user stops the program. Information about interactions by the bot using the account are printed out in the console after every iteration.
