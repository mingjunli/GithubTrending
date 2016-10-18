
### Github Trending API

**This is A python API to get Github Trending(repos, developers) with Flask**

### API Docs

#### 1, Trending Repos
Desc: Get Trending repos list

API: /api/github/trending/<lang>?since=(daily,weekly,monthly)

Method: GET

Request:

Parameter|Desc|Form|Type|Optional|Remark
-----|-----|-----|-----|-----|-----
lang |language|path|String|optional|similar to github trending page
since|time span|query|String|optional|daily,weekly,monthly

Response:

A Repo list, each Repo including:

Parameter|Desc|Type|Remark
-----|-----|-----|-----
avatar|owner's avatar url|String|url string
owner|owner name|String|/
repo|repo name|String|/
desc|repo description|String|/
stars|stars during the time span|int|/
link|repo address|String|/

Example:

**Request url**:

[http://anly.leanapp.cn/api/github/trending/java?since=weekly](http://anly.leanapp.cn/api/github/trending/java?since=weekly)

**Response data**:

````json
[{
    avatar: "https://avatars3.githubusercontent.com/u/69631?v=3&s=40",
    desc: "A framework for building native apps with React.",
    link: "https://github.comfacebook/react-native",
    owner: "facebook",
    repo: "react-native",
    stars: 417
},
{
    avatar: "https://avatars3.githubusercontent.com/u/4239472?v=3&s=40",
    desc: "A small android library to transition between a circular ImageView from one Activity to a rectangular ImageView in the launched Activity.",
    link: "https://github.comvikramkakkar/ImageTransition",
    owner: "vikramkakkar",
    repo: "ImageTransition",
    stars: 206
}]
````

#### 2, Trending Developers

Desc: Get Trending Developers list

API: /api/github/trending/<lang>?since=(daily,weekly,monthly)

Method: GET

Request:

Parameter|Desc|Form|Type|Optional|Remark
-----|-----|-----|-----|-----|-----
lang |language|path|String|optional|similar to github trending page
since|time span|query|String|optional|daily,weekly,monthly

Response:

A Developer list, each developer including:

Parameter|Desc|Type|Remark
-----|-----|-----|-----
avatar|developer's avatar url|String|url string
name|developer name|String|/
full_name|developer full name|String|originName(NickName)
link|developer page link|String|/

Example:

**Request url**:

[http://anly.leanapp.cn/api/github/trending/developers/java?since=weekly](http://anly.leanapp.cn/api/github/trending/developers/java?since=weekly)

**Response data**:

````json
[{
    avatar: "https://avatars3.githubusercontent.com/u/69631?v=3&s=40",
    full_name: "facebook (Facebook)",
    link: "https://github.com/facebook",
    name: "facebook"
}, 
{
    avatar: "https://avatars3.githubusercontent.com/u/4280789?v=3&s=40",
    full_name: "wangshaolei (fearless)",
    link: "https://github.com/wangshaolei",
    name: "wangshaolei"
}]
````

### Other

Since I have an opensource project --- [CoderPub](https://github.com/mingjunli/GithubApp) need the github trending data, but Github DONOT provide the trending api for developer, so, wrote this project to grab the "Github Trending Page" and use BeautifulSoup to parser it, use Flask to provide the Trending API.

This project already deployed at [LeanCloud](leancloud.cn), (free host, has limit).

You can use this URL: [http://anly.leanapp.cn/](http://anly.leanapp.cn/) visit the api.

Wish Enjoy it.

