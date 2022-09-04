from hashlib import new
import praw

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
        count = 0
        for submission in self.redditor.submissions.top(time_filter='all', limit=None):
            print(submission.title + ' : ' +  submission.url)
            # if hasattr(submission, 'media_metadata'):
            #     image_dict = submission.media_metadata
            #     for image_item in image_dict.values():
            #         largest_image = image_item['s']
            #         image_url = largest_image['u']
            #         print(image_url)


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