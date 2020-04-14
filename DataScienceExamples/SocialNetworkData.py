from DataScienceExamples.Data.SocialNetwork import users, friendships,user_ids_by_interests,interests_by_user_ids, interests
from collections import Counter
def not_the_same(user,other):
    return user["id"] !=other["id"]

def not_the_friend(user,other):
    return all(not_the_same(friend,other) for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user,foaf)
                   and not_the_friend(user,foaf)
                   )
def most_common_interests(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_ids[user["id"]]
                   for interested_user_id in user_ids_by_interests[interest]
                   if interested_user_id != user["id"]
                   )
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split()
                           )
print(friends_of_friend_ids(users[3]))
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
print(most_common_interests(users[3]))

