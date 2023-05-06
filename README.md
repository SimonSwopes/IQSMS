# IQSMS
##A small passion project that texts a target number an inspirational quote.

All quotes are from an online Database. There is an excel document in this repo but I have also linked
the download for the Database.
[Quotes DataBase](https://sharpquotes.com/download-45500-famous-motivational-quotes-database-in-excel-and-pdf/)
The program will remove a quote once it's to avoid sending the same quote multiple times. This does imply that
an error will occur once all quotes have been used.
There are 45,000 unique quotes and their authors.

The only file that needs to be changed is the main file.
You will need a Twilio account in order to send the texts. They do a free trial with $15 worth of texts.
[Twilio](https://www.twilio.com/try-twilio?g=/console/twilio-org/sign-up&t=8dde217189bbda6d29cbac8981a52301b544b5acbeb7a9d9eeccedd4b7f365c9&channel=dotorg_website&utm_medium=cpc&utm_source=google&utm_campaign=GS-Brand-Twilioorg-NA)
I scheduled the program to run at a specified time through the Task Scheduler on Windows11. If you do this make sure you make a batchfile with the correct paths.
To download just download the Zip folder it contains all the files shown in the repository

Make sure you have python3 installed as well as the depenedent libraries.
Make sure you add it to the path.
[Python Download](https://www.python.org/downloads/)

Now for the Dependencies
In the command prompt type these lines
'''console
py -m ensurepip --upgrade
pip install twilio
pip install pandas
'''
