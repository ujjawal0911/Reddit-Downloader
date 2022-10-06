import os
import typer
from enum import Enum
from typing import List
from config import reddit
from operations import get_submissions_urls, download_all_images

download_location = os.getcwd()

class RedditorObject:
    ''' Redditor Object class to create a Redditor and get all images.'''
    def __init__(self, redditor_username):
        self.redditor = reddit.redditor(redditor_username)

    def download_posts(self, sort_by: str):

        submissions_list = []
        
        if sort_by == 'top':
            submissions_list = list(self.redditor.submissions.top(time_filter='all', limit=None))
        
        elif sort_by == 'new':
            submissions_list = list(self.redditor.submissions.new(limit=None))
        
        elif sort_by == 'hot':
            submissions_list = list(self.redditor.submissions.hot(time_filter='all', limit=None))

        urls = get_submissions_urls(submissions_list)
        filename = '{}.zip'.format(self.redditor.name)
        download_all_images(urls, filename)
        print("Download Successful")


class SubRedditObject:
    ''' SubReddit Object class to create a subreddit object and get all images. '''
    def __init__(self, subreddit_name):
        self.subreddit = reddit.subreddit(subreddit_name)

    def download_posts(self, sort_by: str, limit=None, time_filter='all'):

        submissions_list = []
        
        if sort_by == 'top':
            submissions_list = list(self.subreddit.top(time_filter='all', limit=None))
        
        elif sort_by == 'new':
            submissions_list = list(self.subreddit.new(time_filter='all', limit=None))
        
        elif sort_by == 'hot':
            submissions_list = list(self.subreddit.hot(time_filter='all', limit=None))

        urls = get_submissions_urls(submissions_list)
        filename = '{}.zip'.format(self.subreddit.name)
        download_all_images(urls, filename)
        print("/nDownload Successful")


class Sort_By(str, Enum):
    hot = 'hot'
    new = 'new'
    top = 'top'


def main(redditor: List[str] = typer.Option(None, help="Username of the Redditor"),
         subreddit: List[str] = typer.Option(None, help="Name of the Subreddit"),
         sort_by: Sort_By = typer.Option(Sort_By.top, help="Parameter by how to get the posts from hot, new or top")):
         limit: int = typer.Option(None, help="The amount of posts to download.")):

    if len(redditor) == 0 and len(subreddit) == 0:
        raise Exception("Either redditor or subreddit required. --help to get help.")

    if redditor != None:
        for cur_redditor in redditor:
            tmp = RedditorObject(cur_redditor)
            tmp.download_posts(sort_by)

    if subreddit != None:
        for cur_subreddit in subreddit:
            tmp = SubRedditObject(cur_subreddit)
            tmp.download_posts(sort_by)


if __name__ == '__main__':
   typer.run(main) 


