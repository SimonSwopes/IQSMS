# IQSMS
A small passion project that text a target number an inspirational quote.
[Quotes DataBase](https://sharpquotes.com/download-45500-famous-motivational-quotes-database-in-excel-and-pdf/)
It will remove the quote sent to avoid sending the same quote multiple times.
There are 45,000 unique quotes and their authors.

The only file that needs to be changed is the main file.
You will need a Twilio account in order to send the texts. They do a free trial with $15 worth of texts.
I scheduled the program to run at a specified time through the Task Scheduler on Windows11.
To download just download the Zip folder it contains all the files shown in the repository

Make sure you have python3 installed as well as the depenedent libraries.
Make sure you add it to the path.
[Python Download](https://www.python.org/downloads/)

Now for the Dependencies
[In the command prompt type these lines]
/code py -m ensurepip --upgrade
/code pip install twilio
/code pip install pandas
