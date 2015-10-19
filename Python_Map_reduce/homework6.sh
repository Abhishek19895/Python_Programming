'Problem1'
sudo su hdfs
hadoop fs -mkdir /user/msan692/
hadoop fs -chown cloudera /user/msan692/
su cloudera
touch test_file.txt
hadoop fs -put test_file.txt /user/msan692/test_file.txt

'I have named the Guttenberg files as file1.txt,file2.txt,file3.txt & saved it to a path'
'Now shifting these files to HDFS along with Python files to run operations'
hadoop fs -put *.txt /user/msan692/
hadoop fs -put *.py /user/msan692/

'Problem2'
'Demo code for running on the local system & saving the Output to localsystem'
cat /home/cloudera/Data_acq_hw/*.txt | python /home/cloudera/Data_acq_hw/mapper.py 
| sort -k1,1 | python /home/cloudera/Data_acq_hw/reducer.py
 > /home/cloudera/Data_acq_hw/output1.txt

'Demo code for practise map-reduce in Hadoop for the 3 files & saving the Output' 
'Output1.txt file'
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.5.0-mr1-cdh5.3.0.jar
 -file /home/cloudera/Data_acq_hw/mapper.py -mapper "python /home/cloudera/Data_acq_hw/mapper.py"
  -file /home/cloudera/Data_acq_hw/reducer.py -reducer "python /home/cloudera/Data_acq_hw/reducer.py"
   -input /user/msan692/*.txt -output /user/msan692/output.txt

'Moving the Output from hdfs to local system'
hadoop fs -get /user/msan692/output.txt /home/cloudera/Data_acq_hw/output
