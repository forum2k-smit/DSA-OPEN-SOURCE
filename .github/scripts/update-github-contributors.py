import urllib.request
import json

REPO = "forum2k-smit/DSA-OPEN-SOURCE"
DISPLAY_MAINTAINER_TAG = True
NAME_MAINTAINER = "rishabh-live"

f = open("./README.md", "r")

fileArray = f.read().split('\n')
f.close()

indexPos = fileArray.index("<!-- START:github_contributors -->")
endPos = fileArray.index("<!-- END:github_contributors -->")
# print(fileArray)
del fileArray[indexPos+1:endPos]
# print(fileArray)
# print(indexPos)

writeData = "<!-- START:github_contributors -->\n<center><table style=\"width:100%;\"><tr><td><b>Profile</b></td><td><b>Username</b></td><td><b>Contributions</b></td></tr>\n"
url = "https://api.github.com/repos/"+REPO+"/contributors"

response = urllib.request.urlopen(url)

data = json.loads(response.read())
i = 1
for x in data:
    profilePic = x["avatar_url"]
    username = x["login"]
    contributions = str(x["contributions"])
    if DISPLAY_MAINTAINER_TAG == True:
        if username == "rishabh-live":
            username = username + " (maintainer)"

    writeData = writeData +"<tr><td><img src='"+profilePic+"' height='50' style=\"border-radius: 50%;-webkit-box-shadow: 0px 0px 15px 0px rgba(135, 135, 135, 1);-moz-box-shadow:0px 0px 15px 0px rgba(135, 135, 135, 1);box-shadow:0px 0px 15px 0px rgba(135, 135, 135, 1);border: 5px solid #1C6EA4;\"/></td><td><a href=\"https://github.com/" +username+"/\" target=\"_blank\" style=\"color:white;\"><button style=\" width:100%; background: #42aef5;  background-image: -webkit-linear-gradient(top, #42aef5, #2980b9)background-image: -moz-linear-gradient(top, #42aef5, #2980b9);background-image: -ms-linear-gradient(top, #42aef5, #2980b9);background-image: -o-linear-gradient(top, #42aef5, #2980b9);background-image: linear-gradient(to bottom, #42aef5, #2980b9);-webkit-border-radius: 60;-moz-border-radius: 60;border-radius: 60px;font-family: Arial;color: #ffffff;font-size: 15px;padding: 10px 20px 10px 20px;text-decoration: none;\">"+username+"</button></a></td><td><label style=\"font-size:18px;color:red; font-weight:bold;\">"+contributions+"</label></td></tr>\n"


fileArray[indexPos] = writeData+"</table></center>\n"
# print(fileArray)

theData = ""
for words in fileArray:
    theData = theData + words + "\n"

theData = theData.strip()

f = open("./README.md", "w")
f.write(theData)
f.close()
print(theData)
