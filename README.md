

# **📊 Reddit Sentiment Analysis Dashboard with Kafka & VADER**  
🚀 **Real-time Sentiment Analysis of WallStreetBets Discussions!**  

## **📖 Overview**  
This project analyzes **Reddit discussions** from *r/WallStreetBets* and visualizes sentiment trends in real time using **Streamlit**. It fetches and processes live Reddit data, applies **NLP sentiment analysis (VADER)**, and displays results in a **dynamic dashboard**.

**VADER Sentiment Analysis (SentimentIntensityAnalyzer)**
SentimentIntensityAnalyzer is a part of VADER (Valence Aware Dictionary and sEntiment Reasoner), which is a pre-trained lexicon-based sentiment analysis tool. It is particularly useful for analyzing social media comments, product reviews, and financial news.

### **✨ Features**
✅ **Live Sentiment Updates** – Tracks bullish & bearish comments in real-time  
✅ **Interactive Dashboard** – Displays trends using Streamlit  
✅ **Kafka Integration** – For processing Reddit comments efficiently  
✅ **Dockerized Deployment** – Run anywhere with `docker-compose`  

---

## **🚀 Setup Instructions**  

### **1️⃣ Prerequisites**
Ensure you have:
- **Python 3.8+**
- **Docker & Docker Compose**
- **Make (for automation)**

### **2️⃣ Run the Application**
You can **run everything using a single command!**  

```bash
make run
```

This command:
- **Checks if Docker is running**
- **Starts the application using `docker-compose.yml`**
- **Automatically builds the necessary images**  

If you don’t have `make`, you can run manually:
```bash
docker-compose up --build
```


## **📊 Dashboard Preview**
Once the app is running, **open your browser** and visit:
```
http://localhost:8501
```
You'll see a **real-time sentiment dashboard** showing:
✅ Total analyzed comments  
✅ Bullish & bearish sentiment  
✅ Sentiment trend over time  

---

## **👨‍💻 Contributing**
Want to improve this project? Follow these steps:  
1. **Fork the repository**  
2. **Make your changes**  
3. **Submit a pull request** 🚀  

---

## **Dashboard**
![image](https://github.com/user-attachments/assets/73172de4-141b-4400-8d39-dca83a039c0c)

