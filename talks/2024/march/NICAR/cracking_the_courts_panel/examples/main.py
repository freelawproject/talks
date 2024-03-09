from gifts import *
from investments import *
from reimbursements import *
from scraper import *
from recap import *

if __name__ == '__main__':
    # pass
    # Juriscraper - https://www.github.com/freelawproject/juriscraper
    # Juriscraper is a python library for scraping Court websites
    # =========================
    scrape_DC_feed()

    # Disclsoures
    # =====================
    # reimbursements(query="harlan")

    # Gifts
    # ===================
    # Gifts including the word tires
    # gifts(query="Tires")

    # Gifts from Harlan Crow
    # gifts_source(query="harlan")

    # Gifts labeled expemt <yikes>
    # gifts_source(query="exempt")

    # Chained from gift -> to disc -> judge -> education -> college
    # query_judge_gifts_by_education(college="baylor")

    # Gift -> disclosure -> court(SCOTUS)
    # query_gifts_to_scotus_judges()

    # Investments
    # ======================
    # queries = ["Tesla", "Coinbase", "COIN", "coin", "Bitcoin", "Etherereum", "crypto", "Trump", "Art", "Under Armour", "UAA"]
    # investments("bitcoin") # Generic

    # Iterate over two first invesments in P1 - to P4 Category
    # large_investments()

    # Recap Searches
    # ================
    # recap_search(query="Elon Musk")
    # query_by_nature_of_suit(query="slander")