import praw
import os
import requests
import zipfile
from tqdm import tqdm
from typing import List
from urllib.parse import urlparse

reddit = praw.Reddit(
    client_id = 'vBOKe5A5jSjLe-i2iCKjww',
    client_secret = '3S6yZWgZoV-6J45aA0TL8b37qF_OdA',
    user_agent = 'reddit-downloader 1.0 by /u/Extreme-Rooster-868',
)

redditor_username = 'chibibellebear'
given_redditor = reddit.redditor(redditor_username)
download_location = os.getcwd()

class RedditorInformation:
    def __init__(self, redditor_username):
        self.redditor = reddit.redditor(redditor_username)


    def get_submissions_urls(self, nsfw_filter=False) -> List['str']:
        print('Getting image urls...')
        urls = []
        all_submissions = list(self.redditor.submissions.top(time_filter='all', limit=None))
		
		# Iterating through all the submissions
        for submission in tqdm(all_submissions, total=len(all_submissions)):

			# If the post is as image
            imgs = ['imgur.com', '.png', '.jpg', '.jpeg']
            if any(img in submission.url for img in imgs):
                urls.append(submission.url)

            # If the post is as gallery
            elif 'gallery' in submission.url:
                tmp = reddit.submission(url = submission.url)
                image_dict = tmp.media_metadata
                for image_item in image_dict.values():
                    largest_image = image_item['s']
                    image_url = image_item['s']['u']
                    urls.append(image_url)
        
        return urls

    def download_all_images(self, submissions: List['reddit.submission'], file_name: str = '{}.zip'.format(redditor_username)):
        print('Downloading Started...')
        # Opening the ZipFile and adding files in that
        with zipfile.ZipFile(file_name, 'w') as img_zip:
            for image_url in tqdm(submissions, total=len(submissions)):
                img_name = os.path.basename(urlparse(image_url).path)
                img_data = requests.get(image_url).content
                img_zip.writestr(img_name, img_data)

    def get_submissions_from_subreddit(self, subreddit):
        pass

    def get_karma(self):
        pass

    def get_submission_karma(self):
        pass

    def get_comment_karma(self):
        pass


class SubredditInformation:
    def __init__(self, subreddit: str):
        self.subreddit = reddit.subreddit(subreddit)
    pass


x = RedditorInformation(redditor_username)
t = x.get_submissions_urls()
x.download_all_images(t)
print(reddit.read_only)
