__author__ = 'abhisheksingh29895'

import facebook
import psycopg2
import pandas as pd

'''
I have used the below url to help answer this question
"http://facebook-sdk.readthedocs.org/en/latest/api.html"
'''

#defining the main function
def homework4():
# see Facebook Graph API: https://developers.facebook.com/docs/reference/api/
oauth_access_token  =  'CAACEdEose0cBAJ51hypynbJZCxWPOtqb9zWkwindanB6xwFj48Qgv5afkokAayuez3iOY6Oqj5q1WDjcfbjPXMLYZCvy9pgsDJVXTo3ia9vyysAHPRDXSzePnR4G9XyncpEfG5VOe0thoKx1E8SdZAZB6J1lzjZBwHeNZCEMTEVm8mE93QZCCPAUqZCFaC4fzsns37yL8z0QggZDZD'
graph  =  facebook.GraphAPI(oauth_access_token)
#Pulling the data from the Bill & Melina Gates
user1  =  'BillGates'
user2  =  'MelindaGates'
posts1  =  graph.get_connections(id  =  user1 ,  connection_name  =  'posts')
posts2  =  graph.get_connections(id  =  user2 ,  connection_name  =  'posts')
posts  =  posts1.values()[1]  +  posts2.values()[1]
#Deleting unsimilar posts
del  posts[29  :  32]
#organing the needed data
all_user,  all_message,  all_created_time,  all_post_id  =  [],  [],  [],  []
for i  in  range(len(posts)):
    user  =  posts[i].values()[3]['name']
    message1  =  posts[i]['message'].decode('ascii', 'ignore')
    hello = message1.split()
    message = ''.join(chr(i) for i in hello)
    created_time  =  posts[i]['created_time']
    post_id  =  posts[i]['id']
    all_user.append(user);  all_message.append(message);  all_created_time.append(created_time)
    all_post_id.append(post_id)
full_data  =  zip(all_user,  all_post_id,  all_created_time,  all_message)
#Converting to a dataframe
all_posts  =  pd.DataFrame(full_data)
all_posts.columns  =  ['user',  'post_id',  'created_time',  'message']
all_posts.to_csv("posts.csv")

"http://zetcode.com/db/postgresqlpythontutorial/"
#Postgreql commands in Python
createdb posts

# I Have done the querying & Database creation in postgresql software as I had difficulty in 
# installing psycopg2 library. I have been granted permission for the same from Professor Maria Daltayanni

'''
CREATE SCHEMA POSTS;

CREATE TABLE Posts_Facebook(
             User_id Text
             , Post_id Text
             , Created_Time TIMESTAMP
             , Message Text
) ;
COMMIT ;

--Loading the data from csv file to this dataframe
COPY Posts_Facebook
FROM '/Users/abhisheksingh29895/Desktop/courses/CURRENT/Data_Acquisition/HW4/post.csv'
DELIMITER ',' CSV;

--SQL queries
-- :  a) Return all user names:
SELECT User_id
FROM Posts_Facebook
group by User_id


-- : b) Return all user names:
SELECT Post_id ,Created_Time
FROM Posts_Facebook
ORDER BY Created_Time ASC


-- : c) Return all user names:
DELETE FROM Posts_Facebook
WHERE Message is NULL
--0 rows

SELECT * FROM Posts_Facebook

'''
