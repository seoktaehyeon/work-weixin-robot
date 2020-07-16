# Work Weixin Robot
> 企业微信机器人

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
```bash
Usage: wwx-robot -k <robot_key> -t <msg_type> -d <msg_data> -f <msg_file_path>
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

Message File Template:
    hello.md
      ## Weixin MSG
      Hello, World
    articles.yaml
      - title: 'Article I'
        description: 'Article I Description'    # Optional
        url: 'URL I'
        picurl: 'Article I Picture URL'    # Optional
      - title: 'Article II'
        description: 'Article II Description'    # Optional
        url: 'URL II'
        picurl: 'Article II Picture URL'    # Optional
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
wwxrbt.send_image(remote_url='http://www.baoxian-sz.com/wp-content/uploads/2019/07/logo_logo_zhenxinhuaxian_tiw_600_150.png')
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
