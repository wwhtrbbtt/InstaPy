headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)"}
################
import urllib.request
import requests
import json
import os
import random
import youtube_dl
#from pytube import *
################

#CONTROLLER

def controller(values):
    mode = values[0]
    path = values[1]
    url = values[2]
    print("mode = " + mode)
    print("path = " + path)
    print("url = " + url)

    if mode == "Youtube video (enter url)":
        print("selected yt download mode, downloading from " + url)
        pathDef("VideoDownload", path)
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        #YouTube(url).streams.first().download(pathDef("YouTube Downloader", path)) # Imagine putting something on pippy, that doesnt fucking work
        
    elif mode == "Instagram - Profile (enter name)":
        print("selected instagram profile scaper mode - downloading data from " + url)
        pathDef(url, path)
        Instagram(url)
        
    

def pathDef(name, path):
    path = path + "/" + name + "-media/"
    
    try:
        os.mkdir(path)
        os.chdir(path)
    except:
        print("failed to ceate directory, most likely because it already exists.")
    print(path)
    


#INSTAGRAM
def downloadpics(JSON, person):
    a = 0
    pics = []
    pics = JSON["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
    
    for x in pics:
        adress = x["node"]["display_url"] # get url
        a += 1
        urllib.request.urlretrieve(adress, person + "-Pic" + str(a) + ".jpg") # download media
    print("downloaded " + str(a) + " pictures.")


def Instagram(person):
    url = "https://www.instagram.com/" + person + "/?__a=1"
    r = requests.get(url, headers=headers)
    try:
        JSON = (r.json())
        #basic data
        cursor = JSON["graphql"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]# cursor, eventually used to get more pics then 12. Or not.

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
        
def pathDef(name, path):
    path = path + "/" + name + "-media/"
    
    try:
        os.mkdir(path)
        os.chdir(path)
    except:
        print("failed to ceate directory, most likely because it already exists.")
    print(path)
    return path



