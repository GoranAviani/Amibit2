def check_url_link(urlLink):
    urlLink = check_https_on_link(urlLink)
    return urlLink




#Check does the link have http or https on the beginning, if it does not add it
def check_https_on_link(urlLink):
    HTTP_URL = "http://"
    HTTPS_URL = "https://"
    if urlLink[0:7] != HTTP_URL:
        if urlLink[0:8] != HTTPS_URL:
            urlLink = HTTP_URL + urlLink
    return urlLink



def main():
    pass

if __name__=="__main__":
    main()