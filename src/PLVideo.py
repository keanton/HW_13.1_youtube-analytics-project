from src.video import Video


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_ids: str):
        super().__init__(video_id)
        self.__playlist_ids = playlist_ids

