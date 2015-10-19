__author__ = 'abhisheksingh29895'

from BeautifulSoup import BeautifulSoup
import requests
import json
import urllib2
import feedparser
import sys
import pandas as pd

######-----------------Begin problem 1
'''
Tried it in command line. PFB, the code i used in the command line:
given url ="www.forbes.com"

commands in unix

wget -p -k -w 1 http://www.forbes.com/
#Opening the index.html file that stores all the downloaded information
open www.forbes.com/index.html

#The snapshot for the output is attached with the code.
'''

######-----------------End of Problem1, Begin problem 2

def problem2():
    all_info  =  pd.DataFrame()
    for year in xrange(2000, 2010):
        url = "http://gomashup.com/json.php?fds=finance/fortune500/year/%d" % year
        request = urllib2.Request(url)
        try:
            page = urllib2.urlopen(request)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'Failed to reach url'
                print 'Reason: ', e.reason
                sys.exit()
            elif hasattr(e, 'code'):
                if e.code  ==  404:  # page not found
                    print 'Error: ', e.code
                    sys.exit()
        page  =  page.read()
        without_parans  =  page[1  :  -1]
        decoded  =  without_parans.decode('utf-8', 'ignore')
    #Correcting bad strings
        decoded1  =  decoded.replace(u'""',  '')
        results  =  json.loads(decoded1,  strict  =  False)['result']
        revenue_list,  rankbucket_list,  name_List,  year_bucket  =  [],  [],  [],  []
        for i in range(500):
            name  =  results[i].values()[1].encode('utf-8')
            revenue  =  float(results[i].values()[2])
            if (year  ==  2009 or year  ==  2008):
                revenue  =  revenue  *  1000
            else:
                revenue  =  revenue
            rank  =  int(results[i].values()[3])
            if  (rank >= 1 and rank <= 100):
                rank_bucket  =  1
            elif  (rank >= 101 and rank <= 200):
                rank_bucket  =  2
            elif  (rank >= 201 and rank <= 300):
                rank_bucket  =  3
            elif  (rank >= 301 and rank <= 400):
                rank_bucket  =  4
            else:
                rank_bucket  =  5
            revenue_list.append(revenue)  ;  rankbucket_list.append(rank_bucket)
            year_bucket.append(year)  ;  name_List.append(name)
        info  =  zip(name_List,  revenue_list,  rankbucket_list,  year_bucket)
        df  =  pd.DataFrame(info)
        df.columns  =  ['Name',  'Revenue',  'Bucket', 'Year']
        df.drop_duplicates(cols  =  'Name',  take_last  =  False)
        del df['Name']
        g1  =  df.groupby( ["Year",  "Bucket"] ).sum()
        df  =  g1.T
        df.columns  =  df.columns.droplevel()
        df.insert(0,  'Year',  year)
        df.columns  =  ['Year',  '1-100 Revenue',  '101-200 Revenue',  '201-300 Revenue',  '301-400 Revenue',  '401-500 Revenue']
        all_info  =  all_info.append(df)
    all_info  =  all_info.reset_index()
    del  all_info['index']
    #Outputting as CSV file
    all_info.to_csv('problem2.csv')

#Calling the function
problem2()


######-----------------End of Problem 2, Begin problem 3 (Kindly note this function takes about 30 secs to run)
def problem3():
    yelp  =  feedparser.parse('http://www.yelp.com/syndicate/area/rss.xml?loc=San+Francisco%2C+CA')
    files  =  yelp.values()[8]
    #Catching the urls
    all_urls,  all_business,  all_review,  all_overall_rating=  [],  [],  [],  []
    for i in range(len(files)):
        url_head  =  files[i].values()[2][0]
        url_head1  =  url_head.values()[0].encode('utf-8')
        url_split  =  url_head1.split("?")
        url  =  url_split[0]
        request  =  urllib2.Request(url)
        try:
            page = urllib2.urlopen(request)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'Failed to reach url'
                print 'Reason: ', e.reason
                sys.exit()
            elif hasattr(e, 'code'):
                if e.code  ==  404:  # page not found
                    print 'Error: ', e.code
                    sys.exit()
#Using beautiful soup to get the HTML content
        page  =  page.read()
        soup  =  BeautifulSoup(page)
        overall_ratings  =  soup.find("div", {"class": "rating-very-large"})
        ratings_str  =  str(overall_ratings)
        ratings_str1  =  ratings_str.split("=")
        str_ratings  =  ratings_str1[8].split("/")
        business_ratings  =  str_ratings[0]
        review_head  =  files[i].values()[0].values()[2]
        review  =  review_head.encode('utf-8')
        idea_head  =  files[i].values()[3]
        idea  =  idea_head.encode('utf-8')
        business_head  =  idea[  :  (len(idea)  -  14)]
        b_split  =  business_head.split(" ")
        business  =  ' '.join(b_split[4:])
#appending the information to the main lists
        all_urls.append(url)  ;  all_overall_rating.append(business_ratings)
        all_business.append(business)  ;  all_review.append(review)
    df2  =  pd.DataFrame(all_urls)
    df2.columns  =  ['Business url']
    df2.to_csv('3(b)Business_url.csv')
#Outputting 3(c) of this question
    list1  =  zip(all_business,  all_overall_rating)
    df3  =  pd.DataFrame(list1)
    df3.columns  =  ['business_name',  'Business_overall_rating']
    df3.to_csv('3(c) Business_Overall_Ratings.csv')
#outputing part (d) of third question in csv form
    list2  =  zip(all_overall_rating,  all_business,  all_review)
    df4  =  pd.DataFrame(list2)
#outputing part (d) of third question in csv form
    df4.columns  =  ['Business overall rating',  'business name',  'user review']
    df4  =  df4.reset_index()
    del  df4['index']
    df4.to_csv('3(d)Review_RSS_feed.csv')
#printing the Final list of 3(d)
    print df4

#End of function for problem 3

#Calling the above function
problem3()