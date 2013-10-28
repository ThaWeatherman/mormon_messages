mormon_messages
===============

Regularly updates a Twitter feed when a new Mormon Message is posted. The script checks [this](http://www.lds.org/pages/mormon-messages/topics?lang=eng&cid=NEDec12) page every hour for new videos. If it finds one it will tweet on the [@mormon_msg_bot](http://twitter.com/mormon_msg_bot) account.

## Dependencies

This script requries that you have Beautiful Soup 4, Tweepy, and Requests installed, as well as Python 2.7. The three libraries can be installed using pip.

## Running it

Simply run  
> python bot.py

and it will run properly. Kill it with Ctrl-C.

## Licensing

This code is licensed under the GNU Public License v2. Check the LICENSE file for details.
