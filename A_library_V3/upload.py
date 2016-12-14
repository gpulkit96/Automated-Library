from catalogue.models import Post
data =open('list.json')
import json
data1 =json.load(data)
i=0
n=len(data1)
while(i<n):
post = Post()
post.Title = data1[i]["Title"]
post.Author=data1[i]["Author"]
post.CallNum=data1[i]["Call Num"]
post.Publisher=data1[i]["Publisher"]
post.Genre="Competitive"
post.Status="N/A"
post.date="2016-12-14T22:11:26Z"
post.save()
i=i+1
