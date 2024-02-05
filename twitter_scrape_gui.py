import customtkinter as ck
import pandas as pd
from ntscraper import Nitter

#create GUI instance
root = ck.CTk()
root.title("Twitter Scraper")
ck.set_default_color_theme("green")
ck.set_appearance_mode("System")

#define callback faunctions for dropdown menus
def optionmenu_callback_lang(language_choice):
    lang_var.set(language_choice)

def optionmenu_callback_modes(modes_choice):
    modes_var.set(modes_choice)

#define tkinter buttons, labels, menus etc.
name_label = ck.CTkLabel(root, text = "Enter Search Title")
name_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "w")

name_entry = ck.CTkEntry(master = root, placeholder_text = "enter search title")
name_entry.grid(row = 1, column = 1, padx = 10, pady = 5)

num_label = ck.CTkLabel(root, text = "Enter number of tweets (800 max)")
num_label.grid(row=2, column = 0, padx = 10, pady = 5, sticky = "w")

no_entry = ck.CTkEntry(master = root, placeholder_text = "enter number of tweets")
no_entry.grid(row = 2, column = 1, padx = 10, pady = 5)

lang_label = ck.CTkLabel(root, text = "select tweet language")
lang_label.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = "w")

lang_var = ck.StringVar(value = "en")
lang_menu = ck.CTkOptionMenu(root ,values = ["en", "de"], command = optionmenu_callback_lang, variable = lang_var)
lang_menu.grid(row = 3, column = 1, padx = 10, pady = 5)

mode_label = ck.CTkLabel(root, text = "select search mode (person, hashtag, etc.)")
mode_label.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = "w")

modes_var = ck.StringVar(value = "hashtag")
modes_menu = ck.CTkOptionMenu(root ,values = ["person", "hashtag"], command = optionmenu_callback_modes, variable = modes_var)
modes_menu.grid(row = 4, column = 1, padx = 10, pady = 5)

#initialize scraper and scrape/export functions
def get_tweets():
    scraper = Nitter()
    tweet_list = []
    tweets = scraper.get_tweets(name_entry.get(), mode = modes_var.get(), number = int(no_entry.get()), language = lang_var.get())

    for tweet in tweets["tweets"]:
        data = [tweet["link"], tweet["text"], tweet["date"], tweet["stats"]["likes"], tweet["user"]["profile_id"], lang_var.get()]
        tweet_list.append(data)

    data = pd.DataFrame(tweet_list, columns = ["link", "tweet content", "date", "likes", "profile_id", "language"])
    return data

def get_tweets_and_export():
    data = get_tweets()
    data.to_excel("tweets.xlsx")
    

export_button = ck.CTkButton(master = root,text="Get Tweets and Export to Excel", command = get_tweets_and_export)
export_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.mainloop()