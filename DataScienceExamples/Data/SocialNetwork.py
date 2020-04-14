from collections import defaultdict
users = [
    {"id":0,"name":"Vasya"},
    {"id":1,"name":"Sam"},
    {"id":2,"name":"Sue"},
    {"id":3,"name":"Peter"},
    {"id":4,"name":"Vova"},
    {"id":5,"name":"Clive"},
    {"id":6,"name":"Hicks"},
    {"id":7,"name":"Devid"},
    {"id":8,"name":"Kate"},
    {"id":9,"name":"Klainer"}
]
friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]
interests= [(0,"Hadoop"),(0,"BigData"),(0,"HBase"),(0,"Java"),
            (0,"Spark"),(0,"Cassandra"),(1,"NoSQL"),(1,"MongoDB"),(1,"Cassandra"),(1,"HBase"),
            (1,"Postgres"),(1,"Python"),(2,"Python"),(2,"scikit-learn"),(2,"NumPy"),(2,"pandas"),(2,"R"),
            (3,"statistics"),(3,"regression"),(3,"probability"),(4,"machine learning"),(4,"regression"),(5,"regression"),(5,"R"),(5,"statistics")
            ]
salaries_tenures = [(83000,8.7),(88000,8.1),(48000,0.7),(76000,6),(69000,6.5),(76000,7.5),(60000,2.5),(83000, 10),(48000,1.9),(63000,4.2)]
for user in users: # add property 'friends' for each user in users
    user["friends"] = []
for i,j in friendships: # for each couple (u_id,f_id) in friendships
    users[i]["friends"].append(users[j]) # add j for i as friend
    users[j]["friends"].append(users[i])# add i for j as friend
def number_of_friends(user):
    return len(user["friends"])
total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections/num_users
num_friends_by_uid = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_uid,
       reverse=True)
user_ids_by_interests = defaultdict(list)
interests_by_user_ids = defaultdict(list)
for user_id,interest in interests:
    user_ids_by_interests[interest].append(user_id)
for user_id,interest in interests:
    interests_by_user_ids[user_id].append(interest)