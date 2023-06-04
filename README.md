# E-commerce-Product-Price-Tracker


This Python-based project is a simple yet powerful tool for tracking product prices on e-commerce websites. It allows users to monitor the prices of their favorite products and receive email alerts when the prices drop below a specified threshold.

Features:
- Product Price Tracking: The tracker can monitor the prices of multiple products on popular e-commerce websites such as Amazon and Flipkart.
- Email Alerts: When a product's price drops below the set threshold, an email notification is sent to the user's specified email address, allowing them to take advantage of the price reduction.
- Flexible Configuration: Users can easily configure the tracker by providing a CSV file containing the product URLs and desired alert prices. This allows for easy customization and tracking of different products.
- Scheduled Execution: The tracker can be set to run at specified intervals, such as every 1 hour, allowing for automatic and continuous price monitoring.
- Data Persistence: The project provides the option to save the tracked prices in a CSV file, enabling the user to analyze price trends over time.

Requirements:

- Python
- Requests library
- BeautifulSoup library
- smtplib library
- CSV module

Usage:
- Clone the repository to your local machine.
- Install the required dependencies
- Configure the email settings in the script by updating the  MAIL_USER, MAIL_PASS, and MAIL_TO variables.
- Prepare a CSV file (products.csv) containing the product URLs and desired alert prices.
- Run the script using python price_tracker.py.

Future Enhancements:
- Support for additional e-commerce websites.
- Web-based user interface for easier configuration and monitoring.
- Price history visualization and trend analysis.
- Integration with external APIs for automatic product price updates.
