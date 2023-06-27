# pip3 install snscrape

import snscrape.modules.twitter as sntwitter
import sys
import argparse


def search_tweets(query, keywords=None, remove_keywords=None):
    """
    Searches for tweets based on the given query and filters using keywords and remove_keywords.
    :param query: Query to search for tweets.
    :param keywords: Keywords to include in the tweets.
    :param remove_keywords: Keywords to exclude from the tweets.
    """
    try:
        # Create search query with keywords and remove_keywords
        if keywords:
            query += " " + " OR ".join(keywords)
        if remove_keywords:
            query += " -" + " -".join(remove_keywords)

        # Search for tweets
        tweets = sntwitter.TwitterSearchScraper(query).get_items()

        # Write the results to the console
        for tweet in tweets:
            print(f"Username: @{tweet.user.username}")
            print(f"Tweet: {tweet.content}")
            print("=" * 50)
            sys.stdout.flush()  # Flush the output to ensure immediate display

    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == '__main__':
    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keywords', nargs='+', help='Keywords to include in the tweets')
    parser.add_argument('-r', '--remove_keywords', nargs='+', help='Keywords to exclude from the tweets')
    args = parser.parse_args()

    # Call the function to search for tweets with specified keywords and remove_keywords, and write to the console
    search_tweets("", keywords=args.keywords, remove_keywords=args.remove_keywords)


