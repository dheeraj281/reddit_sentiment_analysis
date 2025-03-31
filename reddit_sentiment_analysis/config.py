import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Kafka Configurations
KAFKA_BROKER = "broker:9092"
KAFKA_TOPIC = "wallstreetbets-stream"

# Reddit API Credentials
REDDIT_CONFIG = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "user_agent": os.getenv("REDDIT_USER_AGENT"),
}

# Fetching interval (in seconds)
REDDIT_FETCH_INTERVAL = 60

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root
POSTS_CSV = os.path.join(BASE_DIR, "shared_data", "posts.csv")  # Store in a shared folder
COMMENTS_CSV = os.path.join(BASE_DIR, "shared_data", "comments.csv")

# Number of recent posts to fetch
REDDIT_POST_LIMIT = 10
BATCH_SIZE = 10