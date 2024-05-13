import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from datetime import datetime
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to authenticate with Google Sheets API
def authenticate_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('file to the json file', scope)
    gc = gspread.authorize(credentials)
    return gc

# Function to fetch cryptocurrency prices from CoinGecko API
def fetch_crypto_prices():
    crypto_list = ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'bitcoin-cash']  # Add more if needed
    prices = {}
    for crypto in crypto_list:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        if data and crypto in data:
            prices[crypto] = {'price': data[crypto]['usd'], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    return prices

# Function to write data to Google Sheets
def write_to_google_sheets(sheet, prices):
    worksheet = sheet.sheet1  # Access the first worksheet
    header = ['Cryptocurrency', 'Price', 'Timestamp']
    
    # Check if header row exists, if not, add it
    if worksheet.row_count == 0:
        worksheet.append_row(header)
    
    # Append data rows
    for crypto, info in prices.items():
        worksheet.append_row([crypto, info['price'], info['timestamp']])

# Function to fetch prices and update Google Sheets
def update_prices():
    try:
        logging.info("Fetching cryptocurrency prices...")
        
        # Authenticate with Google Sheets API
        gc = authenticate_google_sheets()

        # Open the spreadsheet by its title
        sh = gc.open('Realtimedata')

        # Fetch cryptocurrency prices
        prices = fetch_crypto_prices()

        # Write prices to Google Sheets
        write_to_google_sheets(sh, prices)

        logging.info("Data successfully logged into Google Sheets!")
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

# Schedule the script to run every 1 minute
schedule.every(1).minutes.do(update_prices)

# Main loop to continuously check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
