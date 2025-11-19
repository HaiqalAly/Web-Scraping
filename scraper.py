import requests
from bs4 import BeautifulSoup
import csv
import time

# Target the first catalog page
URL = "http://books.toscrape.com/catalogue/page-1.html" 
OUTPUT_FILE = "books_data.csv"

def scrape_website(url):
    """
    Fetches a webpage, scrapes all book titles, prices, and ratings on that page, 
    and saves the results to a CSV file.
    """
    print(f"--- Starting Scraper by Haiqal---")
    print(f"Attempting to fetch {url}...")
    
    # Header for identifier and good practices
    headers = {
    'User-Agent': 'ThankYou-And-Sorry-Im-A-Student-Learning/1.0 (+https://github.com/search?q=Student-Learning-Project&type=repositories)'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Delay (good etique)
        time.sleep(1) 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 2. TARGET the specific elements for books
        # Each book is contained in an <article> tag with class 'product_pod'
        book_containers = soup.find_all('article', class_='product_pod')
        
        if not book_containers:
            print("❌ Error: No book containers found on the page.")
            return

        all_books_data = []
        
        # 3. Iterate over the found elements to extract structured data
        for book in book_containers:
            
            # Extract Title: In the <h3> tag's anchor <a> tag's 'title' attribute
            title_element = book.h3.a
            title = title_element['title'].strip() if title_element and 'title' in title_element.attrs else "N/A"
            
            # Extract Price: In a <p> tag with class 'price_color'
            price_element = book.find('p', class_='price_color')
            price = price_element.text.strip() if price_element else "N/A"
            
            # Extract Rating: In a <p> tag with a class like 'star-rating Three'
            rating_element = book.find('p', class_=lambda c: c and 'star-rating' in c)
            # We grab the last class (e.g., 'Three', 'Four', etc.)
            rating = rating_element['class'][-1] if rating_element and rating_element.has_attr('class') else "N/A"

            all_books_data.append({
                'Title': title,
                'Price': price,
                'Rating': rating
            })
        
        # 4. Write all collected data to CSV
        if all_books_data:
            print(f"\n✅ Scraper successfully processed {len(all_books_data)} books! Writing to CSV...")
            
            fieldnames = all_books_data[0].keys()
            with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_books_data)

            print(f"✅ Data saved successfully to {OUTPUT_FILE}.")
            print(f"   Sample Title: {all_books_data[0]['Title']}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ A critical error occurred during the request: {e}")

if __name__ == "__main__":
    scrape_website(URL)