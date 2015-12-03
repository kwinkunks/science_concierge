# Science Concierge: Data and model downloader

import os
import urllib


__all__ = ["download"]


def download_files(bucket_path, file_list, download_path):
    """
    Provide path to s3 bucket, download a file list to download path
    """
    if not os.path.isdir(download_path):
        os.makedirs(download_path)
    for f in file_list:
        # check if file already exists
        file_path = os.path.join(download_path, f)
        if os.path.isfile(file_path):
            print 'File "%s" already exists' % f
        else:
            print 'Downloading "%s" ...' % f
            urllib.urlretrieve(bucket_path + f, file_path)
            print 'Done'


def download(file_list=["pubmed_example.pickle"]):
    """
    Downloads example data from Science Concierge S3 folder
    """
    bucket_path = "https://s3-us-west-2.amazonaws.com/science-of-science-bucket/science_concierge/"
    current_path = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(current_path, '..','data')
    download_files(bucket_path, file_list, download_path)