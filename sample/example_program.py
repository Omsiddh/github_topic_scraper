# example_program.py
from github_topic_scraper import GitHubTopicScraper
import pandas as pd
import os
from pathlib import Path

def analyze_topics():
    # Get the current script's directory
    script_dir = Path(__file__).parent.absolute()
    
    # Create a 'data' directory inside the script's directory
    data_dir = script_dir / 'data'
    topics_dir = data_dir / 'topics'
    
    # Create directories if they don't exist
    data_dir.mkdir(exist_ok=True)
    topics_dir.mkdir(exist_ok=True)
    
    # Print the locations where files will be stored
    print(f"\nFile Locations:")
    print(f"Base directory: {script_dir}")
    print(f"Data directory: {data_dir}")
    print(f"Topics directory: {topics_dir}")
    
    # Create a scraper instance with our explicit output directory
    scraper = GitHubTopicScraper(output_dir=str(topics_dir))
    
    try:
        # Scrape all topics and their repositories
        topics_csv_path = data_dir / "all_topics.csv"
        print(f"\nSaving topics to: {topics_csv_path}")
        topics_df = scraper.scrape_all(topics_csv=str(topics_csv_path))
        
        # Example: Analyze the results
        print("\nAnalysis Results:")
        print(f"Total topics scraped: {len(topics_df)}")
        
        # Read all repository CSVs and analyze them
        total_repos = 0
        total_stars = 0
        
        # List all created files
        print("\nCreated Files:")
        print(f"- {topics_csv_path}")
        
        for topic in topics_df['Title']:
            repo_file = topics_dir / f"{topic.lower().replace(' ', '_')}_repos.csv"
            if repo_file.exists():
                print(f"- {repo_file}")
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