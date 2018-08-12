import tweepy
import os

keyFilePath = input("Enter the path to your Twitter key file: ")
keyFile = open(keyFilePath)
lines = keyFile.read().splitlines()

auth = tweepy.OAuthHandler(lines[0], lines[1])
auth.set_access_token(lines[2], lines[3])

api = tweepy.API(auth)

id = input("Enter Username: ")
lists = api.lists_all(id)

print()
print("Displaying all lists available to %s:" % id)
print()

for idx,list in enumerate(lists):
    print("%d) %s" % (idx + 1,list.name))

selectedListIdx = int(input("Enter list number to follow to list members: "), 10)
selectedList = lists[selectedListIdx - 1]

print()
confirm = input("There are " + str(selectedList.member_count) + " members in list " + selectedList.name + ".  Are you sure you want to follow them all? ")

if (confirm == 'Y'):
    print()
    print("You are now following: ")
    for member in tweepy.Cursor(api.list_members, owner_screen_name=id, slug=selectedList.name).items():
        print(member.screen_name)
        api.create_friendship(member.screen_name)