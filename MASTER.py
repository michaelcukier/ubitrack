#!/usr/bin/env python3

import os

dict = ["basic_income_news.py",
        "bbc.py",
        "business_insider.py",
        "case_for_basic_income.py",
        "cnbc.py",
        "dw.py",
        "fast_company.py",
        "fox.py",
        "futurism.py",
        "la_times.py",
        "new_yorker.py",
        "ny_times.py",
        "precarious_work.py",
        "quartz.py",
        "reddit.py",
        "spotlight_on_poverty.py",
        "techcrunch.py",
        "the_independent.py",
        "venture_beats.py",
        "vox.py",
        "washington_post.py",
        "google_news.py"]

for pyFile in dict:
    os.system('python3 /root/realScrap/scrapers/' + str(pyFile))

# os.system('/sbin/reboot')  # cleans up all the mess
