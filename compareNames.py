#checking my list following people who are not following

following = ["a", "b", "c", "z"]
followers = ["a", "c", "e" ]

user = followers

not_following_back = [user for user in following if user not in followers]
print(not_following_back)