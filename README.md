# Work Weixin Robot
> 企业微信机器人

[![org](https://img.shields.io/badge/org-truth%20%26%20insurance%20workshop-informational)](http://bx.baoxian-sz.com)
![author](https://img.shields.io/badge/author-v.stone@163.com-informational)
![github](https://img.shields.io/github/license/seoktaehyeon/testlink-api-client)
[![pypi](https://img.shields.io/pypi/v/WorkWeixinRobot.svg)](https://pypi.org/project/WorkWeixinRobot/)
[![ref](https://img.shields.io/badge/ref-企业微信群机器人-informational)](https://work.weixin.qq.com/help?person_id=1&doc_id=13376)

## Installation
```bash
pip install WorkWeixinRobot
```

## Usage
#### init a weixin robot
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from WorkWeixinRobot.work_weixin_robot import WWXRobot
wwx = WWXRobot(key='Robot Key')
```
#### Send Text Message
```python
wwx.send_text(content='Hello')
```
#### Send Markdown Message
```python
wwx.send_markdown(content='Hello')
```
#### Send Image Message
```python
# Method I: Send local image
wwx.send_image(local_file='local_image.jpg')
# Method II: Send remote URL image
wwx.send_image(remote_url='http://www.baoxian-sz.com/wp-content/uploads/2019/07/logo_logo_zhenxinhuaxian_tiw_600_150.png')
```
#### Send Articles Message [ Image + Text ]
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
wwx.send_news(articles=articles)
```
