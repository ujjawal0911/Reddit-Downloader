from hashlib import new
import praw
from tqdm import tqdm

reddit = praw.Reddit(
    client_id = 'vBOKe5A5jSjLe-i2iCKjww',
    client_secret = '3S6yZWgZoV-6J45aA0TL8b37qF_OdA',
    user_agent = 'reddit-downloader 1.0 by /u/Extreme-Rooster-868',
)

redditor_username = 'chibibellebear'
given_redditor = reddit.redditor(redditor_username)

class RedditorInformation:
    def __init__(self, redditor_username):
        self.redditor = reddit.redditor(redditor_username)


    def get_submissions(self, nsfw_filter=False):
        print('Started Fetching...')
        urls = []
        all_submissions = list(self.redditor.submissions.top(time_filter='all', limit=None))
		
		# Iterating through all the submissions
        for submission in tqdm(all_submissions, total=len(all_submissions)):

			# If the post is as image
            imgs = ['imgur.com', '.png', '.jpg', '.jpeg']
            if any(img in submission.url for img in imgs):
                urls.append(submission.url)
#                print(submission.url)

            # If the post is as gallery
            elif 'gallery' in submission.url:
                tmp = reddit.submission(url = submission.url)
                image_dict = tmp.media_metadata
                for image_item in image_dict.values():
                    largest_image = image_item['s']
                    image_url = image_item['s']['u']
                    urls.append(image_url)
#                    print(submission.url)
        print(urls)

    def get_submissions_from_subreddit(self, subreddit):
        pass

    def get_karma(self):
        pass

    def get_submission_karma(self):
        pass

    def get_comment_karma(self):
        pass


class SubredditInformation:
    pass


x = RedditorInformation(redditor_username)
x.get_submissions()
print(reddit.read_only)
