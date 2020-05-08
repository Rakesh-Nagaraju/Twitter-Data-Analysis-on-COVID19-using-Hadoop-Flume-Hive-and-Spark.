# Twitter-Data-Analysis-on-COVID19-using-Hadoop-Flume-Hive-and-Spark.
Project Done by: Rakesh Nagaraju, Raj Maharjan, Vy Tran as a part of CS257 Database System Principles Project, SJSU

This project aims to use the Hadoop framework to analyze unstructured data that we obtain from Twitter and perform sentiment and trend analysis using Hive on MapReduce and Spark on keyword “COVID19”. We then compare the Hive and Spark approaches to determine the best performance.

Social media has changed the way people get updates about existing or new information by providing real-time data. There are more than 330 million active users on Twitter and every day, it receives millions of tweets. Since it has a big volume of data, to find the trends or patterns of the information given, analyzing tweets in real-time is an interesting topic but challenging at the same time. 
The main objective of this project is to generate Twitter data and use it to find out people's opinions and views on a wide range of topics. In addition to that, we would analyze tweets of every user to get an opinion (positive, negative, or neutral) on a topic. This is done using Hadoop concepts, Flume, Hive, and Spark. Hadoop is one of the best tools to perform such analysis as it works with different types of data such as streaming data or distributed big data. In this project, we are extracting the data from Twitter and then performing sentiment and trend analysis on this data. We evaluate the popular hashtags related to COVID19 which are currently trending. To achieve this, we plan to use Apache flume for data extraction, HDFS to store data, and Hive and Spark for analyzing the data. After this, we also compare the performance of both approaches. 
By analyzing the tweets/sentiment/hashtags, we can find out and understand the views of people on a specific topic of interest. However, the amount of data that has to be processed and stored in a database is challenging, analyzing the data for the sentiment and performance is also a challenging task. The direct benefit of this project will be any twitter account holder who wants to analyze the sentiment or trend analysis of other people on any topic including or excluding COVID19.


# Functional requirements 
The functional requirements are as follows:
The system should be able to extract Twitter data and store it in HDFS for further analysis.
The system should be able to process new tweets stored in the database after retrieval.
The system should be able to analyze data and classify each tweet’s polarity.
Calculate the sentiment of a tweet and store in the database, for later querying.
The system should be able to determine the recent trend pattern among the given data.
Finally, plot a graph to analyze the performance of the hive and spark approaches in querying databases.

# Non-functional requirements 
Performance requirements: We need to detect if the system crashed or hanged, also in case of an operating system error occurred. We need to make sure to keep track of the system's performance in terms of efficiency of integration. 

Safety requirements: The operation of the database ‘s backups should take place weekly in case of possible loss, damage, or harm that could result from system issues. 

Security requirements: Only authorized people are allowed to use and access the database but anyone can access and use the portal. 

Quality Attributes
Reliability: The project should deliver all the solutions mentioned in this project to the user. The solution should be tested, debugged completely, and is available and executing perfectly. If there are any errors or exceptions, they should be handled.
Accuracy: The result should be accurate and be able to prove the concept of the project.

# Software and Hardware Requirements
Server/System Software Requirement
Host Operation System: Windows / IOS 
Guest Operating System(Virtual Machine): Ubuntu 18.04.4 LTS
VMware Workstation Pro
HDP Sandbox 3.0
Java, Open Source Programming language
Apache Flume 1.6.0
Hadoop 2.7.0
Apache Hive
Apache Spark 
Twitter API

# Hardware Configuration
Processor:  Core  i3 or higher processor system
RAM: 8 GB or higher
Hard-disk: 100 GB or above
Platform: Ubuntu

# Analysis 
Sentiment analysis: 
Sentiment analysis is a process of determining the attitude of the mass id positive, negative or neutral towards the subject of interest. First, using Hive, we move unstructured data obtained in JSON format into structured format Hive tables. We also fetch a dictionary file. Then, we execute queries to create multiple views by combining the data with the dictionary words to determine the tweet’s polarity. The polarity includes:
Positive: the tweet mentions positive connotations or has a positive/happy attitude. The positive sentiment has to be more dominant if the tweet includes more than one sentiment.
Negative:  the tweet mentions negative connotations or has a negative/sad attitude. The negative sentiment has to be more dominant if the tweet includes more than one sentiment.
Neutral: If the tweet doesn’t include any personal sentiment/opinion or no particular sentiment stands out in the tweet.

Trend Analysis: 
A tweet will be always attached to multiple ‘#’(hashtags) and trend analysis includes finding out which hashtags are most shared and talked about. A topic is trending only many posts with a certain hashtag are shared or posted in a short duration of time. Hence, we use recent data for our analysis. To perform this, the unstructured data extracted from Flume into HDFS is directly read and processed using Python, Pyspark, and Apache Spark to represent the recent trending topics that are related to the COVID-19. For example, France has been trending recently on twitter during the corona pandemic. Our analysis aims to get such trending topics that are related to COVID-19.

Performance Analysis: 
Performance analysis includes comparing the hive and spark approaches to determine which approach is faster in processing the data. We store the time taken to execute queries in the hive and also the time is taken by spark on the same amount of data and varying them. Finally, plot a graph based on this data to a better approach.

# Implementation
# NOTE: 
        Make the FilePath changes as per your systems location or store the files as per the locations in this implementation.
# Signing up a Twitter developer account
In order to get Twitter data for sentiment and trend analysis, we need to sign up for a developer account and create an application.
Open developer.twitter.com/en/apps and create an app. Fill in all required fields for our purpose of using the Twitter data to the Twitter team. 
After the request got approved from the Twitter reviewing team, we were granted consumer key, consumer secret, access token, and access token secret.

# Setting up the virtual environment
The installation of Hadoop, Flume, Hive, and Spark is easier and less hassle in Linux OS. Since we have either Windows or MAC operating systems, the team set up a virtual environment using a 3rd party application called VMWare workstation player or Oracle virtual box.

# Configuring/ starting Flume Agent:
Steps to install and run Apache Flume,Hadoop services 

1.	Both Apache flume and Hadoop File System(HDFS) work seamlessly on Linux Operating System so it is recommended for the user to have  Flume Agent and HDFS installed on Linux Operating System. However with the users who are using Mac or Windows they need to install any virtual machine application such as VMware Workstation Pro or Oracle Virtual Box. For our project, we have installed VMware workstation pro. One can download the VMware workstation pro setup file  from the following link https://www.vmware.com/products/workstation-pro.html . Once the file is downloaded one can just setup the software following the steps displayed on the screen .

2.	After VMWorkstation Pro software is installed we need to set up a new virtual Machine. Again this is just a simple straight step where the user needs to click on the ‘Create a New Virtual Machine’ button displayed on the home page and the user is asked to provide all  the specifications for the virtual machine they wanted to set up. Once all the steps are completed  we have successfully set up a new virtual machine. 

3.	 After setting up a new virtual machine, it is now time for us to install and configure Apache Flume on our new Virtual Machine. Apache Flume is an open source application so we can download the software free of cost visiting the following link https://flume.apache.org/download.html . There are multiple versions of Apache Flume available but for the project we have used flume version 1.6.0. There are 2 types of Apache Flume setup file available one is with the suffix of bin.tar.gz and the other is src.tar.ga. Among the two we need to choose the file with a suffix bin.tar.gz. After downloading the file it gets a file in a zip format. So we just need to unzip and extract the files out of that zipped folder.

4.	Extracting the file will install Flume in the Virtual Machine. So in order to check that Flume has installed correctly in our Virtual Machine we need to open a new terminal and type the following commands
                                   getit .bashrc
                                   source . bashrc
                                   flume-ng
After entering the above commands if the Flume has been installed correctly in our system then it will display all  the help commands for Flume agent.  After confirming that we have installed Flume correctly then it is now time to configure Flume to extract Twitter data. For that we need to create a config file under the conf folder of the directory where we have installed the Flume application. In our case our conf file is located at the following location 
           /usr/local/hadoop-env/flume-1.6.0/conf

          In order in create a conf file we can open any text editor and specify the following properties such as   
          Flume agent name,  source where the data is being extracted, channel which is a temporary data 
          Staging storage and finally sink information  which is our destination where the data is finally stored. 
          Here is the  code snippet of our config file. If you need to explore more on the config file please check for      
          the file twitter-flume-hdfs.conf on our project package.
   
twtagent.sources = Twitter
twtagent.channels = memchannel
twtagent.sinks = HDFS


# Source Information

t.sources.Twitter.type = org.apache.flume.source.twitter.TwitterSource
twtagent.sources.Twitter.type = com.cloudera.flume.source.TwitterSource


# Sink Information

twtagent.sinks.HDFS.channel = memchannel
twtagent.sinks.HDFS.type = hdfs
twtagent.sinks.HDFS.hdfs.path = hdfs://localhost:9000/twitter_Extract/

# Channel Information

twtagent.channels.memchannel.capacity = 10000
twtagent.channels.memchannel.type = memory
twtagent.channels.memchannel.transactionCapacity = 100

5.	After configuring Flume now we need to install the HDFS on our Virtual Machine. Again HDFS is an open source application so one can download it free of cost visiting the following URL
https://archive.apache.org/dist/hadoop/core/ . There are multiple versions of HDFS available but for our project we have installed hadoop 2.7.0.  In the download page we get two types of files one is with the suffix .src.tar.gz and the other is .tar.gz. Among the two we need to choose .tar.gz. Once the file is downloaded we need to untar the file from the terminal. We need to execute the following command in the terminal to untar our application.

Tar -xvf hadoop-2.7.0.tar.gz -C /usr/local/hadoop-env

After untarring the file we need to set up environment variables and we can do that editing .bashrc file. In order to edit .bashrc file we can open a terminal and type the following command 

gedit .bashrc

It will open the .bashrc file in edit mode and we need to set up JAVA path and  Hadoop path as follows

#HADOOP path

export HADOOP_HOME=/usr/local/hadoop-env/hadoop-2.7.0
export HADOOP_PREFIX=/usr/local/hadoop-env/hadoop-2.7.0
export HADOOP_MAPRED_HOME=${HADOOP_HOME}
export HADOOP_COMMON_HOME=${HADOOP_HOME}

export HADOOP_HDFS_HOME=${HADOOP_HOME}
export YARN_HOME=${HADOOP_HOME}
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop

#Java path
# Add Hadoop bin/ directory to PATH
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

After finishing this we need additional configuration on core-site.xml , hdfs-site.xml, yarn-site.xml and mapred-site.xml. Since we have included all the files in our project package so one can just copy the content of those files and create individual files on their instances. Just as FYI all these files needs to be created at the following location 

/usr/local/<YOUR FOLDER NAME WHERE HADOOP IS INSTALLED>/etc/hadoop

6.	Once we have configured everything it is now time to check if HDFS is installed correctly on my machine or not. To check that we need to open a new terminal and enter the following command

hadoop version

If the hadoop is installed correctly then it will display us the hadoop version and other additional information of the hadoop application. After the installation of Hadoop we need to create a directory in the hadoop system where our Twitter data will be stored. In order to create a new directory we need to enter the following command in a terminal window

hadoop fs -mkdir /<YOUR CHOICE OF FOLDER NAME>

7.	After setting up both the FLUME and Hadoop system it is now time to run the services to extract the data from Twitter. In order to start hadoop services we need to enter the following command in the terminal window

Start-all.sh

To make sure if all the Hadoop services are started correctly or not we can visit the following URL in the browser 

http://localhost:50070

If  the browser redirects to the welcome page of Hadoop system then it is confirmed that all the Hadoop services have started successfully. After starting the Hadoop services we need to start the Flume agent and extract the data from Twitter. To do so we need to enter the following command in the terminal window. When the user is executing the command he/she needs to be on the home directory where the Flume agent is installed 

./bin/flume-ng  agent -n <YOUR TWITTER AGENT NAME> -c conf -f conf/twitter-flume-<YOUR FLUME CONFIG FILE NAME> -Dflume.root.logger=INFO,console

8.	Once the process gets started we can visit the URL http://localhost:50070 and under  Utilities menu bar ,we choose Browse the file system sub menu. There we can see the folder that we created earlier and when we open that folder we can see some data files that are being extracted. We can just download that file and open it in any text editor to view its content. 



# Hive Installation:
Verifying JAVA Installation ($ java -version)
Verifying Hadoop Installation ($ hadoop version)
Download Hive from http://apache.petsads.us/hive/hive-0.14.0/.
Make sure Hive is installed and HDFS, Hadoop is configured.
Extracting and verifying Hive Archive
 $ tar zxvf apache-hive-0.14.0-bin.tar.gz
Copy the extracted files to local directory
Set up the Hive environment by copying the following path in ~/.bashrc file.
 export HIVE_HOME=/usr/local/hive
 export PATH=$PATH:$HIVE_HOME/bin
 export CLASSPATH=$CLASSPATH:/usr/local/Hadoop/lib/*:.
 export CLASSPATH=$CLASSPATH:/usr/local/hive/lib/*:.
Execute $ source ~/.bashrc to run the .bashrc file.

# Configuring Hive
To configure Hive with Hadoop, we edit the “hive-env.sh file”, located in the $HIVE_HOME/conf directory. 
The following commands redirect to Hive config folder and copy the template file:
 $ cd $HIVE_HOME/conf
 $ cp hive-env.sh.template hive-env.sh

Edit the hive-env.sh file by appending the following line: 
 export HADOOP_HOME=/usr/local/hadoop
 Hive installation is completed
But we also need an external DB server to configure the Metastore, hence we also install Apache Derby. 

# Downloading Apache Derby:
Download the file using following command:
 $ wget http://archive.apache.org/dist/db/derby/db-derby-10.4.2.0/db-derby-10.4.2.0-bin.tar.gz

Extracting and verifying Derby archive
 $ tar zxvf db-derby-10.4.2.0-bin.tar.gz

Copy the files to /usr/local/derby directory using the cp command.

Setting up the environment for Derby : edit the ~/.bashrc file and enter the following lines.
 export DERBY_HOME=/usr/local/derby
 export PATH=$PATH:$DERBY_HOME/bin
 Apache Hive
 18
 export CLASSPATH=$CLASSPATH:$DERBY_HOME/lib/derby.jar:$DERBY_HOME/lib/derbytools.jar.

Create a directory to store Metastore
 $ mkdir $DERBY_HOME/data

Configuring Metastore of Hive:
Configuring Metastore means specifying to Hive where the database is stored. You can do this by editing the hive-site.xml file, which is in the $HIVE_HOME/conf directory. First of all, copy the template file using the following command:
 $ cd $HIVE_HOME/conf
 $ cp hive-default.xml.template hive-site.xml

Edit hive-site.xml and append the following lines :
 <property>
   <name>javax.jdo.option.ConnectionURL</name>
   <value>jdbc:derby://localhost:1527/metastore_db;create=true </value>
   <description>JDBC connect string for a JDBC metastore </description>
 </property>

Create a file named jpox.properties and add the following lines into it:
 javax.jdo.PersistenceManagerFactoryClass =
 org.jpox.PersistenceManagerFactoryImpl
 org.jpox.autoCreateSchema = false
 org.jpox.validateTables = false
 org.jpox.validateColumns = false
 org.jpox.validateConstraints = false
 org.jpox.storeManagerType = rdbms
 org.jpox.autoCreateSchema = true
 org.jpox.autoStartMechanismMode = checked
 org.jpox.transactionIsolation = read_committed
 javax.jdo.option.DetachAllOnCommit = true
 javax.jdo.option.NontransactionalRead = true
 javax.jdo.option.ConnectionDriverName = org.apache.derby.jdbc.ClientDriver
 javax.jdo.option.ConnectionURL = jdbc:derby://hadoop1:1527/metastore_db;create = true
 javax.jdo.option.ConnectionUserName = APP
 javax.jdo.option.ConnectionPassword = mine

# Verifying Hive Installation: 
Before running Hive, you need to create the /tmp folder and a separate Hive folder in HDFS. Here, we use the /user/hive/warehouse folder. You need to set write permission for these newly created folders as shown below: chmod g+w

Now set them in HDFS before verifying Hive. Use the following commands:
 $ $HADOOP_HOME/bin/hadoop fs -mkdir /tmp 
 $ $HADOOP_HOME/bin/hadoop fs -mkdir /user/hive/warehouse
 $ $HADOOP_HOME/bin/hadoop fs -chmod g+w /tmp 
 $ $HADOOP_HOME/bin/hadoop fs -chmod g+w /user/hive/warehouse

The following commands are used to verify Hive installation:
 $ cd $HIVE_HOME
 $ bin/hive

On successful Installation and running the above command, you should see the Hive Terminal.

On the Other Hand, we can also download HDP Sandbox 3.0, which is a virtual machine for using HDFS, Hive and other services. More at: https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html.

For more queries regarding this Installation, please follow: https://www.tutorialspoint.com/hive/hive_installation.html



# Spark Installation:

Verifying Java Installation
 $java -version
	
Downloading Scala
Download the latest version of Scala from https://www.scala-lang.org/download/ . 

Installing Scala
 Extract the Scala tar file : $ tar xvf scala-2.11.6.tgz
 Set PATH for Scala : $ export PATH = $PATH:/usr/local/scala/bi

Verifying Scala installation
 $scala -version

Downloading Apache Spark
 Download the latest version of Spark by visiting https://spark.apache.org/downloads.html.

Installing Spark: Extracting Spark tar file using the command below:
 $ tar xvf spark-1.3.1-bin-hadoop2.6.tgz 

Moving Spark software files: Use following commands for moving the Spark software files to respective directory (/usr/local/spark).
 $ su – Password:  
 #cd /home/Hadoop/Downloads/ 
 #mv spark-1.3.1-bin-hadoop2.6 /usr/local/spark 
 #exit 

8.	Setting up the environment for Spark by adding the following line to ~/.bashrc file.
export PATH=$PATH:/usr/local/spark/bin

9.	Use the following command for sourcing the ~/.bashrc file.
$ source ~/.bashrc

10.	Verify the Spark Installation:
Use the following command for opening Spark shell.
$spark-shell

11.	On successful installation, you should see a pyspark terminal. For additional information see: 
https://www.tutorialspoint.com/apache_spark/apache_spark_installation.htm

This is about the installation process,
To perform sentiment and Trend Analysis, please follow the Readme* files assosciated which each folder.
The Readme files are self-explainatory.
