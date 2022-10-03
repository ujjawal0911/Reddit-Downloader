import os
from config import reddit
from operations import get_submissions_urls, download_all_images

download_location = os.getcwd()

class RedditorObject:
    def __init__(self, redditor_username):
        self.redditor = reddit.redditor(redditor_username)

    def download_posts(self):
        submissions_list = list(self.redditor.submissions.top(time_filter='all', limit=None))
        urls = get_submissions_urls(submissions_list)
        filename = '{}.zip'.format(self.redditor.name)
        download_all_images(urls, filename)
        print("Download Successful")


class SubRedditObject:
    def __init__(self, subreddit_name):
        self.subreddit = reddit.subreddit(subreddit_name)

    def download_top_posts(self, limit=None, time_filter='all'):
        submissions_list = list(self.subreddit.top(limit=limit, time_filter=time_filter))
        urls = get_submissions_urls(submissions_list)
        filename = '{}.zip'.format(self.subreddit.name)
        download_all_images(urls, filename)
        print("/nDownload Successful")


if __name__ == '__main__':
    inp = int(input("Choose Redditor or subreddit (1 or 2):"))

    if inp == 1:
        username = input("Enter the username of the redditor: ")
        redditor = None

        try:
            redditor = RedditorObject(username)
        except:
            raise Exception("No such user")

        redditor.download_posts()

    elif inp == 2:
        subreddit_name = input("Enter the name of the Subreddit: ")
        subreddit = None

        try:
            subreddit = SubRedditObject(subreddit_name)
        except:
            raise Exception("Invalid Subreddit Name")

        subreddit.download_top_posts(limit=100)
        pass
    else:
        raise Exception("Invalid Option Provided.")
