from juriscraper.pacer import PacerRssFeed
import json
from pprint import pprint
from utils import *

# This code - iterates over the newest documents from PACER
# And prints out the LINK and case name to each in the courtlistener
# system

def scrape_DC_feed():
    # Scrape Pacer RSS FEED
    feed = PacerRssFeed("cadc")
    feed.query()
    feed.parse()

    for document in feed.data:
        print("")
        print(f"case name: {document['case_name']}")
        print(f"docket_number: {document['docket_number']}")
        print(f"docket_entries: {document['docket_entries'][0]['date_filed']}")
        print(
            f"docket_entries: {document['docket_entries'][0]['short_description']}")
        print(f"pacer_doc_id: {document['docket_entries'][0]['pacer_doc_id']}")
        pacer_doc_id = document['docket_entries'][0]['pacer_doc_id']
        print(
            f"document_number: {document['docket_entries'][0]['document_number']}")
        print(f"court_id: {document['court_id']}")

        s = make_session()
        url = f"https://www.courtlistener.com/api/rest/v3/recap-documents/?pacer_doc_id={pacer_doc_id}&fields=absolute_url,is_available"
        r = s.get(url).json()
        for doc in r['results']:
            if doc['is_available']:
                print(f"https://www.courtlistener.com{doc['absolute_url']}")