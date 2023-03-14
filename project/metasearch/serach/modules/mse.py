class mse:
    def __init__(self, ua, query):
        self.userAgent = ua
        self.query = query

    def search_query(self):
        from . import scrapers
        from . import algorithms
        search = scrapers.scrapers()
        algorithms = algorithms.algorithms()
        google_results = search.search_google(self.query, self.userAgent)
        bing_results = search.search_bing(self.query, self.userAgent)
        yahoo_results = search.search_yahoo(self.query, self.userAgent)
        ddgo_results = search.search_duck_duck_go(self.query, self.userAgent)
        print("Results fetched!")
        results = []
        for result in [(google_results, "google"), (bing_results, "bing"), (yahoo_results, "yahoo"), (ddgo_results, "ddgo")]:
            if len(result[0]) == 0:
                continue
            else:
                results.append((result[0], result[1]))
        print(
            f"Google : {len(google_results)}, Bing : {len(bing_results)}, Yahoo : {len(yahoo_results)}, Ddgo : {len(ddgo_results)}")
        #print(f"results : {results}")
        ranked_results = algorithms.novel_approach(self.query, results)
        '''
        import requests
        from bs4 import BeautifulSoup
        '''
        '''
        for i in range(len(ranked_results)):
            
            url = ranked_results[i][0]
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            ti = ""
            c=1
            for title in soup.find_all('title'):
                if c==3:
                    break
                ti = ti + title.get_text() + " "
                c+=1
            ti=ti[:-1]
            unaccept = ["403 forbidden","access denied"]
            if ti[:13].lower() in unaccept :
                ti = self.query.capitalize()
            ranked_results[i] = list(ranked_results[i])
            ranked_results[i].append(ti)
            print("Titles fetched")
            '''
        '''
            ranked_results[i] = list(ranked_results[i])
            ranked_results[i].append(self.query.capitalize())
            '''

        return ranked_results
