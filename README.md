# Social-Share-Counts
API to grab number of shares your site has on each of the top 8 social networks

### Sample O/P

```
Enter the URL to be analysed: http://www.gsmarena.com
Facebook: 52190
Twitter: 84039
Google Plus: 136164
LinkedIn: 150
StumbleUpon: 204250
Pinterest: 6
Reddit: 11
VKontakte: 36

Fork me on Github!
```

## Social Network APIs

### Facebook

Request:
`https://graph.facebook.com/?id=https://www.github.com`

Response:
```json
{
   "id": "http://www.github.com",
   "shares": 31684
}
```

### Twitter

Request:
`http://cdn.api.twitter.com/1/urls/count.json?url=https://github.com`

Response:
```json
{"count":14,"url":"http:\/\/github.com\/"}
```

### Google Plus

Request:
`https://plusone.google.com/_/+1/fastbutton?url=https://github.com`

This returns the +1 button. I extracted the counts using regex `window.__SSR = {c: ([\d]+)`

### LinkedIn

Request:
`http://www.linkedin.com/countserv/count/share?url=https://github.com&format=json`

Response:
```json
{"count":0,"fCnt":"0","fCntPlusOne":"1","url":"https:\/\/github.com"}
```

### StumbleUpon

Request:
`http://www.stumbleupon.com/services/1.01/badge.getinfo?url=https://github.com`

Response:
```json
{"result":{"url":"https:\/\/github.com\/","in_index":true,"publicid":"2T2aNf","views":298,"title":"GitHub \u00b7 Social Coding","thumbnail":"http:\/\/cdn.stumble-upon.com\/mthumb\/837\/17983837.jpg","thumbnail_b":"http:\/\/cdn.stumble-upon.com\/bthumb\/837\/17983837.jpg","submit_link":"http:\/\/www.stumbleupon.com\/badge\/?url=https:\/\/github.com\/","badge_link":"http:\/\/www.stumbleupon.com\/badge\/?url=https:\/\/github.com\/","info_link":"http:\/\/www.stumbleupon.com\/url\/https%253A\/\/github.com\/"},"timestamp":1436538129,"success":true}
```

### Pinterest

Request:
`http://api.pinterest.com/v1/urls/count.json?url=https://github.com`

Response:
```json
receiveCount({"url":"https://github.com","count":0})
```

### Reddit

Request:
`http://www.reddit.com/api/info.json?&url=https://github.com`

This returns a lot of data, which can be easily used to extracted counts.
**Note** that the Reddit guys don't really like automated requests and may cause the call to return HTTP 429.

### Vkontakte

Request:
`https://vk.com/share.php?act=count&index=1&url=https://github.com`

Response:
```json
VK.Share.count(1, 419);
```

## Screenshot

![screenshot](https://raw.githubusercontent.com/abhn/Social-Share-Counts/master/sharesCountScreenshot.png)
