from kafka import KafkaProducer
import json
from reddit_sentiment_analysis.config import KAFKA_BROKER

class KafkaMessageProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def send_message(self, topic, message):
        """Sends message to Kafka topic."""
        self.producer.send(topic, value=message)

    def flush(self):
        """Ensures all messages are sent."""
        self.producer.flush()
