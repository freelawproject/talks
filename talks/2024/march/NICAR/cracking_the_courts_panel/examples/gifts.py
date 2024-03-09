from utils import make_session, make_endpoint


def gifts(query: str):
    """Lets query for Gifts

    Choose your favorite billionaire here.
    """
    session = make_session()
    params = (("description__icontains", query),)
    # params = ()

    url = make_endpoint("gifts")
    resp = session.get(url, params=params, timeout=15).json()

    # Print Counts FOund
    print(resp['count'], "Gifts found")
    for row in resp['results']:
        print("")
        print(row['financial_disclosure'])
        print("DESCRIPTION:", row['description'])
        print("REDACTED:", row['redacted'])
        print("SOURCE:", row['source'])
        print("VALUE:", row['value'])


def gifts_source(query: str):
    """Lets query for Gifts

    Choose your favorite billionaire here.
    """
    session = make_session()
    params = (("source__icontains", query),)
    # params = ()

    url = make_endpoint("gifts")
    resp = session.get(url, params=params, timeout=15).json()

    # Print Counts FOund
    print(resp['count'], "Gifts found")
    for row in resp['results']:
        print("")
        print(row['financial_disclosure'])
        print("DESCRIPTION:", row['description'])
        print("REDACTED:", row['redacted'])
        print("SOURCE:", row['source'])
        print("VALUE:", row['value'])


def query_judge_gifts_by_education(college: str = "harvard"):
    session = make_session()
    params = (
        ("financial_disclosure__person__educations__school__name__icontains",
         college),
    )
    url = make_endpoint("gifts")
    r = session.get(url, params=params, timeout=15).json()
    print(f"Found {r['count']}")
    while True:
        for item in r['results']:
            print((item['value'] if item['value'] else "?").ljust(14),
                  item['source'].ljust(50), item['description'])

        if r['next']:
            r = session.get(r['next'], timeout=15).json()
        else:
            break


def query_gifts_to_scotus_judges():
    """Chain between APIs

    from disclosure - to person -to position -to court - to court ID

    """
    session = make_session()
    params = (
        ("financial_disclosure__person__positions__court__id", "scotus"),
    )
    url = make_endpoint("reimbursements")
    r = session.get(url, params=params, timeout=15).json()
    print(f"Found {r['count']}")

    last_judge = None
    for item in r['results']:
        rq = session.get(item['financial_disclosure']).json()
        p = session.get(rq['person']).json()
        if p['name_last'] == last_judge:
            pass
        else:
            last_judge = p['name_last']

        judge = f"{p['name_first']} {p['name_middle']} {p['name_last']}"
        print(judge.ljust(30), item['source'], item.get("location", ""),
              item.get("purpose", ""))
