import os
import zipfile
import requests
from config import reddit
from typing import List
from tqdm import tqdm
from urllib.parse import urlparse


def get_submissions_urls(submissions: List['reddit.submission']) -> List['str']:
        '''Function to get URLs of all the image based submissions'''
        
        print('Getting image urls...')
        urls = []
		
		# Iterating through all the submissions
        for submission in tqdm(submissions, total=len(submissions)):

			# If the post is as image
            imgs = ['imgur.com', '.png', '.jpg', '.jpeg']
            if any(img in submission.url for img in imgs):
                urls.append(submission.url)

            # If the post is as gallery
            elif 'gallery' in submission.url:
                tmp = reddit.submission(url = submission.url)
                image_dict = tmp.media_metadata
                for image_item in image_dict.values():
                    image_url = image_item['s']['u']
                    urls.append(image_url)
        
        return urls

def download_all_images(submissions: List['str'], file_name: str):
        '''Function to download all images given the url links'''

        print('Downloading Started...')

        # Opening the ZipFile and adding files in that
        with zipfile.ZipFile(file_name, 'w') as img_zip:
            for image_url in tqdm(submissions, total=len(submissions)):
                img_name = os.path.basename(urlparse(image_url).path)
                img_data = requests.get(image_url).content
                img_zip.writestr(img_name, img_data)