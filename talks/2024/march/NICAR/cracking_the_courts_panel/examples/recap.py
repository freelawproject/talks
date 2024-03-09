from utils import make_session, make_endpoint

search_endpoint = "https://www.courtlistener.com/api/rest/v3/search/"
court_endpoint = "https://www.courtlistener.com/api/rest/v3/courts"
docket_endpoint = "https://www.courtlistener.com/api/rest/v3/dockets/"


def recap_search(query="Elon Musk"):
    """Looking for new documents with elon musk in side them
    """

    s = make_session()
    params = [
        ('type', 'r'),
        ('q', query),
        ('order_by', 'dateFiled desc'),
        ('available_only', 'on'),
        # ("court", "alnd alsd almd"),
        ('filed_after', '2022-03-01'),
        # ('filed_before', '2022-09-01'),
        # ("suitNature", "950 Constitutional - State Statute"),
    ]
    r = s.get(search_endpoint, params=params, timeout=15).json()

    print(r['count'])
    for row in r['results']:
        print("")
        print(row['caseName'])
        # print(row)
        print("Date:", row['entry_date_filed'][:10])
        print(row['id'], row['docketNumber'])
        print(f"Judge: {row['assignedTo']}")
        print(f"Nature of Suit: {row['suitNature']}")
        print("Description:", row['description'][:200])
        print(f"https://www.courtlistener.com{row['absolute_url']}")


def query_by_nature_of_suit(query: str = "slander"):
    """Query for each district court go.
    """
    s = make_session()

    params = [
        ("jurisdiction", "FD"),
        ("in_use", True),
        # ('fields', "id,url,full_name")
    ]
    res = s.get(court_endpoint, params=params, timeout=15).json()
    while True:
        for court in res['results']:
            params = [
                ("fields", "id"),
                ("date_filed__gt", "2024-01-01"),
                ("court", court['id']),
                ("nature_of_suit__icontains", query),
            ]
            try:
                cases = s.get(docket_endpoint, params=params, timeout=10).json()
                print(court['full_name'].ljust(45),
                      str(cases['count']).ljust(8),
                      "⬛" * int(cases['count'] / 1))
            except Exception as e:
                # print(court, str(e))
                print(court.get("full_name", "short_name").ljust(45), "~")

        res = s.get(res['next'], timeout=5).json()
        if not res['next']:
            break
