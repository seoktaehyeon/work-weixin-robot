# Work Weixin Robot
> 企业微信群机器人

[![Org](https://img.shields.io/static/v1?label=org&message=Truth%20%26%20Insurance%20Office&color=597ed9)](http://bx.baoxian-sz.com)
![Author](https://img.shields.io/static/v1?label=author&message=v.stone@163.com&color=blue)
![License](https://img.shields.io/github/license/seoktaehyeon/work-weixin-robot)
[![python](https://img.shields.io/static/v1?label=Python&message=3.7&color=3776AB)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/WorkWeixinRobot.svg)](https://pypi.org/project/WorkWeixinRobot/)
[![Ref](https://img.shields.io/badge/ref-企业微信群机器人-informational)](https://work.weixin.qq.com/help?person_id=1&doc_id=13376)

## Installation
```bash
pip install WorkWeixinRobot
```

## Usage
#### Command
```text
Usage: wwx-robot -k <robot_key> -t <msg_type> -d <msg_data> -f <msg_file_path>
Option:
    -k      Robot key
    -t      Message type
              text, markdown, image, news
    -d      Message data
    -f      Message file
              +--------------+--------------+
              | Message Type |  File Type   |
              +--------------+--------------+
              |     text     |     text     |
              +--------------+--------------+
              |   markdown   |   markdown   |
              +--------------+--------------+
              |     image    |    jpg,png   |
              +--------------+--------------+
              |     news     |     yaml     |
              +--------------+--------------+
Example:
    wwx-robot -k xxxx -t text -d "Hello world"
    wwx-robot -k xxxx -t markdown -f demo/help.md
    wwx-robot -k xxxx -t image -f demo/picture.jpg
    wwx-robot -k xxxx -t news -f demo/articles.yaml

Message File Template:
    help.md
      ## Weixin MSG
      How to use this tool
    articles.yaml
      - title: 'Article I'
        description: 'Article I Description'    # Optional
        url: 'URL I'
        picurl: 'Article I Picture URL'         # Optional
      - title: 'Article II'
        description: 'Article II Description'   # Optional
        url: 'URL II'
        picurl: 'Article II Picture URL'        # Optional
```

#### Python 
##### Init a weixin robot
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from WorkWeixinRobot.work_weixin_robot import WWXRobot
wwxrbt = WWXRobot(key='Robot Key')
```
##### Send Text Message
```python
wwxrbt.send_text(content='Hello')
```
##### Send Markdown Message
```python
wwxrbt.send_markdown(content='Hello')
```
##### Send Image Message
```python
# Method I: Send local image
wwxrbt.send_image(local_file='local_image.jpg')
# Method II: Send remote URL image
wwxrbt.send_image(remote_url='https://office.baoxian-sz.com/assets/img/logo_logo_zhenxinhuaxian_tiw_600_150.png')
```
##### Send Articles Message [ Image + Text ]
```python
articles = [
    {
        'title': 'Article I',
        'description': 'Article I Description',  # Optional
        'url': 'URL I',
        'picurl': 'Article I Picture URL',  # Optional
    },
    {
        'title': 'Article II',
        'description': 'Article II Description',  # Optional
        'url': 'URL II',
        'picurl': 'Article II Picture URL',  # Optional
    }
]
wwxrbt.send_news(articles=articles)
```
