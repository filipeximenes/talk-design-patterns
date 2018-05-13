from pipeline import (
    download_page, find_youtube_links, fetch_youtube_videos,
    convert_videos_to_mp4, save_videos_to_cloud)


def process_videos(url):
    page_html = download_page(url)
    video_links = find_youtube_links(page_html)
    videos = fetch_youtube_videos(video_links)
    videos = convert_videos_to_mp4(videos)
    return save_videos_to_cloud(videos)


print(
    process_videos('some url')
)
