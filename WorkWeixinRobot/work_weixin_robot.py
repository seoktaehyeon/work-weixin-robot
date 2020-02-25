#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Will v.stone@163.com

import requests
import base64
import hashlib


class WWXRobot(object):
    def __init__(self, key: str):
        self.url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key
        self.headers = {
            'Content-Type': 'application/json'
        }

    def _send(self, body: dict):
        rsp = requests.post(url=self.url, headers=self.headers, json=body)
        assert rsp.status_code == 200, rsp.content
        assert rsp.json().get('errmsg') == 'ok', rsp.content
        print('SUCCEED')
        return True

    def send_text(self, content: str):
        """
        文本类型
        :param content:
        :return:
        """
        body = {
            'msgtype': 'text',
            'text': {
                'content': content,
                # 'mentioned_list': ['@all'],  # Optional
                # 'mentioned_mobile_list': ['@all']  # Optional
            }
        }
        self._send(body)

    def send_markdown(self, content: str):
        """
        Markdown 类型
        :param content:
        :return:
        """
        body = {
            'msgtype': 'markdown',
            'markdown': {
                'content': content,
            }
        }
        self._send(body)

    def send_image(self, local_file=None, remote_url=None):
        """
        图片类型
        :param local_file: local file path
        :param remote_url: image url
        :return:
        """
        if local_file:
            with open(local_file, 'rb') as f:
                image_content = f.read()
        elif remote_url:
            image_content = requests.get(remote_url).content
        else:
            raise Exception('Need provide local_file: str or remote_url: str')
        image_base64 = base64.b64encode(image_content).decode('utf-8')
        md5 = hashlib.md5()
        md5.update(image_content)
        image_md5 = md5.hexdigest()
        body = {
            'msgtype': 'image',
            'image': {
                'base64': image_base64,
                'md5': image_md5
            }
        }
        self._send(body)

    def send_news(self, articles: list):
        """
        图文类型
        :param articles: [
            {
                'title': '',
                'description': '',  # Optional
                'url': '',
                'picurl': '',  # Optional
            }
        ]
        :return:
        """
        assert len(articles) <= 8, 'Only support 1-8 articles'
        for article in articles:
            assert article.get('title'), 'Need provide article title'
            assert article.get('url'), 'Need provide article url'
        body = {
            'msgtype': 'news',
            'news': {
                'articles': articles
            }
        }
        self._send(body)


if __name__ == '__main__':
    print('This is the scripts for QiYe WeiXin Robot')

