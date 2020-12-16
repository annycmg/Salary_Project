import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/anny_/Documents/The_Glassdoor_Project/chromedriver_win32/chromedriver.exe"
df = gs.get_jobs("data scientist", 35, False, path, 15)
df.to_csv("C:\\Users\\anny_\\Documents\\The_Glassdoor_Project\\input_glassdoor.csv", index=False)