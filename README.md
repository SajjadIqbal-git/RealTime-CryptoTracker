# Realtime Cryptocurrency Price Tracker

This repo fetches real-time cryptocurrency prices from the CoinGecko API and logs the data into a Google Sheets spreadsheet.

## Features

- Fetches current prices of specified cryptocurrencies
- Logs data into Google Sheets with columns for cryptocurrency name, current price, and timestamp
- Can be scheduled to run at specific intervals or triggered manually

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Google account for accessing Google Sheets
- CoinGecko API key 

### Installation

1. Clone the repository:
git clone https://github.com/SajjadIqbal-git/RealTime-CryptoTracker.git


2. Install the required Python packages:
pip install -r requirements.txt


### Configuration

1. Obtain your Google Sheets API credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the Google Sheets API for your project.
   - Create credentials for the API and download the JSON file containing your credentials.
   - Place the downloaded JSON file in the project directory and update the file path in the script.

2. Update the Google Sheets spreadsheet title:
   - Open the script (`realtime_crypto_tracker.py`) and replace `'Realtimedata'` with the title of your Google Sheets spreadsheet.

### Usage

Run the script:
python realtime_crypto_tracker.py


By default, the script fetches cryptocurrency prices and updates the Google Sheets every 1 minute. You can modify the interval as needed.

To manually trigger a data refresh, use the `-m` or `--manual` option:
python realtime_crypto_tracker.py -m
