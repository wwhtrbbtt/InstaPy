headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)"}
################
import urllib.request
import requests
import json
import os
import random
################

def downloadpics(JSON, person):
    a = 0
    pics = []
    pics = JSON["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
    
    for x in pics:
        adress = x["node"]["display_url"] # get url
        a += 1
        urllib.request.urlretrieve(adress, person + "-Pic" + str(a) + ".jpg") # download media
    print("downloaded " + str(a) + " pictures.")


def GetData(person):
    proxies = prox()
    proxy = {
     "http": (random.choice(proxies)),
     "http": (random.choice(proxies))
    }
    url = "https://www.instagram.com/" + person + "/?__a=1"
    r = requests.get(url, headers=headers, proxies=proxy)
    try:
        JSON = (r.json())
        #basic data
        cursor = JSON["graphql"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]# cursor, eventually used to get more pics then 12

        bio = JSON["graphql"]["user"]["biography"]
        sups = JSON["graphql"]["user"]["edge_followed_by"]["count"]
        following = JSON["graphql"]["user"]["edge_follow"]["count"]
        TotalPics = JSON["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]

        #basic media
        ProfilePic = JSON["graphql"]["user"]["profile_pic_url_hd"]# get url of pb
        urllib.request.urlretrieve(ProfilePic, person + "-ProfilePic.jpg") #download profile picture


        print(person + " has " + str(sups) + " followers, and follows " + str(following) + " people. The account posted " + str(TotalPics) + " pictures/videos in total. The bio is:\n " + str(bio))

        if JSON["graphql"]["user"]["is_private"] == True:
            print("Cant download any media except profile picture, because the profile if private /:")
        else:
            downloadpics(JSON, person)
    except:
        print(url)
        a = 0
def prox():
    r = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http", allow_redirects=True)
    open('proxies.txt', 'wb').write(r.content)
    with open("proxies.txt") as f:
        proxies = f.readlines()
    return proxies
##input = input("You can either do single or multi mode. If you want to do single, just enter a name. If you want to do a file, enter file:\n")
##
##if input == "file":
##    print("ok, gonna check the whole file lol")
##    with open("names.txt") as f:
##        persons = f.readlines()
##        for person in persons:
##            GetData(person, proxies)
##else:
##    person = input
def path(person):
    path = person + "-media/"
    try:
        os.mkdir(path)
    except:
        print("failed to ceate directory, most likely because it already exists.")
    os.chdir(path)
##    print("Ok, you are getting info about " + person)
##    GetData(person, proxies)
##

#####getting proxies, idk if you can get an IP-ban


