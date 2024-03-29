# All the regex
url_regex = r'\w+\:\w+\.\w+\.\w+'
resource_regex = r'("|\'){1}(/[\w\/]+)("|\'){1}'
file_regex = r'\w+\.\w+'
jwt_regex = r'^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$'


# Grabbed from
# https://www.networkinghowtos.com/howto/common-user-agent-list/
user_agents_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',                                                          # Chrome

    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',                                                                                               # Firefox

    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',                                             # Edge

    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',                                                                                                                      # IE 6
    'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',                                                                                                                    # IE 7
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',                           # IE 8
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)',                                                                                                # IE 9
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)',                                                                                                     # IE 10
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',                                                                                           # IE 11

    'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',                                              # iPad
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',                                    # iPhone

    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',                                                                                                     # Googlebot
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',                                                                                                      # Bing Bot
    
    'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',        # Samsumg Phone
    'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',            # Samsung Galaxy Note 3
    'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',        # Samsung Galaxy Note 4

    'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',                           # Google Nexus
    
    'Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',                                        # HTC

    'curl/7.72.0',                                                                                                                                                                   # cURL

    'Wget/1.20 (linux-gnu)',                                                                                                                                                         # Wget

    'Lynx/2.8.8pre.4 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.12.23'                                                                                                                    # Lynx
]

# list of headers to be shown to the user!
notable_headers = [
    'server',
    'x-provided-by',
    'content-security-policy'
    'x-powered-by'
]
