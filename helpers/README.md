# Recon

The main purpose of this class is to grab as much information as it can about the website _**without**_ attempting any kind of exploitation

##### `execute()`
Runs all the other functions in the class.

##### `robots()`
Grab [`robots.txt`](https://yoast.com/ultimate-guide-robots-txt/) and print the contents.

##### `sitemap()`
Grab [`sitemap.xml`](https://yoast.com/what-is-an-xml-sitemap-and-why-should-you-have-one/) and print the contents.

##### `cookies()`
Read the [cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) and display them as key-value pairs.

##### `get_jwts()`
Analyse the full response and use [regex](https://www.regexbuddy.com/regex.html) to attempt to locate possible [JSON Web Tokens](https://jwt.io/). <br>

If any are found, the first and second parts are decoded from base64 and printed out as plaintext. The third part is the signature, and is therefore not decoded.

##### `redirects()`
Prints out all the redirects the request undergoes. New URL parameters are then analysed using [regex](https://www.regexbuddy.com/regex.html) to calculate potential LFI/RFI/SSRF opportunities (e.g. if the parameter is of a similar sequence to a filename or a URL).

##### `comments()`
Just grab and print any [comments](https://en.wikipedia.org/wiki/Comment_(computer_programming)) in the source code.

##### `resources()`
Uses regex to identify and print potential resources in the code, e.g. `/api/v2`.

##### `user_agents()`
Cycles through a list of [User-Agents](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) to identify if the response differs between them.

# Analysis
This file just contains any helpful functions.

##### `redirect()`
As mentioned above, analyses URLs for potential LFI/RFI/SSRF vulnerabilities using [regex](https://www.regexbuddy.com/regex.html).