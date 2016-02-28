
#loading the concerned libraries
import numpy as np, os, sys, random, pandas as pd
from math import sqrt



#Accepting inputs from the terminal
train_file = 'training_subset2.txt'  ;  test_file = 'testingRatings.txt'
#train_file = sys.argv[-3]  ;  test_file = sys.argv[-1]





#loading the datasets
def load(file):
    """
    :param: txt file
    :return: dataframe
    """
    data1 = pd.read_csv(file, sep = ',', header = 0)
    data1.columns = ['Movie_ID', 'User_ID', 'Rating' ]
    return data1






#Convert dataframes to a Unit matrix
def convert(df):
    """
    :param: dataframe
    :return: Utility matrix
    """
    new_df = df.pivot(index='Movie_ID', columns='User_ID', values='Rating')
    return new_df





#Filling up the utilty matrix
def fill(df):
    """
    :param: dataframe with lots of blanks
    :return: dataframe with values for each cell
    """
    dft = df.transpose()
    if (df.shape[1] < dft.shape[1]):        #Dataframe to store all similarity values
        rating = dft
    else:
        rating = df
    row_means = rating.mean(axis = 1)
    rating = rating.sub(rating.mean(axis = 1), axis = 0) #Centering values about row mean
    rating.fillna(0, inplace = True) #Treating NA's

    #Calcullating similarity
    data_ibs = rating.corr()
    data_ibs.fillna(0, inplace = True) #Treating NA's
    print "Finished computing Pearson's similarity, Now computing ratings"

    #Filling up the ratings
    data_ibs1 = data_ibs.as_matrix()  ;  rating1  =  rating.as_matrix()
    rating1 = rating1.dot(data_ibs1) / np.array([np.abs(data_ibs1).sum(axis=1)])
    rating = pd.DataFrame(rating1)
    rating.fillna(0, inplace = True) #Treating NA's

    #Adding back the row means
    m  = pd.Series(row_means.tolist(), name='mean')
    result = pd.concat([rating, m], axis=1)
    result['mean'] *=-1
    rating = result.sub(result['mean'], axis = 0)
    rating = rating.drop("mean", axis = 1)
    print "Finished computing ratings"
    return rating






#scoring the test set; Handling all cases here
def score(data, test):
    """
    :param: The training set with values, The test set, that gets scored
    :return: Test set with predicted values
    """
    stacked = data.stack()
    stacked.index.set_names('var_name', level=len(stacked.index.names)-1, inplace=True)
    data_long = stacked.reset_index().rename(columns={0:'value'})
    data_long.rename(columns={'level_0':'Movie_ID'}, inplace=True) #Changing col name
    data_long.rename(columns={'var_name':'User_ID'}, inplace=True) #Changing col name
    new_data = pd.merge(test, data_long, how = 'left', on=['Movie_ID','User_ID'])
    new_data.rename(columns={'value':'Predicted_Rating'}, inplace=True) #Changing colname to predicted

    #Handling Special Cases: New data of 3 forms
    new_data1 = new_data[pd.isnull(new_data).any(axis = 1)]
    new_data = new_data.dropna() #Getting rid of empty rows in older dataframe
    #[New_User,Same_Movie]
    movie_mean = data_long.loc[:,['Movie_ID','value']].groupby(['Movie_ID'], sort = False).mean()
    new_data1.update(movie_mean)
    new_data1['Predicted_Rating'] = movie_mean['value'].combine_first(new_data1['Predicted_Rating'])

    new_data2 = new_data1[pd.isnull(new_data1).any(axis = 1)]
    new_data1 = new_data1.dropna() #Getting rid of empty rows in older dataframe
    #[Same_User,New_Movie]
    user_mean = data_long.loc[:,['User_ID','value']].groupby(['User_ID'], sort = False).mean()
    new_data2['Predicted_Rating'] = user_mean['value'].combine_first(new_data2['Predicted_Rating'])

    #[New_User,New_Movie]
    full_mean = data_long.icol(2).mean()
    new_data2.fillna(full_mean, inplace=True)

    #Concatenating the 3 dataframes into 1 Dataframe
    frames = [new_data, new_data1, new_data2]
    result = pd.concat(frames)
    #Treating decimals
    result.Predicted_Rating = result.Predicted_Rating.round(1)

    return result







#Printing the results
def results(data):
    """
    :param: The test set with (Actual & Predicted values)
    :return: RMSE, MAE & The Test set
    """
    predictions = data['Predicted_Rating']
    targets = data['Rating']
    rmse = np.sqrt(((predictions - targets) ** 2).mean())
    mae = np.mean(np.abs((targets - predictions)))
    print "The Mean Absolute Error is",np.round(mae,2)
    print "The RMSE is",np.round(rmse,2)
    data.to_csv("predictions.txt")
    print "Predictions file exported"





# this is the main program
if __name__ == '__main__':

    print "******* loading the datasets & naming the columns **********"
    training_data = load(train_file)  ;  test_data = load(test_file)
    print "Done"

    print "******* Converting datasets to Utility matrix format **********"
    train = convert(training_data)
    print "Done"

    print "******* Predicting the missing ratings of Utility Matrix **********"
    new_train_data = fill(train)
    print "Done"

    print "******* Scoring the test set **********"
    result_data = score(new_train_data, test_data)
    print "Done"

    print "******* Outputting the results **********"
    results(result_data)
    print "Done"







