from importlib import import_module


class PipelineManager:

    def __init__(self, step_paths):
        self.step_paths = step_paths

    def execute(self, value):
        result = value

        for step_path in self.step_paths:
            [module_name, function_name] = step_path.rsplit('.', 1)

            module = import_module(module_name)
            function = getattr(module, function_name)

            result = function(result)

        return result


def process_videos(url):
    pipeline = PipelineManager([
        'pipeline.download_page',
        'pipeline.find_youtube_links',
        'pipeline.fetch_youtube_videos',
        'pipeline.convert_videos_to_mp4',
        'pipeline.save_videos_to_cloud',
    ])

    return pipeline.execute(url)


print(
    process_videos('some url')
)
