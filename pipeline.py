from time import sleep


def download_page(url):
    print('Downloading Page HTML')
    sleep(1)
    return '<h1>Some html</h1>'


def find_youtube_links(page_html):
    print('Finding Youtube videos in page HTML')
    sleep(1)
    return ['link1', 'link2']


def fetch_youtube_videos(video_links):
    print('Downloading Youtube videos')
    sleep(1)
    return ['Video Object 1', 'Video Object 2']


def convert_videos_to_mp4(videos):
    print('Converting Videos to MP4')
    sleep(1)
    return ['MP4 Video Object 1', 'MP4 Video Object 2']


def save_videos_to_cloud(videos):
    print('Saving videos to cloud')
    sleep(1)
    return ['Link to Video 1', 'Link to Video 2']
