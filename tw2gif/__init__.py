import os
import sys
from tw2gif.tw2gif import Tw2Gif
import click

@click.command()
@click.option('--url', help='Post a tweet')
@click.option('--path', help='Post a tweet')
def main(url, path):
    if not url:
        print('Ups, you didn\'t especified any tweet url... :/ ')
        return
    if not path:
        path = ''
    tw2gif = Tw2Gif()
    tw2gif.download_gif(url, path)