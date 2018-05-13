from pipeline import (
    download_page, find_youtube_links, fetch_youtube_videos,
    convert_videos_to_mp4, save_videos_to_cloud)


# The Chain Of Responsibility Pattern


class ChainOfResponsibility:

    def __init__(self):
        self.next_step = None

    def set_next_step(self, next_step):
        self.next_step = next_step

    def execute(self, value):
        result = self.execute_step(value)
        if self.next_step:
            return self.next_step.execute(result)

        return result


class PageDownloader(ChainOfResponsibility):

    def execute_step(self, url):
        return download_page(url)


class VideoURLFinder(ChainOfResponsibility):

    def execute_step(self, page_html):
        return find_youtube_links(page_html)


class YoutubeVideoFetcher(ChainOfResponsibility):

    def execute_step(self, links):
        return fetch_youtube_videos(links)


class MP4VideoConverter(ChainOfResponsibility):

    def execute_step(self, videos):
        return convert_videos_to_mp4(videos)


class VideoCloudUploader(ChainOfResponsibility):

    def execute_step(self, videos):
        return save_videos_to_cloud(videos)


def process_videos(url):
    page_downloader = PageDownloader()
    video_finder = VideoURLFinder()
    youtube_fetcher = YoutubeVideoFetcher()
    mp4_converter = MP4VideoConverter()
    cloud_uploader = VideoCloudUploader()

    page_downloader.set_next_step(video_finder)
    video_finder.set_next_step(youtube_fetcher)
    youtube_fetcher.set_next_step(mp4_converter)
    mp4_converter.set_next_step(cloud_uploader)

    return page_downloader.execute(url)


print(
    process_videos('some url')
)
