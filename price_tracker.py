import requests
from bs4 import BeautifulSoup as bs
from smtplib import SMTP
import csv
import schedule
import time

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587 
MAIL_USER = "your_email"  # Replace with your email address
MAIL_PASS = "your_password"  # Replace with your email password
MAIL_TO = "recipient_email@gmail.com"  # Replace with recipient's email address

def extract_product_price(url):
    page = requests.get(url=url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
    soup = bs(page.content, "html.parser")
    
    try:
        price_element = soup.find(class_="a-price-whole")
        price_text = price_element.text.split()[0].replace(",", "")
        price=int(price_text)
    except AttributeError:
        try:
            price_element = soup.find(class_="_30jeq3 _16Jk6d")
            price_text = price_element.text.split()[0].replace(",", "")
            price=int(price_text[1:])
        except AttributeError:
            print("Price element not found")
            return None
    
    return price

def email(url):
    server = SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(MAIL_USER, MAIL_PASS)

    subject = "BUY NOW"
    body = f"Price has dropped. Buy it now: {url}"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(MAIL_USER, MAIL_TO, msg)
    server.quit()

def save_price_to_csv(url, price):
    with open("tracked_price.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([url, price])

def check_product_prices(file):
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row if present
        for row in reader:
            url = row[0]
            alert_price = float(row[1])
            product_price = extract_product_price(url)
            save_price_to_csv(url,product_price)
            if product_price <= alert_price:
                email(url)
                print(f"Price dropped for {url}")

def job():
    products_file = "products.csv"
    check_product_prices(products_file)

# Schedule the job to run every 60 minutes
schedule.every(60).minutes.do(job)

# Keep the script running indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)