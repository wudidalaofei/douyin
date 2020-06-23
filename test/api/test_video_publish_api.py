# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import unittest

from douyin.open.video_create.api.video_publish_api import VideoPublishApi
from douyin.open.video_create.rest import ApiException

from douyin.open.video_create.model.video_create_body import VideoCreateBody
from douyin.open.video_create.model.video_create_response import VideoCreateResponse
from douyin.open.video_create.model.video_part_complete_response import VideoPartCompleteResponse
from douyin.open.video_create.model.video_part_init_response import VideoPartInitResponse
from douyin.open.video_create.model.video_part_upload_response import VideoPartUploadResponse
from douyin.open.video_create.model.video_upload_response import VideoUploadResponse


class TestVideoPublishApi(unittest.TestCase):
    """VideoPublishApi unit test stubs"""

    def setUp(self):
        self.api = VideoPublishApi()

    def tearDown(self):
        pass

    def test_video_create_post(self):
        """Test case for video_create_post

        创建抖音视频
        """
        body=VideoCreateBody()
        resp = self.api.video_create_post(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', body=body)
        pass

    def test_video_part_complete_post(self):
        """Test case for video_part_complete_post

        完成上传
        """
        
        resp = self.api.video_part_complete_post(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', upload_id='upload_id_example', )
        pass

    def test_video_part_init_post(self):
        """Test case for video_part_init_post

        初始化上传
        """
        
        resp = self.api.video_part_init_post(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', )
        pass

    def test_video_part_upload_post(self):
        """Test case for video_part_upload_post

        上传视频分片到文件服务器
        """
        
        resp = self.api.video_part_upload_post(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', upload_id='upload_id_example', part_number=56, video='video_example')
        pass

    def test_video_upload_post(self):
        """Test case for video_upload_post

        上传视频到文件服务器
        """
        
        resp = self.api.video_upload_post(open_id='ba253642-0590-40bc-9bdf-9a1334b94059', access_token='act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr', video='video_example')
        pass


if __name__ == '__main__':
    unittest.main()