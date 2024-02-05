# twitter_scraper_gui
# GUI for ntscraper Twitter scraping

This simple program provides a GUI to scrape tweets by hashtag or profile making use of the "ntscraper" library, exporting the tweets to an excel (.xlsx) file.

## Capabilities:
### It retrieves the following attributes: 
tweet link, tweet content, date, likes, profile ID, language

It can retrieve up to 800 tweets per runthrough.

## INSTALLATION:
run twitter_gui_prerequisites.py
### or manually install the prerequisites.
run twitter_scrape_gui.py

### Prerequisites:
twitter_scraper_gui makes use of the following python libraries:
pandas, tqdm, tkinter, customtkinter, ntscraper, openpyxl
