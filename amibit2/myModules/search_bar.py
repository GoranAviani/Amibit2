

def get_web_url(text):
    HTTP_URL = "http://"
    HTTPS_URL = "https://"

    if text[0:2+1] == "go ": #open direct page
        return (HTTP_URL+text[3:])
    elif text[0:3+1] == "goo ":
        return (HTTP_URL+"www.google.com/?#q="+(text[4:])) #search with..
    elif text[0:3+1] == "ddg ":
        return (HTTP_URL+"www.duckduckgo.com/?q="+(text[4:])) #search with..
    else:
        return (HTTP_URL+"www.google.com/?q="+(text)) #search with...

