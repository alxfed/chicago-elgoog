"""
cse

https://developers.google.com/custom-search/docs/tutorial/introduction

"""

import os
from googleapiclient.discovery import build


my_api_key = os.environ['API_TOKEN']
my_cse_id = '003673300674975650612:vlq44zbzywo'


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


result = google_search("McDonald's", my_api_key, my_cse_id)
print(result)