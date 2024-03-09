from utils import make_session, make_endpoint


def investments(query: str = "bitcoin"):
    """Lets query for investments

    Choose your favorite investments trend here.
    """
    session = make_session()
    url = make_endpoint("investments")

    params = (
        ("description__icontains", query),
    )
    resp = session.get(url, params=params, timeout=15).json()
    print("\n===============")
    print(f"Results count: {resp['count']}")
    last_file = None
    last_judge = None
    for inv in resp["results"]:

        r = session.get(inv['financial_disclosure']).json()
        p = session.get(r['person']).json()
        judge = f"{p['name_first']} {p['name_middle']} {p['name_last']}"
        if judge != last_judge:
            print(f"\nJudge: {last_judge}")
            print(r['filepath'])
            last_judge = judge
        print(inv['gross_value_code'].ljust(10), inv['description'])


def large_investments():
    """Lets query for large investments

    # https://whitney.org/collection/works/42027
    Choose your favorite investments trend here.
    """
    people = []
    values = {
        "P1": "1,000,001 to 5,000,000",
        "P2": "5,000,001 to 25,000,000",
        "P3": "25,000,001 to 50,000,000",
        "P4": "50,000,001 +",
    }
    session = make_session()
    url = make_endpoint("investments")
    codes = ["P1", "P2", "P3", "P4"]
    for code in codes:
        params = (
            ("gross_value_code", code),
        )
        resp = session.get(url, params=params, timeout=15).json()
        print(resp['count'], "Large Investments found")
        for inv in resp["results"]:
            r = session.get(inv['financial_disclosure']).json()
            print("")
            p = session.get(r['person']).json()
            print(f"{p['name_first']} {p['name_middle']} {p['name_last']}")
            print(r['filepath'])
            print(inv['description'], inv['gross_value_code'])
            print(values[inv['gross_value_code']])

