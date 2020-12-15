import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/anny_/Documents/DataScience_Project/chromedriver_win32/chromedriver.exe"
df = gs.get_jobs("data scientist", 15, False, path, 15)
df.to_excel("C:\\Users\\anny_\\Documents\\DataScience_Project\\input\\input.xlsx")