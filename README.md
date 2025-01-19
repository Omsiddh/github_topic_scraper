# github_topic_scraper
A Python package for scraping GitHub topics and their top repositories.

## Installation

```bash
pip install github-topic-scraper
```

## Usage

```python
from github_topic_scraper import GitHubTopicScraper

# Initialize the scraper
scraper = GitHubTopicScraper()

# Scrape topics and repositories
topics_df = scraper.scrape_all()

# Access the scraped data
topics_df.head()
```

## Features

- Scrapes GitHub topics and their descriptions
- Collects top repositories for each topic
- Saves data to CSV files
- Includes error handling and progress tracking
- Configurable output directory

## Requirements

- Python 3.7+
- requests
- pandas
- beautifulsoup4


## Problems in install?

1. Install Dependencies
    - Make sure your virtual environment is activated
    - pip install requests pandas beautifulsoup4
2. Install Package in Development Mode
    - Make sure you're in the github_topic_scraper directory
    - pip install -e .
3. Verify Installation
    - Start Python interpreter
    - python

    - Try importing the package
    - >>> from github_topic_scraper import GitHubTopicScraper
    - >>> # If no error appears, the package is installed correctly
    - >>> exit()

4. Run the sample file
    - if the files are being generated inside sample diretory the installation is a success
    - if the files arent being generated make sure you have a vertual enviornment setup and dependencies installed in it