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
Before starting up the bot, you have to initialize the ```config.py``` file with your information. Here is a step-by-step to set it up:

First, locate this block of code:
```
access_tokens = {
    "user1" : {
        'consumer_key' : '', 
        'consumer_secret' : '', 
        'access_token' : '', 
        'access_token_secret' : ''
    }...
 ```
Replace ```user1``` with your twitter username/handle (without the @). Then, paste the respective access tokens in each of the four values of the respective username. You can do this for as many usernames as you want to use. This way, when you start the program, you can specify which Twitter account you want the bot to run on, and have the bot running on multiple accounts simultaneously.

Next, locate this block of code:
```
# REQUIRED
# Users that you would like to tag in the giveaway. Add three users here.
tag_users = ["z1rk4", "user2", "user3"]
```
Replace each of the three strings with a Twitter account you want to tag (if the tweet requires you to tag someone) Only include three accounts here.

Finally, locate this block of code:
```
#REQUIRED
# Keywords that the bot will search for in tweets. Change/add as many as you want!
keywords = ["giveaway", "coding", "python"]
```
Replace each of the strings with keywords that you want the bot to look for when searching for new tweets. For example, if I wanted to look for tweets with the words "puppy," "dog," "cat," and "rabbit," I would put ```keywords = ["puppy", "dog", "cat", "rabbit"]```

You're all set! Further down the ```config.py``` file, you will see other information you can optionally provide if you would like to provide custom behavior.

In this block of code:
```
custom_replies = {
    "keyword1" : "reply1",
    "keyword2" : "reply2",
    "keyword3" : "reply3",
}
```
You can specify a keyword to look for in the filtered list of tweets, and then include a special reply you want the bot to reply with. You can include as many custom replies as you want!

### How it works
This script uses Tweepy to automatically search through tweets that match a specified keyword. The bot then filters out irrelevant tweets, then processes each tweet to look for tags within the tweet for it to perform the appropriate action.

For example, if a tweet contained the tag *retweet*, then the bot will retweet the tweet from your account.
If the tweet asked for you to tag two friends, the bot will reply with two users to tag from the users specified in the ```config.py``` file.

After every iteration, to ensure that the account does not get ratelimited by Twitter, the bot sleeps for 150 seconds (can be modified on the user's own risk) before combing through another set of tweets. This process is repeated until the user stops the program. Information about interactions by the bot using the account are printed out in the console after every iteration.

To check the limits Twitter sets please refer to [Twitter's Rate Limits](https://dev.twitter.com/rest/public/rate-limits) and [Twitter’s Account Limits](https://support.twitter.com/articles/344781).

### Author
Z1 (http://www.twitter.com/Z1RK4), follow me for further updates on the development of this project!

## Disclaimer

This is entirely for educational purpose. Use at your own risk and responsibility, there's a possibility that your Twitter account gets banned. I hold no liability for what you use the bot for or the consequences.

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Troubleshooting
Any questions, issues, or feature requests? Feel free to leave a comment on this project, email me at ```slitherthuglife@gmail.com```, or message me on [Twitter](https://www.twitter.com/Z1RK4)
