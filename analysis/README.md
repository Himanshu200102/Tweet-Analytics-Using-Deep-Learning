# Analysis Outline

## How to Run

1.  `DM_Classification_Pipeline_Training.ipynb`

    -   Download file and open in a *iPython* environment (Jupyter Notebook) OR copy the link to the notebook to [google colab](https://colab.research.google.com/).
    -   Take the training and testing datasets (`train.csv` and `test.csv`) from the `data/` folder of the repository in order to load data.
    -   Run each cell where you need to cross check output.
    -   Run/skip training cell in the end as per computing requirements.

2.  `Data_Mining_LSTM.ipynb`

    -   Download file and open in a *iPython* environment (Jupyter Notebook) OR copy the link to the notebook to [google colab](https://colab.research.google.com/).
    -   Take the training and testing datasets (`train.csv` and `test.csv`) from the `data/` folder of the repository in order to load data.
    -   Run each cell where you need to cross check output.
    -   Run/skip training cell in the end as per computing requirements.

3.  `Twitter_API_test.ipynb`

    -   Download file and open in a *iPython* environment (Jupyter Notebook) OR copy the link to the notebook to [google colab](https://colab.research.google.com/).
    -   Run the section after the heading "Nitter Scraper".
    -   Run/skip cells as per computing requirements.

4.  `models/trainedl_lstm_model.h5`

    -   trained and saved lstm model.

    -   this can be used to load directly to the pipeline and predict the results

## File Description

1.  `DM_Classification_Pipeline_Training.ipynb`

    Contains the EDA and Preprocessing code for the dataset (`train.csv` and `test.csv`).\
    Also contains the Training script for classification model that classifies tweets into "Real" and "Fake".\
    This notebook implements the BERT model from transformers to train the data.\
    *Note: High computational GPU/TPU resources required to train this model*

2.  `Data_Mining_LSTM.ipynb`

    Contains the Training script for classification model that classifies tweets into "Real" and "Fake".\
    This notebook implements the LSTM network to train the data.

3.  `Twitter_API_test.ipynb`

    Testing script to use Nitter instances and obtain real-time tweets using keywords.

4.  `ntscraper/nitter.py`

    Scraping algorithm that initiates a nitter instance with beautiful soup and extracts tweets.

5.  `models/trainedl_lstm_model.h5`

    trained and saved lstm model.

## Outcome

1.  A classification model that will classify tweets in real-time.
2.  A streaming pipeline that will fetch real-time tweets and save them in data/saved_tweets.csv location for further analysis.

## Goal (Next Steps)

Create a GUI using the classification model and applying it on the real-time data to generate insights for disaster tweets.
