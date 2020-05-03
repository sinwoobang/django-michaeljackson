import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-michael-jackson',
    version='0.0.1',
    license='BSD',
    description="Put Michael Jackson's information into every response",
    long_description=README,
    long_description_content_type='text/markdown',
    author='Sin-Woo Bang',
    author_email='sinwoobang@gmail.com',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=["django>=2.2"],
    python_requires=">=3.5",
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    project_urls={
        'Source': 'https://github.com/sinwoobang/django-michaeljackson',
    },
)
