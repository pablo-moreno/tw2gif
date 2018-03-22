import os
import sys
from tw2gif.tw2gif import Tw2Gif
import click

@click.command()
@click.option('--url', help='Tweet URL')
@click.option('--path', help='Output file path')
def main(url, path):
    if not url:
        print('Ups, you didn\'t especified any tweet url... :/ ')
        return
    if not path:
        path = ''
    tw2gif = Tw2Gif()
    tw2gif.download_gif(url, path)