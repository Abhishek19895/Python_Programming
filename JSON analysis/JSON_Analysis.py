__author__ = 'abhisheksingh29895'

'''
I have used the below urls to answer these questions
"http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20"
" "
'''

#loading the libraries
import json
import pandas as pd
import re
import matplotlib.pyplot as plt

'''Begin with Part 1, loading the data through a function'''

#Setting the preferences
json_file1  =  'restaurants.json'
alias  =  "lillians-italian-kitchen-santa-cruz"

#Defining a defualt parameter function for the same
def  restaurant_analysis(json_file1,  alias):
    json_data  =  open(json_file1).read()
    data  =  json.loads(json_data)
#converting dictionary to individual lists
    alias_name,  lat,  type,  ratings,  name,  price,  categories  =  [],  [],  [],  [],  [],  [],  []
    for i in data:
        l  =  i.values()[0];  t  =  str(i.values()[3]);  c  =  str(i.values()[1].values()[7])
        r  =  i.values()[1].values()[0];  a  =  str(i.values()[1].values()[6]);  n  =  i.values()[1].values()[2]
        p  =  str(i.values()[1].values()[5])
#converting to strings
        alias_name.append(a);  lat.append(l);  type.append(t);  price.append(p);  categories.append(c);
        name.append(n);  ratings.append(r)
#Merging the strings
    Full_list  =  zip(alias_name,  lat,  type,  ratings,  name,  price,  categories)
    df  =  pd.DataFrame(Full_list)
    df.columns  =  ['alias_name',  'lat',  'type',  'ratings',  'name',  'price',  'categories']
    output  =  df[(df.alias_name  ==  alias)]
    return output
'''
If You need to enter a data other than the one mentioned in the homework pdf
Kindly enter that in the function parameters
'''

#Calling the function--and storing it as an object
a  =  restaurant_analysis(json_file1,  alias)
a

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''
End of Part 1, Begin with Part 2
'''

json_file2  =  'ratings.json'

def  ratings_analysis(json_file2):
    data = []
    with open(json_file2) as f:
        for line in f:
            data.append(json.loads(line))
#converting dictionary to individual lists
    ratings,  review,  funny,  cool,  useful,  alias_name,  uid,  date  =  [],  [],  [],  [],  [],  [],  [],  []
    for i in data:
        ra  =  i.values()[0];  re  =  i.values()[3];  f  =  i.values()[5]
        c  =  i.values()[6];  use  =  i.values()[7];  a  =  str(i.values()[4])
        u  =  str(i.values()[1]);  d  =  str(i.values()[8])
    #converting to strings
        ratings.append(ra);  review.append(re);  funny.append(f);  cool.append(c);  useful.append(use);
        alias_name.append(a);  uid.append(u);  date.append(d)
#Merging the strings
    full_list  =  zip(ratings,  review,  funny,  cool,  useful,  alias_name,  uid,  date)
    df  =  pd.DataFrame(full_list)
    df.columns  =  ['ratings',  'review',  'funny',  'cool',  'useful',  'alias_name',  'uid',  'date']
    return df

#Calling the function & storing it as an object
b  =  ratings_analysis(json_file2)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''
End of Part 2, Begin with Part 3
'''

def ratings_distribution(b):
    ratings_value  =  list(b['ratings'])
    length  =  len(ratings_value)
#Calculating Average Ratings
    avg_rating  =  sum(ratings_value)  *  1.0/length
    print "The Average of ratings is ",avg_rating
#Calculating Top 5 % ratings
    sort_list  =   sorted(ratings_value,  reverse  =  True)
    len_5  =  int((5  *  length)/100)
    sub_list  =  sort_list[  :  len_5]
    avg_ratings_top5  =  round((sum(sub_list)  *  1.0)/len_5,  2)
    print "The Average of Top 5% of rating is ",avg_ratings_top5
#incorporating weighted ratings (Useful count)
    useful  =  list(b['useful'])
    useful_count  =  []
    for i in useful:
        a  =  i  +  1
        useful_count.append(a)
    full_list  =  zip(useful_count,  ratings_value)
    product  =  []
    for i in full_list:
        b  =  i[0]  *  i[1]
        product.append(b)
    w_avg_ratings  =  sum(product)*1.0/sum(useful_count)
    w_avg_ratings  =  round(w_avg_ratings,  2)
    print "The weighted Average of rating is ",w_avg_ratings
    if w_avg_ratings  > avg_rating:
        print "Restaurant looks more appealng with weighted Ratings"
    else:
        print "Restaurant looks less appealng with weighted Ratings"
#Comparing these values to yelp's estimate
    yelp_data  =  restaurant_analysis(json_file1,  alias)
    yelp  =  yelp_data['ratings'][0]
    print "The overall average rating",avg_rating,"is closest to yelp's estimation ",yelp
#plotting the ratings using matplotlib
    plt.hist(ratings_value,  histtype  =  'stepfilled')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.hist(ratings_value, bins  =  (.5,1.5,2.5,3.5,4.5,5.5))
    plt.title("Ratings distribution")
    plt.show()

#Calling the functions
ratings_distribution(b)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''
End of Part 3, Begin with Part 4
'''
def avg_n_prcnt(b,  n  =  100):
    ratings_value  =  list(b['ratings'])
    sort_list  =   sorted(ratings_value,  reverse  =  True)
    length  =  len(sort_list)
    len_n  =  int((n  *  length)/100)
    sub_list  =  sort_list[  :  len_n]
    result  =  round((sum(sub_list)  *  1.0)/len_n,  2)
    return result

#filtering out inconsistent data formats from the list
def  ratings_good_data(b):
    list_data  =  b.values.tolist()
    good_2010_data,  good_2011_data,  bad_data  =  [],  [],  []
    for  i  in  list_data:
        date  =  i[7]
        valid  =  re.match(r'^([1-9]|1[0-2])\/([1-9]|[1-2][0-9]|3[0-1])\/201[0-1]$',  date)
        date_split  =  date.split('/')
        year  =  int(date_split[2])
        if valid:
            if  year  ==  2010:
                good_2010_data.append(i)
            elif  year  ==  2011:
                good_2011_data.append(i)
            else:
                bad_data.append(i)
        else:
            bad_data.append(i)
#Filling back the 2 datasets for 2010 & 2011
    data_2010,  data_2011  =  pd.DataFrame(good_2010_data),  pd.DataFrame(good_2011_data)
    data_2010.columns  =  ['ratings',  'review',  'funny',  'cool',  'useful',  'alias_name',  'uid',  'date']
    data_2011.columns  =  ['ratings',  'review',  'funny',  'cool',  'useful',  'alias_name',  'uid',  'date']
#Calculating average of top 5% ratings for each dataframe through the user defined function
    ratings_5prcnt_2011,  ratings_5prcnt_2010  =  avg_n_prcnt(data_2011,  5),  avg_n_prcnt(data_2010,  5)
    ratings_2011,  ratings_2010  =  avg_n_prcnt(data_2011,  100),  avg_n_prcnt(data_2010,  100)
#Comparing 2011 to 2010 (Top 5% average ratings)
    ratio_2011_2010  =  ratings_5prcnt_2011  *  1.0/ratings_5prcnt_2010
#Comparing Top % ratings to overall ratings (2010)
    ratio_2010  =  ratings_5prcnt_2010  *  1.0/ratings_2010
#Comparing Top % ratings to overall ratings (2011)
    ratio_2011  =  ratings_5prcnt_2011  *  1.0/ratings_2011
#Calculating period average
    print "Average rating for Top 5% ratings of 2010 is ",ratings_5prcnt_2011
    print ""
    print "Average rating for Top 5% ratings of 2011 is ",ratings_5prcnt_2010
    print ""
    print "Average rating for all ratings of 2010 is ",ratings_2010
    print ""
    print "Average rating for all ratings of 2011 is ",ratings_2011
    print ""
    print "Ratio of top 5% of ratings 2011 to Top 5% in 2010 ",ratio_2011_2010
    print ""
    print "Ratio of top 5% of ratings of 2011 to all its ratings ",round(ratio_2011,  2)
    print ""
    print "Ratio of top 5% of ratings of 2010 to all its ratings ",round(ratio_2010,  2)

#Calling the above function and printing the output
ratings_good_data(b)


