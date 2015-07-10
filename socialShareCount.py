import urllib2, json, re

print "****************************************************************"
print "******************* URL Shares Counter *************************"
print "****************************************************************"

try:
    url = raw_input("Enter the URL to be analysed: ")
    # naive validation for proper input
    match = re.findall("^(http|https)://.*", url)
    if match:
        pass
    else:
        print "Enter the URL in proper format: http(s)://(www.)domain.com"
        exit(0)
    
    # facebook
    urlFacebook = "https://graph.facebook.com/?id=" + url
    dFacebook = urllib2.urlopen(urlFacebook).read()
    data = json.loads(dFacebook)
    try:
        print "Facebook: " + str(data["shares"])
    except KeyError:
        print "Facebook: " + str(0)
            
    # twitter
    urlTwitter = "http://cdn.api.twitter.com/1/urls/count.json?url=" + url
    dTwitter = urllib2.urlopen(urlTwitter).read()
    data = json.loads(dTwitter)
    try:
        print "Twitter: " + str(data["count"])
    except KeyError:
        print "Twitter: " + str(0)
    
    # google plus
    urlGplus = "https://plusone.google.com/_/+1/fastbutton?url=" + url
    data = urllib2.urlopen(urlGplus).read()
    match = re.findall('window.__SSR = {c: ([\d]+)', data)
    if match:
        print "Google Plus: " + str(match[0])
    else:
        print "Google Plus: " + str(0)
            
    # linkedin
    urlLinkedin = "http://www.linkedin.com/countserv/count/share?url=" + url + "&format=json"
    dLinkedin = urllib2.urlopen(urlLinkedin).read()
    data = json.loads(dLinkedin)
    try:
        print "LinkedIn: " + str(data["count"])
    except KeyError:
        print "LinkedIn: " + str(0)
        
    # stumbleupon
    urlStumble = "http://www.stumbleupon.com/services/1.01/badge.getinfo?url=" + url
    dStumble = urllib2.urlopen(urlStumble).read()
    data = json.loads(dStumble)
    try:
        print "StumbleUpon: " + str(data["result"]["views"])
    except KeyError:
        print "StumbleUpon: " + str(0)
        
    # pinterest
    urlPinterest = "http://api.pinterest.com/v1/urls/count.json?url=" + url
    dPinterest = urllib2.urlopen(urlPinterest).read()
    dPinterest = dPinterest[dPinterest.find("(")+1:dPinterest.find(")")]
    data = json.loads(dPinterest)
    try:
        print "Pinterest: " + str(data["count"])
    except KeyError:
        print "Pinterest: " + str(0)
        
    # reddit
    # reddit may limit automated user-agents like python/urllib.
    # a solution is to fake the user-agent.
    # I've just made sure the program doesnt terminates in that case.
    try:    
        urlReddit = "http://www.reddit.com/api/info.json?&url=" + url
        dReddit = urllib2.urlopen(urlReddit).read()
        dReddit = json.loads(dReddit)
        ups = 0
        downs = 0
        for i in dReddit["data"]["children"]:
            ups += int(i["data"]["ups"])
            downs += int(i["data"]["downs"])
        print "Reddit: " + str(ups - downs)
    except HTTPError:
        print "Reddit is not behaving. Try again later."
        
    # vkontakte
    urlVk = "https://vk.com/share.php?act=count&index=1&url=" + url
    dVk = urllib2.urlopen(urlVk).read()
    print "VKontakte: " + str(dVk[18:len(dVk)-2])


except KeyboardInterrupt:
    pass

finally:
    print "\nFork me on Github!"