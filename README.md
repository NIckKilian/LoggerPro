
# LoggerPro will look over various log files that you add to watch.  It will determine if there is any bad logs to alert you about.
The hope
    
   -Add any type of log files from any network accessible location and bring them all into one location
     
   -Determine if there are IP addresses attempting to connect to anything that you don't trust and add them to a blocklist. Will eventually attempt to add them to any Router BlockLis   
   
   -Determine any failures in the logs and Email/Text you those failures.
     
     Logger.py  - main class

     Communicate.py - class that sets up Texting to your phone or emailing

     pullLogfiles.py - on load it will pull copies of the log files and put them into the log files directory to then process (so no reall log files should be touched)

     settings.py - get the log file paths to donwload and various other settings the program will have (currently connecting to a mongo DB


