import threading
import requests

def fetch_url(url,results):
    response=requests.get(url)
    html_content=response.text
    results.append(f"Fetch {url}:\n{html_content}\n")

urls=[
    "https://example.com",
    # "https://www.python.org",
    # "https://www.github.com"
]
threads=[]
results=[]

for url in urls:
    thread=threading.Thread(target=fetch_url,args=(url,results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for result in results:
    print(result)

print("All URLs fetched")