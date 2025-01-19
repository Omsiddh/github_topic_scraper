import os
from typing import Dict, List, Optional, Union
import pandas as pd
import requests
from bs4 import BeautifulSoup
from .utils import parse_star_count, ensure_output_directory, sanitize_filename

class GitHubTopicScraper:
    """
    A class to scrape GitHub topics and their repositories.
    """
    
    def __init__(self, output_dir: str = "topic_repos"):
        """
        Initialize the scraper.
        
        Args:
            output_dir (str): Directory to save topic repository CSV files
        """
        self.base_url = "https://github.com"
        self.topics_url = f"{self.base_url}/topics"
        self.output_dir = output_dir
        ensure_output_directory(output_dir)
        
    def _get_page(self, url: str) -> BeautifulSoup:
        """
        Get and parse a webpage.
        
        Args:
            url (str): URL to fetch
            
        Returns:
            BeautifulSoup: Parsed webpage
        """
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f'Failed to load page {url}')
        return BeautifulSoup(response.text, 'html.parser')
    
    def _get_topics(self) -> List[Dict[str, str]]:
        """
        Scrape the main topics page.
        
        Returns:
            List[Dict[str, str]]: List of topic information dictionaries
        """
        doc = self._get_page(self.topics_url)
        
        title_tags = doc.find_all('p', {'class': 'f3 lh-condensed mb-0 mt-1 Link--primary'})
        desc_tags = doc.find_all('p', {'class': 'f5 color-fg-muted mb-0 mt-1'})
        link_tags = doc.find_all('a', {'class': 'no-underline flex-1 d-flex flex-column'})
        
        return [
            {
                'Title': title.text.strip(),
                'Description': desc.text.strip(),
                'URL': self.base_url + link['href']
            }
            for title, desc, link in zip(title_tags, desc_tags, link_tags)
        ]
    
    def _get_topic_repos(self, topic_url: str) -> List[Dict[str, Union[str, int]]]:
        """
        Scrape repositories for a specific topic.
        
        Args:
            topic_url (str): Topic page URL
            
        Returns:
            List[Dict[str, Union[str, int]]]: List of repository information dictionaries
        """
        doc = self._get_page(topic_url)
        
        repo_tags = doc.find_all('h3', {'class': 'f3 color-fg-muted text-normal lh-condensed'})
        star_tags = doc.find_all('span', {'id': 'repo-stars-counter-star'})
        
        repos_data = []
        for repo_tag, star_tag in zip(repo_tags, star_tags):
            try:
                a_tags = repo_tag.find_all('a')
                repos_data.append({
                    'username': a_tags[0].text.strip(),
                    'repo_name': a_tags[1].text.strip(),
                    'stars': parse_star_count(star_tag.text),
                    'repo_url': self.base_url + a_tags[1]['href']
                })
            except Exception as e:
                print(f"Error processing repository: {str(e)}")
                
        return repos_data
    
    def scrape_all(self, topics_csv: str = "topics.csv") -> pd.DataFrame:
        """
        Scrape all topics and their repositories.
        
        Args:
            topics_csv (str): Filename for topics CSV
            
        Returns:
            pd.DataFrame: DataFrame containing topic information
        """
        # Get topics
        topics_data = self._get_topics()
        topics_df = pd.DataFrame(topics_data)
        topics_df.to_csv(topics_csv, index=None)
        print(f"Saved {len(topics_data)} topics to {topics_csv}")
        
        # Scrape repositories for each topic
        for topic in topics_data:
            try:
                repos_data = self._get_topic_repos(topic['URL'])
                if repos_data:
                    repos_df = pd.DataFrame(repos_data)
                    filename = f"{self.output_dir}/{sanitize_filename(topic['Title'])}_repos.csv"
                    repos_df.to_csv(filename, index=None)
                    print(f"Saved {len(repos_data)} repositories for topic: {topic['Title']}")
            except Exception as e:
                print(f"Error processing topic {topic['Title']}: {str(e)}")
        
        return topics_df