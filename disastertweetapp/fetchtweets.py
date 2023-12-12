import ntscraper
import streamlit as st
import spacy

@st.cache_resource
def tweet_object(skip_check=False):
    
    scraper = ntscraper.Nitter(skip_instance_check=skip_check)

    return scraper



def fetch_tweets(keyword, mode, number, near=None, exclude=None, filters=None, to=None, language='en', since=None, until=None):

    scraper = tweet_object()

    try:
        tweet_dict = scraper.get_tweets(keyword, mode=mode, number=number,
                                        near=near, exclude=exclude, filters=filters,
                                        to=to, language=language, since=since, until=until,
                                        # instance="http://localhost:8080"
                                        )
    except Exception as e:
        st.write("Retry request")
        print(e)

    return tweet_dict

def get_location(tweet_text):
    
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(tweet_text)

    gpe_entities = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    if gpe_entities or gpe_entities != []:
        return ", ".join(gpe_entities)
    else:
        return "No location found"