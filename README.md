# MID-J Search
Fetches, filters, and downloads MidJourney generated images <br />
Data is from kaggle dataset: https://www.kaggle.com/datasets/ldmtwo/midjourney-250k-csv

## How to use
Resolve depedencies `pip3 install selenium`

`import searchMJ`, use in any python scripts <br />
or use the interactive search script <br />
`python3 interact.py`


## How does it work?
`downloadData.sh` cloans [MidjourneyCSV-Kaggle](https://github.com/JustinJiangNext/MidjourneyCSV-Kaggle) if not already clones and unzips archive containing CSV files <br />
`searchMJ` searches for given terms and completes the URL from job IDs <br />
> Midjourney image: `https://cdn.midjourney.com/ + job_id + /0_0.webp` <br />
>  Midjourney job page: `https://www.midjourney.com/app/jobs/ + job_id` <br />
> Discord image: `https://media.discordapp.net/attachments/ + img_url` <br />

`scape.py` uses `selenium` to automates downloading the images from search <br />

> [!CAUTION]
> Large image batches download may result in IP ban

## Automating downloading images
Midjourney doesn't support scraping. Using `requests` library returns `403 Forbidden` status <br />
Fetching from discord URL returns `This content is no longer available.` <br />
Try exploring `selenium` in `scrape.py`


