import urllib.request
import json

REPO = "forum2k-smit/DSA-OPEN-SOURCE"

f = open("./README.md", "r")

fileArray = f.read().split('\n')
f.close()

indexPos = fileArray.index("<!-- START:github_contributors -->")
endPos = fileArray.index("<!-- END:github_contributors -->")
# print(fileArray)
del fileArray[indexPos+1:endPos]
# print(fileArray)
# print(indexPos)

writeData = "<!-- START:github_contributors -->\n<table><tr><td><b>Profile</b></td><td><b>Username</b></td><td><b>Contributions</b></td></tr>\n"
url = "https://api.github.com/repos/"+REPO+"/contributors"

response = urllib.request.urlopen(url)

data = json.loads(response.read())
i = 1
for x in data:
    # if i >= 11:
    #     break
    # try:
    #     if x["type"] == "WatchEvent":
    #         continue
    #     event = x["payload"]["commits"][0]["message"]
    #     repoName = x["repo"]["name"]
    #     url = "https://github.com/"+repoName
    #     hashKey =  x["payload"]["head"]
    #     hashUrl = "https://github.com/"+repoName+"/commit/"+hashKey

    #     writeData = writeData +"<tr><td>"+event+"</td><td><a href=\"" +url+"\">"+repoName+"</a></td><td><a href=\"" +hashUrl+"\">"+hashKey+"</a></td></tr>\n"
    #     i = i + 1
    # except:
    #     pass
    profilePic = x["avatar_url"]
    username = x["login"]
    contributions = str(x["contributions"])

    writeData = writeData +"<tr><td><img src='"+profilePic+"' height='50'/></td><td><a href=\"https://github.com/" +username+"/\" target=\"_blank\">"+username+"</a></td><td>"+contributions+"</tr>\n"


fileArray[indexPos] = writeData+"</table>\n"
# print(fileArray)

theData = ""
for words in fileArray:
    theData = theData + words + "\n"

theData = theData.strip()

f = open("./README.md", "w")
f.write(theData)
f.close()
print(theData)