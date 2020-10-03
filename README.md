# Web Analyser
Analyses Websites for you. It can grab a limited amount of things, but it's better than doing them manually:

* Robots and Sitemap
* Cookies and JWTs
* Redirects
    * Parameters in redirects are analysed using regex for potential LFI/RFI/SSRF vulnerabilities
* Comments
* URLs in the source
* Resources in the source, e.g. `/api/v2`
* Differences in responses between User-Agents

Also allows you to specify your own:
* User-Agent
* Cookies
* Username and Password (for Basic Authentication)

# Installing
```
git clone https://github.com/ir0nstone/web-analyser.git
cd web-analyser
pip3 install -r requirements.txt
```