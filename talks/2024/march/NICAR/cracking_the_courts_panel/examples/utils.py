import requests


def make_session():
    """Create session with NICAR24 API KEY

    :return:
    :rtype:
    """
    s = requests.session()
    NICAR_API = "d6f1a87f6ccb8dfe13494e87d50b5ca128e603b4"
    s.headers = {"Authorization": f"Token {NICAR_API}"}
    return s

def make_endpoint(endpoint: str):
    return f"https://www.courtlistener.com/api/rest/v3/{endpoint}/"



