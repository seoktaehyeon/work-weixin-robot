#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Will v.stone@163.com

import requests
import base64
import hashlib
import os
import yaml
import sys
import getopt


help_doc = """Usage: wwx-robot -k <robot_key> -t <msg_type> -d <msg_data> -f <msg_file_path>
Option:
    -k      Robot key
    -t      Message type
            text, markdown, image, news
    -d      Message data
    -f      Message file
            It should be text file if message type is text
            It should be markdown file if message type is markdown
            It should be image file if message type is image
            It should be YAML file if message type is news
Example:
    wwx-robot -k xxxx -t text -d "Hello world"
    wwx-robot -k xxxx -t markdown -f ./hello.md
    wwx-robot -k xxxx -t image -f ./picture.png
    wwx-robot -k xxxx -t news -f ./articles.yaml
"""


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

    @staticmethod
    def read_file(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read()
        else:
            return ""

    def sender(self, msg_type: str = "text", msg_data=None, msg_file_path=None):
        if msg_type == "text":
            self.send_text(msg_data or self.read_file(msg_file_path))
        elif msg_type == "markdown":
            self.send_markdown(msg_data or self.read_file(msg_file_path))
        elif msg_type == "image":
            if os.path.exists(msg_file_path):
                self.send_image(local_file=msg_file_path)
            else:
                self.send_image(remote_url=msg_file_path)
        elif msg_type == "news":
            self.send_news(yaml.full_load(self.read_file(msg_file_path)))


def main():
    if len(sys.argv[1:]) == 0:
        print(help_doc)
        exit(1)
    try:
        _args = dict()
        for opt, arg in getopt.getopt(sys.argv[1:], "k:t:d:f:")[0]:
            if opt == '-k':
                _args['key'] = arg
            elif opt == '-t':
                _args['type'] = arg
            elif opt == '-d':
                _args['data'] = arg
            elif opt == '-f':
                _args['file'] = arg
        print('Welcome to use Work WeiXin Robot tool')
        rbt = WWXRobot(key=_args.get('key'))
        print('Try to send == %s == message' % _args.get('type').upper())
        if _args.get('data'):
            print('Message Content:\n%s' % _args.get('data'))
        else:
            if _args.get('type') == 'image':
                print('Message Content: \n%s' % _args.get('file'))
            else:
                with open(_args.get('file'), 'r') as f:
                    print('Message Content:\n%s' % f.read())
        rbt.sender(msg_type=_args.get('type'), msg_data=_args.get('data'), msg_file_path=_args.get('file'))
    except getopt.GetoptError:
        print(help_doc)
        exit(1)
    print('Complete send message')


if __name__ == '__main__':
    print('This is the scripts of Work Weixin Robot sender')
