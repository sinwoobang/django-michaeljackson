# django-michaeljackson

<img src="https://www.grammy.com/sites/com/files/styles/news_detail_header/public/blogs/79917259.jpg?itok=vbiQiNae" alt="">
A middleware library that puts Michael Jackson's information into every response.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install django-michaeljackson
```

In your settings.py
```python
INSTALLED_APPS.append('michaeljackson')
MIDDLEWARE.append('michaeljackson.middleware.MJMiddleware')
```

## Result
You will see the header `X-Michael-Jackson` in your response.
```
X-Michael-Jackson: Parent(s): Joe Jackson Katherine Jackson
```