from kafka import KafkaConsumer
import json
import pandas as pd
from reddit_sentiment_analysis.consumer.preprocessing import PreProcessor
from reddit_sentiment_analysis import config

class KafkaDataConsumer:
    def __init__(self, topic=config.KAFKA_TOPIC, broker=config.KAFKA_BROKER):
        """Initialize Kafka Consumer"""
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=broker,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )

        self.pre_processor = PreProcessor()
        self.posts = {}  # Store post IDs and titles
        self.posts_data = []
        self.comments_data = []
        self.batch_size = config.BATCH_SIZE
        self.posts_file = config.POSTS_CSV
        self.comments_file = config.COMMENTS_CSV

    def consume_messages(self):
        """Consume messages from Kafka and process them"""
        print("🟢 Kafka Consumer Started... Listening for messages.")
        while True:
            for message in self.consumer:
                data = message.value

                if data["type"] == "post":
                    self.process_post(data)
                elif data["type"] == "comment":
                    self.process_comment(data)

                # Save data to CSV when batch size is reached
                self.save_batches()

    def process_post(self, data):
        """Process Post Data"""
        self.posts[data['id']] = data['title']
        self.posts_data.append([
            data['id'],
            data['title'],
            self.pre_processor.clean_text(data['selftext']),
            data['created_utc']
        ])
        print(f"✅ Post Saved: {data['title']}")

    def process_comment(self, data):
        """Process Comment Data"""
        parent_id = data['parent_id'].replace('t3_', '')  
        post_title = self.posts.get(parent_id, "Unknown Post")  
        self.comments_data.append([
            data['id'],
            post_title,
            self.pre_processor.clean_text(data['body']),
            data['created_utc']
        ])
        print(f"💬 Comment Saved: {data['body'][:50]}")

    def save_batches(self):
        """Save posts and comments data in batches"""
        if len(self.posts_data) >= self.batch_size:
            self.save_to_csv(self.posts_data, self.posts_file, ["post_id", "title", "selftext", "created_utc"])
            self.posts_data = []

        if len(self.comments_data) >= self.batch_size:
            self.save_to_csv(self.comments_data, self.comments_file, ["comment_id", "post_title", "comment", "created_utc"])
            self.comments_data = []

    @staticmethod
    def save_to_csv(data, file, columns):
        """Helper function to save data to CSV."""
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(file, mode='a', header=False, index=False)

if __name__ == "__main__":
    consumer = KafkaDataConsumer()
    consumer.consume_messages()
