# TwitterScraper
Python-based Twitter scraper capable of executing queries on the Twitter platform in the absence of an API key.

pip3 install -r requirements.txt

python3 twitterScraper.py --help

options:
  
  -h, --help            show this help message and exit
  
  -k KEYWORDS [KEYWORDS ...], --keywords KEYWORDS [KEYWORDS ...]
                        Keywords to include in the tweets
                        
  -r REMOVE_KEYWORDS [REMOVE_KEYWORDS ...], --remove_keywords REMOVE_KEYWORDS [REMOVE_KEYWORDS ...]
                        Keywords to exclude from the tweets

Examples: 

python3 twitterScraper.py -k Joan Adon -r baseball
