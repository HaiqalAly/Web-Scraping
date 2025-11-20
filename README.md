# 📚 Python Web Scraper

A simple and clean web-scraping project written in Python.  
This scraper fetches **book titles, prices, and ratings** from *Books to Scrape* and saves the results into a CSV file.

> **Note:** This project is primarily for learning purposes, especially to practice **containerization with Docker**.  
> Docker is new to me, and while I’ve tested the instructions carefully, there may still be **errors or issues on other systems**.  
> Feedback or suggestions are very welcome!

---

## ✨ Features

- Scrapes **title**, **price**, and **rating** from each book  
- Saves results automatically to: `data/books_data.csv`
- Includes polite scraping practices (custom user-agent + delay)
- Fully containerized with **Docker**
- Supports **VS Code Dev Containers**

---

## 📁 Project Structure

```bash
Web-Scraping/
│
├── .devcontainer/
│ └── Dockerfile
│ └── devcontainer.json
│
├── src/
│ └── scraper.py
│
├── data/
│ └── (generated CSV file here)
│
├── requirements.txt
```

---

## 🛠️ Tech
* ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
* ![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

---

## 🚀 How to Run the Scraper

You can run the scraper in **three ways**:

---

## 1. Run with Local Python 🐍 (No Docker)

### Prerequisites
- Python 3.10+  
- `pip`

### Clone the repo
```bash
git clone https://github.com/HaiqalAly/Web-Scraping
cd Web-Scraping
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run scraper
```bash
python src/scraper.py
```

### Your output CSV will appear here:
```bash
data/books_data.csv
```

---

## 2. Run with Docker 🐳

### Navigate to root directory
```bash
cd C:\Users\Your Username\Documents\Web-Scraping
```

### Build the image
```bash
docker build -t web-scraper -f .\.devcontainer\Dockerfile .
```

### Run the container
* Linux / MacOS
```bash
docker run --rm -v $(pwd)/data:/app/data web-scraper
```

* Windows PowerShell
```bash
docker run --rm -v ${PWD}/data:/app/data web-scraper
```
This mounts your local data/ folder so the CSV appears outside the container.

---

## ⚠️ Troubleshooting

- On Windows, use PowerShell for the volume mount: `${PWD}/data:/app/data`  
- If the `data/` folder doesn’t exist, Docker will create it automatically  
- For other issues, please open a GitHub Issue or send feedback

