import os
from googleapiclient.discovery import build


class Video:

    __API_KEY: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__API_KEY)

    def __init__(self, video_id: str):
        self.__video_id = video_id
        if self.__verify_video_id(video_id) != 0:

            self.__video_response = self.__youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                                 id=self.__video_id).execute()
            self.__title = self.__video_response['items'][0]['snippet']['title']
            self.__video_url = f"https://www.youtube.com/watch?v={self.__video_id}"
            self.__view_count = self.__video_response['items'][0]['statistics']['viewCount']
            self.__like_count = self.__video_response['items'][0]['statistics']['likeCount']
        else:
            self.__title = None
            self.__video_url = None
            self.__view_count = None
            self.__like_count = None
