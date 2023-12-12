# Data

There are two sources of the dataset. The model training has been taken from [**Natural Language Processing with Disaster Tweets**](https://www.kaggle.com/competitions/nlp-getting-started) competition. It comes with a training and a testing dataset.\
The real-time scraped data comes from a streaming using NTscraper, a webscraping based python package, to create a Nitter object which uses Beautiful soup in the back end to fetch tweet details.

-   **\[saved_tweets.csv\]**: Tweets scraped from streaming client are saved in this file
-   **\[train.csv\]**: Training dataset with tweet text and annotated labels
-   **\[test.csv\]**: Testing dataset to validate the model

## Data Types:

-   train.csv and test.csv

| Column Name | Data Type       | Description                                                                                     |
|----------------|----------------|----------------------------------------|
| id          | Integer         | A unique identifier for each tweet                                                              |
| text        | List of strings | It contains the text of the tweet                                                               |
| location    | List of strings | The location the tweet was sent from (may be blank)                                             |
| keyword     | List of Strings | A particular keyword from the tweet (may be blank)                                              |
| target      | Integer         | in **train.csv** only, this denotes whether a tweet is about a real disaster (`1`) or not (`0`) |

-   saved_tweets.csv

| Column Name | Data Type | Description                                                                                             |
|-----------------|-----------------|--------------------------------------|
| link        | String    | The link to the tweet                                                                                   |
| text        | String    | It contains the text of the tweet                                                                       |
| user        | Object    | A disctionary contatining the information about user such as name, profile link and profile description |
| is_retweet  | Boolean   | Is tweet a retweet                                                                                      |
| comments    | Integer   | Number of comments on the tweet                                                                         |
| quotes      | Integer   | Number of tweets that quote this tweet                                                                  |
| likes       | Integer   | Number of likes                                                                                         |
| images      | List      | List of link of images associated with the tweet                                                        |
| video       | List      | List of link of video associated with the tweet                                                         |
| gifs        | List      | List of link of gifs associated with the tweet                                                          |
| topic       | String    | Topic of the tweet, keyword used to fetch this tweet                                                    |
