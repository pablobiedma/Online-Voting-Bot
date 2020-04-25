import requests, json, time, bs4, re

def parser(step,text):
    if step == 0:
        soup = bs4.BeautifulSoup(text,'lxml')
        token = soup.find('input',{'name':'_token'})['value']
        print(token)
        return token
    elif step == 1:
        res = re.findall(re.compile('\/(.*?)\/vote\/(.*?)\\n'),text)
        if len(res) != 0:
            print('https:/'+res[0][0]+'/vote/'+res[0][1].split('\\')[0])
            return 'https:/'+res[0][0]+'/vote/'+res[0][1].split('\\')[0]
        else:
            return False
    elif step == 2:
        soup = bs4.BeautifulSoup(text,'lxml')
        table = soup.find('table',{'id':'proxylisttable'})
        working_proxies = []
        for ele in table.findAll('tr'):
            res = [x.text for x in ele.findAll('td')]
            if len(res) != 0:
                working_proxies.append([res[0],res[1]])
        return working_proxies

def get_email(email=False, check=False):
    'https://api.internal.temp-mail.io/api/v2/email/yh3rt7m9yn@safemail.icu/messages'
    s1 = requests.session()
    s1.verify = False

    headers_get = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'es-ES,es;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://temp-mail.io',
        'pragma': 'no-cache',
        'referer': 'https://temp-mail.io/en',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Mobile Safari/537.36',
    }
    if email != False:
        s1.verify = False
        url = s1.post('https://api.internal.temp-mail.io/api/v2/email/new',headers=headers_get, json={"min_name_length":10,"max_name_length":10})
        new_email = json.loads(url.text)['email']
        return new_email

    if check != False:
        url2 = s1.get('https://api.internal.temp-mail.io/api/v2/email/{}/messages'.format(check),headers=headers_get)
        #print(url2.text)
        res2 = parser(1,url2.text)
        if res2 != False:
            vote_link = res2
            return vote_link
        else:
            return False

    #input(url.text)
    #input(url2.text)
    #print(new_email)
    #print(url2.text)
def scrape_proxies():
    headers_get_3 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    s = requests.session()
    s.verify = False
    s.allow_redirects = True

    url = s.get('https://www.sslproxies.org/', headers=headers_get_3)

    #input(url.text)
    return parser(2,url.text)
def filter_prox(prox4):
    working = []
    #input(prox4)
    print('testing {}'.format(prox4))
    try:
        prox = {'http':'http://{}'.format(prox4),
                'https':'http://{}'.format(prox4)}
        #print(proxu)
        #input(prox)
        requests.get('https://contest.com/candidate/6969', proxies=prox, timeout=15)
        print('working > {}'.format(prox4))
        #working.append(prox4)
        return True
    except:
        return False
def get_new_proxie():
    global already_used_proxies
    for ie in [(x[0] + ':' + x[1]) for x in proxy]:
        if ie not in already_used_proxies:
            if filter_prox(ie) == True:
                already_used_proxies.append(ie)
                return ie
            else:
                print('Not working proxie > {}'.format(ie))
                already_used_proxies.append(ie)
        else:
            print('Already used proxie...')

    #amzon_sc('https://www.amazon.com/s?me=A3T35W8YQ26H4Z&marketplaceID=ATVPDKIKX0DER', ie)
def do_vote(proxy):
    headers_get = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'es-ES,es;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': '',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    headers_post = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'es-ES,es;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://contest.com',
        'pragma': 'no-cache',
        'referer': 'https://contest.com/candidate/6969',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }
    s = requests.session()
    s.verify = False
    s.allow_redirects = True
    proxies_pload = {
        'http':'http://{}'.format(proxy),
        'https':'http://{}'.format(proxy)
    }
    profile_data = s.get('https://randomuser.me/api/?country=us')
    res1 = json.loads(profile_data.text)['results']
    data = {}
    data['gender'] = res1[0]['gender']
    data['name'] = res1[0]['name']['first']+' '+res1[0]['name']['last']
    import random
    url = s.get('https://contest.com/candidate/6969', headers=headers_get, proxies=proxies_pload)
    new_mail = get_email(email=True)

    payload = {
        '_token': parser(0, url.text),
        'name': data['name'],
        'email': 'youremail+'+str(random.randint(6,500))+'@gmail.com',#new_mail,
        'terms': '1',
    }
    print('Voting > {}\nEmail > {}'.format(payload['name'],payload['email']))
    url2 = s.post('https://contest.com/candidate/6969/vote', headers=headers_post, data=payload, proxies=proxies_pload)
    while True:
        res2 = get_email(check=new_mail)
        if res2 != False:
            input('confirm vote')
            url3 = s.get(res2,headers=headers_get, proxies=proxies_pload)
            break
        time.sleep(5)

if __name__ == '__main__':
    already_used_proxies = []
    proxy = scrape_proxies()
    MAX_VOTES = 5

    CURRENT_VOTES = 0
    while MAX_VOTES > CURRENT_VOTES:
        aja = get_new_proxie()
        try:
            do_vote(aja)
            #do_vote('')
            CURRENT_VOTES+=1
            input('VOTE+1')
        except Exception as e:
            print('ERROR > {}'.format(str(e)))