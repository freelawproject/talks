from utils import make_session, make_endpoint

def reimbursements(query: str):
  """Lets query for reimbursements

  Choose your favorite billionaire here.
  """
  session = make_session()
  params = (
      # ("location__icontains", q),
      # ("redacted", True),
      ("source__icontains", query), )

  url = make_endpoint("reimbursements")
  resp = session.get(url, params=params, timeout=15).json()


  # Print Counts FOund
  print(resp['count'], "Reimbursements found")
  for row in resp['results']:
    print("")
    print("Date:", row['date_raw'])
    print("Purpose:", row['purpose'])
    print("Items:", row['items_paid_or_provided'])
    print("Location:", row['location'])
    print("Redacted Y/N:", row['redacted'])

