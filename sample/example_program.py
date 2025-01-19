from github_topic_scraper import GitHubTopicScraper
import pandas as pd
import os
from pathlib import Path

def analyze_topics():
    # Create a scraper instance with custom output directory
    scraper = GitHubTopicScraper(output_dir="downloaded_topics")
    
    try:
        # Scrape all topics and their repositories
        topics_df = scraper.scrape_all(topics_csv="all_topics.csv")
        
        # Example: Analyze the results
        print("\nAnalysis Results:")
        print(f"Total topics scraped: {len(topics_df)}")
        
        # Read all repository CSVs and analyze them
        total_repos = 0
        total_stars = 0
        
        for topic in topics_df['Title']:
            repo_file = f"downloaded_topics/{topic.lower().replace(' ', '_')}_repos.csv"
            if os.path.exists(repo_file):
                repos_df = pd.read_csv(repo_file)
                total_repos += len(repos_df)
                total_stars += repos_df['stars'].sum()
                
                # Print top repository for each topic
                if not repos_df.empty:
                    top_repo = repos_df.iloc[0]
                    print(f"\nTop repository for {topic}:")
                    print(f"  {top_repo['username']}/{top_repo['repo_name']}")
                    print(f"  Stars: {top_repo['stars']:,}")
        
        print(f"\nTotal repositories found: {total_repos:,}")
        print(f"Total stars across all repos: {total_stars:,}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    analyze_topics()