from pipeline import (
    download_page, find_youtube_links, fetch_youtube_videos,
    convert_videos_to_mp4, save_videos_to_cloud)


# The Pipeline Pattern


class PipelineManager:

    def __init__(self):
        self.steps = []

    def add_step(self, next_step):
        self.steps.append(next_step)

    def execute(self, value):
        result = value
        for step in self.steps:
            result = step.execute_step(result)

        return result


class PageDownloader:

    def execute_step(self, url):
        return download_page(url)


class VideoURLFinder:

    def execute_step(self, page_html):
        return find_youtube_links(page_html)


class YoutubeVideoFetcher:

    def execute_step(self, links):
        return fetch_youtube_videos(links)


class MP4VideoConverter:

    def execute_step(self, videos):
        return convert_videos_to_mp4(videos)


class VideoCloudUploader:

    def execute_step(self, videos):
        return save_videos_to_cloud(videos)


def process_videos(url):
    pipeline = PipelineManager()

    pipeline.add_step(PageDownloader())
    pipeline.add_step(VideoURLFinder())
    pipeline.add_step(YoutubeVideoFetcher())
    pipeline.add_step(MP4VideoConverter())
    pipeline.add_step(VideoCloudUploader())

    return pipeline.execute(url)


print(
    process_videos('some url')
)
