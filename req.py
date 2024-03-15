import requests

def fetch_by_title(title):
    res = requests.get('https://openlibrary.org/search.json?title={}'.format(title)).json()
    book = res['docs'][0]
    book_key = book["key"]
    details = requests.get('https://openlibrary.org{}.json'.format(book_key)).json()
    
    value = {
        "Title": details["title"],
        "Description": details["description"],
        "Cover": details["covers"][0],
        "Authors": ", ".join(book["author_name"]),
        "Publish_Year": min(book["publish_year"])
    }

    print(value)
    return value