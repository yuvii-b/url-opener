import webbrowser
import time

def main():
    browser = webbrowser.get()
    url_list = []

    with open("urls.txt", "r") as f:
        urls = f.readlines()
    for url in urls:
        url = url.strip()
        if url:
            if not url.startswith(("http://", "https://")):
                url = "https://" + url
            url_list.append(url)
        
    if not url_list:
        print("No URLs found in urls.txt")
        return  
    print("Found {} URLs in urls.txt".format(len(url_list)))
    for url in url_list:
        print("Opening {}".format(url))
        browser.open(url)

if __name__ == "__main__":
    main()