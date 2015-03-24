# kfdata scraper
Scraper around KF data

## Getting started

* Step 0: Have virtualenv and virtualenvwrapper installed.

```
sudo pip install virtualenv virtualenvwrapper
```

* Step 1: Make a virtualenv and install requirements.

```
git clone git@github.com:poderomedia/kfdata.git && cd kfdata
mkvirtualenv kfdata
pip install -r requirements.txt
```

* Step 2: Run the scraper.
```
scrapy crawl grants -t csv -o filename.csv
```

