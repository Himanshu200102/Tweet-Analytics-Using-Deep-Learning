# GUI using Streamlit

This script utilizes the streamlit python package and cloud services to host the disaster management app.

## Tweet Analytics for Disaster & Calamity Management

Social media platforms like Twitter provide an unprecedented opportunity to access a vast amount of information and gain insights directly from those affected by disasters. By analyzing the conversations and trends on Twitter during such situations, the project aims to uncover patterns, validate the truthfulness of information, improve situational awareness, and ultimately contribute to the resilience and safety of individuals and communities faced with critical events.\
The major motivation behind the proposed project is to save lives and improve public safety by harnessing the power of Twitter data to access real-time information, understand & validate public sentiment.

## Deployment

🔗 The GUI made with the script in the disastertweetapp/ folder has been deployed on this link: (https://disaster-tweet-app-algorhythms.streamlit.app/)

## File Description

-   `disastertweetapp/`: This folder contains the code for GUI built using streamlit

    -   `app.py`: Main folder containing the GUI code of the app.

    -   `classification_script.py`: This file contains code for loading the trained models and functions to predict the class labels if given text. It also contains the code to extract location from the tweet.

    -   `embedtweet.py`: This file contains code to embed tweets in the GUI

    -   `fetchtweets.py`: This file contains the streaming client script to fetch real-time tweets using keywords.

    -   `requirements.py`: requirements file containing package details

    -   `models/`: Folder containing the serialized models

#### Disclosure:

Derived from the original data viz course by Mine Çetinkaya-Rundel \@ Duke University
