# Analysis Outline

## How to Run

1.  `DM_Classification_Pipeline_Training.ipynb`

    -   Download file and open in a *iPython* environment (Jupyter Notebook) OR copy the link to the notebook to [google colab](https://colab.research.google.com/).

    -   Run each cell where you need to cross check output.

    -   Run/skip training cell in the end as per computing requirements.

2.  `Twitter_API_test.ipynb`

    -   Download file and open in a *iPython* environment (Jupyter Notebook) OR copy the link to the notebook to [google colab](https://colab.research.google.com/).

    -   Run the section after the heading "Nitter Scraper".

    -   Run/skip cells as per computing requirements.

## File Description

1.  `DM_Classification_Pipeline_Training.ipynb`

    Training script for classification model that classifies tweets into "Real" and "Fake"

2.  `Twitter_API_test.ipynb`

    Testing script to use Nitter instances and obtain real-time tweets using keywords.

3.  `ntscraper/nitter.py`

    Scraping algorithm that initiates a nitter instance with beautiful soup and extracts tweets.

## Outcome

1.  A classification model that will classify tweets in real-time.
2.  A streaming pipeline that will fetch real-time tweets and save them in data/saved_tweets.csv location for further analysis.

## Goal (Next Steps)

Create a GUI using the classification model and applying it on the real-time data to generate insights for disaster tweets.
