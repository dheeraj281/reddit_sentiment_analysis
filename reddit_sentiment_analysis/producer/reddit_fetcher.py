import praw
import time
from reddit_sentiment_analysis.producer.kafka_producer import KafkaMessageProducer
from reddit_sentiment_analysis.config import REDDIT_CONFIG, KAFKA_TOPIC, REDDIT_FETCH_INTERVAL, REDDIT_POST_LIMIT

class RedditFetcher:
    def __init__(self):
        self.reddit = praw.Reddit(**REDDIT_CONFIG)
        self.producer = KafkaMessageProducer()
        self.processed_posts = set()
        self.processed_comments = set()

    def fetch_and_publish(self):
        """Fetches Reddit posts & comments and sends them to Kafka."""
        print("Fetching new Reddit posts and comments...")

        for submission in self.reddit.subreddit("wallstreetbets").new(limit=REDDIT_POST_LIMIT):
            if submission.id not in self.processed_posts:
                post_data = {
                    "type": "post",
                    "id": submission.id,
                    "title": submission.title,
                    "selftext": submission.selftext,
                    "url": submission.url,
                    "created_utc": submission.created_utc,
                }

                print(f"Fetched New Post: {submission.title}")
                self.producer.send_message(KAFKA_TOPIC, post_data)
                self.processed_posts.add(submission.id)

                submission.comments.replace_more(limit=0)
                for comment in submission.comments.list():
                    if comment.id not in self.processed_comments:
                        comment_data = {
                            "type": "comment",
                            "id": comment.id,
                            "parent_id": comment.parent_id,
                            "body": comment.body,
                            "created_utc": comment.created_utc,
                        }

                        print(f"Fetched New Comment: {comment.body[:50]}")
                        self.producer.send_message(KAFKA_TOPIC, comment_data)
                        self.processed_comments.add(comment.id)

        self.producer.flush()

    def run(self):
        """Runs the fetcher in a loop with intervals."""
        while True:
            self.fetch_and_publish()
            print(f"Waiting {REDDIT_FETCH_INTERVAL} seconds before next fetch...")
            time.sleep(REDDIT_FETCH_INTERVAL)

if __name__ == "__main__":
    fetcher = RedditFetcher()
    fetcher.run()
