from googleapiclient.discovery import build

# API Key and Custom Search Engine ID
api_key = 'AIzaSyB2re0D_m7GvBV81JjUorpuCgjaMPK-g7o'

cse_id = '243607d51f37f424b'

def google_search(query):
    service = build("customsearch", "v1", developerKey=api_key)
    
    # Optional: limit search to Wikipedia by using siteSearch="wikipedia.org"
    # You can replace "wikipedia.org" with any other domain you'd like to focus on
    #res = service.cse().list(q=query, cx=cse_id, siteSearch="wikipedia.org").execute()
    res = service.cse().list(q=query, cx=cse_id).execute()

    
    # Get results from the search
    results = res.get('items', [])
    
    # Clean and return the first result's title, link, and snippet
    if results:
        top_result = results[0]
        title = top_result.get('title')  # The title of the top result
        link = top_result.get('link')  # The URL of the top result
        snippet = top_result.get('snippet')  # The description/snippet of the top result
        #return f"Top search result: {title}\nURL: {link}\nDescription: {snippet}"
        return snippet
    else:
        return "No results found."

if __name__ == "__main__":
    # Take user input for the search query
    query = input("Enter your search query: ")
    
    # Perform the search and display the result
    result = google_search(query)
    print(result)
