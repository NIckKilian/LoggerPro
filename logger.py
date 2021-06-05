import sys
from lib.settings import settings
from datetime import datetime, timedelta
import qlogging, re

# Validating IP addresses in the string (IP_Login_list)
# spit out results of logfiles in a certain amount of time default 1 week (recentLogs)

Qlogger = qlogging.get_logger(level='debug')
daysBack = (datetime.today() - timedelta(days=17)).strftime("%Y/%m/%d")
dates = datetime.today()

currentDirectory = sys.path[0]
filename = currentDirectory + r"\logFiles\auth.log"


class logger():
    #currently logger loads the list from a logfile and loops through, only keeping things after certain amount of days (daysBack)
    def recentLogs(self):
        logList = []
        trigger_phrases = ['Failure', 'Error']
        line = 1

        with open(filename) as logFile:
            logFile = logFile.readlines()

        for logLine in logFile:
            splitLine = logLine.split()
            #break the date down and remove the hours/min/seconds
            splitLine2 = splitLine[0].split('T')
            try:
                dates = splitLine2[0]
                if datetime.strptime(daysBack, "%Y/%m/%d") < datetime.strptime(dates, "%Y-%m-%d"):
                    logList.append(splitLine)
            except:
                next
            line += 1
        return logList

    #Loop through list, use RegEX to determine if an IP address. If confirmed will add it to a list to alert USER.
    def IP_login_list(logList):
        ipList = []
        for logline in logList:
            match = re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})',str(logline))
            if match:
                ipList.append(match)
        return ipList
                

if __name__ == '__main__':
    #load settings for the app
    settingsLoad = settings()
    settingsList = settingsLoad.mongoDBconnection()
    Qlogger.debug('\n                                    LOG File settings')
    Qlogger.warning(settingsLoad.logFileLocations())  
    #load the log file and display anything new
    Qlogger.debug('                LOG File Lists')
    Logger = logger()
    logList = Logger.recentLogs()
    #give you a list of Ip addresses in the log file
    Qlogger.debug('                IP addresses in log')
    print(logger.IP_login_list(logList))

