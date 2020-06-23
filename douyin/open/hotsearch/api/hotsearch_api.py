# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from douyin.open.hotsearch.api_client import ApiClient


class HotsearchApi(object):
    """NOTE: 由抖音小开自动生成，请勿自己修改
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def hotsearch_sentences_get(self, access_token, **kwargs):
        """获取实时热点词

        * Scope: `hotsearch` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hotsearch_sentences_get(access_token, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :return: HotsearchSentencesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hotsearch_sentences_get_with_http_info(access_token, **kwargs)
        else:
            (data) = self.hotsearch_sentences_get_with_http_info(access_token, **kwargs)
            return data

    def hotsearch_sentences_get_with_http_info(self, access_token, **kwargs):
        """获取实时热点词  # noqa: E501

        * Scope: `hotsearch` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hotsearch_sentences_get_with_http_info(access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :return: HotsearchSentencesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hotsearch_sentences_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `hotsearch_sentences_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/hotsearch/sentences/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HotsearchSentencesResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def hotsearch_videos_get(self, access_token, hot_sentence, **kwargs):
        """获取热点词聚合的视频

        * Scope: `hotsearch` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hotsearch_videos_get(access_token, hot_sentence, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :param str hot_sentence: 热点词 (required)
        :return: HotsearchVideosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hotsearch_videos_get_with_http_info(access_token, hot_sentence, **kwargs)
        else:
            (data) = self.hotsearch_videos_get_with_http_info(access_token, hot_sentence, **kwargs)
            return data

    def hotsearch_videos_get_with_http_info(self, access_token, hot_sentence, **kwargs):
        """获取热点词聚合的视频  # noqa: E501

        * Scope: `hotsearch` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hotsearch_videos_get_with_http_info(access_token, hot_sentence, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :param str hot_sentence: 热点词 (required)
        :return: HotsearchVideosResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'hot_sentence']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hotsearch_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `hotsearch_videos_get`")
        # verify the required parameter 'hot_sentence' is set
        if ('hot_sentence' not in params or
                params['hot_sentence'] is None):
            raise ValueError("Missing the required parameter `hot_sentence` when calling `hotsearch_videos_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'hot_sentence' in params:
            query_params.append(('hot_sentence', params['hot_sentence']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/hotsearch/videos/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HotsearchVideosResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)