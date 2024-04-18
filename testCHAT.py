import datetime
import requests

today = datetime.datetime.now()
date = today.strftime('%Y/%m/%d')

url = 'https://wikidata.org/w/rest.php/wikibase/v0/entities/items/Q42'

headers = {
  'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4NDAyMDg2ZGM5MTVlMDMxNDBlMjBhMGVlZWUwNjlkNiIsImp0aSI6ImQ0MWM1ZTU2NWIzMWQ1ZTkzMmE5ZDhhMjY1ZjY4ODVlYzU3ZGM4YWYyZDM5OTk5MGYyNmU0MDU3NTA4NmE5YWUwMjAyZWIyMWMzOGI5MDI4IiwiaWF0IjoxNzEzMjMyNDU5LjkyMzgwMiwibmJmIjoxNzEzMjMyNDU5LjkyMzgwOCwiZXhwIjozMzI3MDE0MTI1OS45MjE3MzgsInN1YiI6Ijc1NDM5NTgwIiwiaXNzIjoiaHR0cHM6Ly9tZXRhLndpa2ltZWRpYS5vcmciLCJyYXRlbGltaXQiOnsicmVxdWVzdHNfcGVyX3VuaXQiOjUwMDAsInVuaXQiOiJIT1VSIn0sInNjb3BlcyI6WyJiYXNpYyJdfQ.UqfOvVLy5dY4XQuE-fBii0llJTnRqxbD9VstJaQomboQrlbUd8ICBCvbaNAEDV74buauxDz10bpYDYUY5sgZsuFjngRnpQbtdwBVSIjo6xhDNtVjmJ_8kz29-zB0jannaKq5Kx1x10UFTOR_gmJEWJRBwTt5atGTr4i_f2-Z2XG3wGtIjuIrEc-_zjeiSr3VeBaS0rd2KykG8BrVm5ySIKVnoGmQa5U6eyKfmsvtARynM0YuLGhapT74Z60s9BSRPTfjaPPEzAsRYzTXBy4-j7sZjTMtKdAAf5eS6U6XpOmG3xQ6z19zwdwePim7rsRUR3Qxb17qS0VvxOezhT4Qi3rXq9mMj5wmnGz4ZbzQTcRAjwHqkZgN63uCQ-0R1kUulk5aXpFehpMEnuSIHT7qMZefBknWIns4zpQOvnkTnPIHtvsutHOgd_MstpaOeuMzRdbbOaQ9n8LmAh5Mna0AGxGrJwgIXO-KSA1SMFyV2QUZsko5YC1ZnGZddq5gNNJKRBUTp3MtHlOQqg0CIho6ru6KhzvgU0FfpiEDjU_99DHorVrf9bQudgR2M99TBHhNdj-OglXGEYtj2lOSgnV8ejIUAaHqUqz7w2-42d7AFWjkZm2e2-PHEYmVoDjzzwHDcnJ0CuaJkq15xWte3HQ7bI3CCnJ8Li2fHxqLlHN9MOE',
  'User-Agent': 'HDM Infinite'
}

def count_languages(wikidata_id):
    """Count the number of language versions for a Wikidata item."""
    url = f"https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbgetentities",
        "format": "json",
        "ids": wikidata_id,
        "props": "sitelinks"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'entities' in data and wikidata_id in data['entities']:
        sitelinks = data['entities'][wikidata_id].get('sitelinks', {})
        return len(sitelinks)
    return 0

print(count_languages("Q1459100"))