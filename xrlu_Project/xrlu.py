from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv
import sys

video_Info = [["Count", "Title", "Video Link"]]

for i in range(1,615):
    if i%10 == 0:
        print("----------------the "+str(i)+"th video---------------")
    req = Request('https://www.xrlu.com/videos/'+str(i), headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    title = soup.prettify()[(soup.prettify().find("<title>")+7):(soup.prettify().find("动漫")-3)].strip()
    title = title.encode("gbk", "replace").decode('gbk', 'strict')
    video_Link = soup.prettify()[(soup.prettify().find("url: '")+6):(soup.prettify().find(".mp4")+4)].strip()
    new_Vid = [i,title,video_Link]
    video_Info.append(new_Vid)
    
with open('video_Links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(video_Info)
    
    
#create 2d list to store video informations
video_Info = [["Count", "Title", "Video Link"]]

#for loop to got through all videos
for i in range(1,615):
    if i%10 == 0:
        print("----------------the "+str(i)+"th video---------------")
    #request webpage html
    req = Request('https://www.xrlu.com/videos/'+str(i), headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    #create a soup
    soup = BeautifulSoup(webpage, 'html.parser')
    # search for title within the html file
    title = soup.prettify()[(soup.prettify().find("<title>")+7):(soup.prettify().find("动漫")-3)].strip()
    title = title.encode("gbk", "replace").decode('gbk', 'strict') #take out invalid characters
    # search for video link within html file
    video_Link = soup.prettify()[(soup.prettify().find("url: '")+6):(soup.prettify().find(".mp4")+4)].strip()
    #save count, title, video link into a list 
    new_Vid = [i,title,video_Link]
    #save list into the 2d list
    video_Info.append(new_Vid)
    
#write 2d list into csv
with open('video_Links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(video_Info)
    
    
    
