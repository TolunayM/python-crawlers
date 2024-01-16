import time

from googlesearch import search


def find_website(company_name):
    try:
        query = f"{company_name} official website"
        search_results = search(query, num_results=1,sleep_interval=3)
        website = next(search_results)
        return website
    except StopIteration:
        return "Web site not found"


with open('companies.txt','r',encoding='utf8') as file:
    lines = file.readlines()
    for line in lines:
        company_name = line
        website = find_website(company_name)
        print(website)

