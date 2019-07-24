'''
Config! Change as needed.

NOTE: Please make sure that all information (except for authentication keys)
are passed in lower-case!
'''

# Your twitter access tokens. These are your accounts that you will enter giveaways from.
# Add as many users as you want, and please make sure to enter your username in lower case!
access_tokens = {
    "user1" : {
        'consumer_key' : '', 
        'consumer_secret' : '', 
        'access_token' : '', 
        'access_token_secret' : ''
    },

    "user2" : {
        'consumer_key' : '', 
        'consumer_secret' : '', 
        'access_token' : '', 
        'access_token_secret' : ''
    },
    
    "user3" : {
        'consumer_key' : '',
        'consumer_secret' : '',
        'access_token' : '',
        'access_token_secret' : ''
    }
}

# REQUIRED
# Users that you would like to tag in the giveaway. Add three users here.
tag_users = ["z1rk4", "user2", "user3"]

#REQUIRED
# Keywords that the bot will search for in tweets. Change/add as many as you want!
keywords = ["giveaway", "coding", "python"]

# OPTIONAL
# Account names that you want to specifically search for giveaway tweets. 
# Add as many as you want!
account_names = ["giveaway_account1", "giveaway_account2", "giveaway_account3"]

# OPTIONAL
# Add your own custom replies here that are triggered upon a specific keyword. 
# NOTE: Program may not be able to send reply if replies are too long! Please be careful
# with how many custom replies you use :)
custom_replies = {
    "keyword1" : "reply1",
    "keyword2" : "reply2",
    "keyword3" : "reply3",
}

'''
Leave the variables below alone if you do not have the respective information.
'''
# OPTIONAL
# Your steam trade link
trade_link = ""

# OPTIONAL
# Your wax trade link 
wax_trade_link = ""

# OPTIONAL
# Your DatDrop profile link 
datdrop_profile_link = ""



# IGNORE
link_paste_keywords = ["tradelink", "trade link", " tl"]