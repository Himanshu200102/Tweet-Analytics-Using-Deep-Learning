# project-final

Final project repo for INFO 523 - Fall 2023.

## Tweet Analytics for Disaster & Calamity Management

Social media platforms like Twitter provide an unprecedented opportunity to access a vast amount of information and gain insights directly from those affected by disasters. By analyzing the conversations and trends on Twitter during such situations, the project aims to uncover patterns, validate the truthfulness of information, improve situational awareness, and ultimately contribute to the resilience and safety of individuals and communities faced with critical events.\
The major motivation behind the proposed project is to save lives and improve public safety by harnessing the power of Twitter data to access real-time information, understand & validate public sentiment.

## Deployment

🔗 The GUI made with the script in the `disastertweetapp/` folder has been deployed on this link: (https://disaster-tweet-app-algorhythms.streamlit.app/)

## Repo Organization

-   `.github`: This directory contain files related to GitHub, such as workflows, issue templates, or other configurations.

-   `. _extra`: Contains code, notes and other files used during experimentation. Contents of this folder is not a part of the final output.

-   `_freeze`: The folder created to store files generated during project render.

-   `analysis/`: This folder contains the analysis scripts used to generate output for the project outline.

    -   README.md describes the steps to run and generate the results using scripts

    -   Other code files are added to review and understand the source of the output

    -   Relevant datasets used for the scripts are under the `data/` folder in the main directory.

-   `disastertweetapp/`: This folder contains the code for GUI built using streamlit

    -   `app.py`: Main folder containing the GUI code of the app.

    -   `classification_script.py`: This file contains code for loading the trained models and functions to predict the class labels if given text. It also contains the code to extract location from the tweet.

    -   `embedtweet.py`: This file contains code to embed tweets in the GUI

    -   `fetchtweets.py`: This file contains the streaming client script to fetch real-time tweets using keywords.

    -   `requirements.py`: requirements file containing package details

    -   `models/`: Folder containing the serialized models

-   `data/`: This folder contains data files or datasets that are used in the project.

    -   README.md : A readme file that describes the datasets in more detail.

-   `images`: This folder contains image files that are used in the project, such as illustrations, diagrams, or other visual assets.

-   `.gitignore`: This file specifies which files or directories should be ignored by version control.

-   `README.md`: This file usually contains documentation or information about the project. It's often the first thing someone reads when they visit the project repository.

-   `_quarto.yml`: This is likely a configuration file

-   `about.qmd` : This quarto document contains the information about team members.

-   `index.qmd` : This quarto document contains the approach and analysis and results of the project.

-   `presentation.qmd` : It contains the slides for the presentation.

-   `proposal.qmd` : This quarto documents has the proposal of the project.

-   `project-final.Rproj` : This is an RStudio project file, which helps organize R-related files and settings for the project.

#### Disclosure:

Derived from the original data viz course by Mine Çetinkaya-Rundel \@ Duke University
