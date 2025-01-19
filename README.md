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