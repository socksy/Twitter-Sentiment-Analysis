Twitter Sentiment Analysis
==========================
Setup
---------
Needs twitter authentication details in a file called secrets.py containing

        APP_KEY = "xs"
        APP_SECRET = "xs"
        OAUTH_TOKEN = "xs"
        OAUTH_TOKEN_SECRET = "xs"

(obviously replacing the xs with relevant details). Run the following:

        pip install -r requirements.txt

to install the requirements (including nltk).

To Run 
------------
Atm just `python twitter.py` should work assuming everything preinstalled fine.
