

#function for cleaning Text
def process_text(record):
    """ Tokenize text and remove stop words."""
    text = record['text']
    stopWords = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also','am', 'among', 'an', 'and', 'any'
    ,'are', 'as', 'at', 'be','because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear','did', 'do', 'does'
    , 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers'
    , 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is','it', 'its', 'just', 'least', 'let', 'like'
    , 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor','not', 'of', 'off', 'often'
    , 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so'
    , 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too'
    , 'twas', 'us', 've', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which','while', 'who', 'whom'
    , 'why', 'will', 'with', 'would', 'yet', 'you', 'your',  'NA',  '..........', '%', '@']
    words = [''.join(c for c in s if c not in string.punctuation) for s in text]
    no_stops = [word for word in words if word not in stopWords]
    return {'label':record['label'], 'words':no_stops}







#Function to count the words
def count_word(record, index):
    return record.features[index]






#Function to classify a test record
def classify_test_record(record, log_pos_prior, log_neg_prior, log_pos_probs, log_neg_probs):
    words = np.array(record.features)
    pos_prob = log_pos_prior + np.dot(words, log_pos_probs)
    neg_prob = log_neg_prior + np.dot(words, log_neg_probs)
    if pos_prob > neg_prob:
        return 1
    else:
        return 0







#Function to build a Naive bayes Classifier from scratch and classify documents
def build_naive_bayes():
    """
    Building the Naive Bayes from Spark
    """
    import string, numpy as np
    from collections import Counter
    from pyspark.mllib.classification import NaiveBayes
    from pyspark.mllib.linalg import Vectors
    from pyspark.mllib.regression import LabeledPoint
    #loading the files
    path = "/Users/abhisheksingh29895/Desktop/courses/CURRENT/Advance_Machine_Learning/HW2/aclImdb/"
    train_pos = sc.textFile(path + "train/pos/*txt").map(lambda line: line.encode('utf8')).map(lambda line: line.split())
    train_neg = sc.textFile(path + "train/neg/*txt").map(lambda line: line.encode('utf8')).map(lambda line: line.split())
    test_pos = sc.textFile(path + "test/pos/*txt").map(lambda line: line.encode('utf8')).map(lambda line: line.split())
    test_neg = sc.textFile(path + "test/neg/*txt").map(lambda line: line.encode('utf8')).map(lambda line: line.split())
    #Binding the Positive & Negatives sets
    train = train_pos.map(lambda x: {'label':1, 'text':x}).union(train_neg.map(lambda x: {'label':0, 'text':x}))
    test = test_pos.map(lambda x: {'label':1, 'text':x}).union(test_neg.map(lambda x: {'label':0, 'text':x}))
    #Processing the test
    train = train.map(process_text)  ;  test = test.map(process_text)
    #Creating a dictionary
    vocabulary_rdd = train.flatMap(lambda x: x['words']).distinct()
    vocabulary = vocabulary_rdd.collect()
    #Function to count the number of words for this
    def count_words(record):
        word_counts = Counter(record['words'])
        word_vector = []
        for word in vocabulary:
            word_vector.append(word_counts[word])
        label = record['label']
        features = Vectors.dense(word_vector)
        return LabeledPoint(label, features)
    #
    #Word count on each of the file
    train_data = (train.map(count_words).repartition(16))
    test_data = test.map(lambda record: count_words(record)).repartition(16)
    #making our own model
    total_training = train.count()
    pos_prior = train_pos.count() * 1.0/ total_training  ;  neg_prior = 1 - pos_prior  ;  num_unique_words = len(vocabulary)
    pos_total_words = train_data.filter(lambda x: x.label == 1).map(lambda x: sum(x.features)).reduce(lambda x1, x2: x1 + x2)
    neg_total_words = train_data.filter(lambda x: x.label == 0).map(lambda x: sum(x.features)).reduce(lambda x1, x2: x1 + x2)
    vocabulary_rdd_index = vocabulary_rdd.zipWithIndex().collect()
    pos_word_counts = []  ;  pos_probs = []  ;  neg_word_counts = []  ;  neg_probs = []  #To store the list of all positives
    for word, index in vocabulary_rdd_index:
        word_p = train_data.filteda x: x.label == 1).map(lambda x: x.features[index]).reduce(lambda x1, x2: x1 + x2)
        word_n = train_data.filter(lambr(lambda x: x.label == 0).map(lambda x: x.features[index]).reduce(lambda x1, x2: x1 + x2)
        word_prob_p = float(word_p + 1) / (pos_total_words + num_unique_words + 1)
        word_prob_n = float(word_n + 1) / (neg_total_words + num_unique_words + 1)
        pos_word_counts.append(word_count)  ;  pos_probs.append(word_prob)
        neg_word_counts.append(word_count)  ;  neg_probs.append(word_prob)
    #Calculating the log of probabilities
    log_pos_prior ,  log_neg_prior  =  np.log(pos_prior),  np.log(neg_prior)
    log_pos_probs,  log_neg_probs  =  np.log(np.array(pos_probs)),  np.log(np.array(neg_probs))
    #Making classification based on conditional probabilities
    classifications = test_data.map(lambda x: classify_test_record(x, log_pos_prior, log_neg_prior, log_pos_probs, log_neg_probs))
    correct = classifications.zip(test_data.map(lambda x: x.label)).filter(lambda x: x[0] == x[1]).count()
    #Accuracy is
    accuracy = correct / test_data.count()
    print ""
    print "Test accuracy is {}".format(round(accuracy,4))







#Calling the main function to run the code
if __name__ == '__main__':

    print "******* Q.2) Part 2] Document Classification using my own Naive Bayes **********"
    build_naive_bayes()
    print "Done"


