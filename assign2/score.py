# Score.py
# This program will go to any of the http://sports.yahoo.com/college-football/scoreboard/*
# It will take 3 arguments: "Team Name", "Time", "URI for sports.yahoo.com/college-football/scoreboard"
# 
# ex: python score.py "Virginia Tech" "60" http://sports.yahoo.com/college-football/scoreboard
#
# Author: Francis W. Pruter
# CS595 - Web Science -Professor Nelson
#
# Learned most of python coding from: http://www.codecademy.com/en/tracks/python
# BeautifulSoup portion was adapted from the example provided in class by Hany SalahEldeen Khalil; email:hany@cs.odu.edu
# Used http://www.crummy.com/software/BeautifulSoup/bs4/doc/ to gain an understanding of the functions avail
# Everything else used google to find the correct syntax.


from bs4 import BeautifulSoup
import time
import urllib2
import sys

#three arguements from the commandline
team = sys.argv[1]
sleep = sys.argv[2]
URI = sys.argv[3]

homeTeam = ""
homeScore = 0
awayTeam = ""
awayScore = 0

#Continue until Ctrl+C
while 1:
  try:
    #openURI using urllib2 and format with beautifulsoup
    yahooFile = urllib2.urlopen(URI)
    yahooHTML = yahooFile.read()
    soup = BeautifulSoup(yahooHTML)
    #read in each line with the tag <td class="score">
    for score in soup.find_all("td", "score"):
        temp = str(score.h4)
        #search for the team in the <h4> tag until found
        if not team.lower().replace(' ', '-') in temp:
            continue    
        else:
            #Gather names of both teams playing
            #go to the previous sibling and see if they are home or away
            #set the away/home Team
            if "away" in score.find_previous_sibling("td").get('class'):
                awayTeam = score.find_previous_sibling("td").em.get_text()
            else:
                homeTeam = score.find_previous_sibling("td").em.get_text() 

            #go to the previous sibling and see if they are home or away
            #set the away/home Team after striping all the tags       
            if "away" in score.find_next_sibling("td").get('class'):
                awayTeam = score.find_next_sibling("td").em.get_text()
            else:
                homeTeam = score.find_next_sibling("td").em.get_text()
            #Get the score
            s = score.find_all("span")
            if "away" in str(s[0]):
                awayScore = s[0].get_text()
            else:
                homeScore = s[0].get_text()
            if "home" in str(s[1]):
                homeScore = s[1].get_text()
            else:
                awayScore = s[1].get_text()

            #print output in format Away Team: Score, Home Team: Score
            print awayTeam + ": " + str(awayScore) + " " + homeTeam + ": " + str(homeScore)

    #sleep for timer
    time.sleep(float(sleep))

  except KeyboardInterrupt: # catch CTRL+C and print close
    print "Exiting"
    yahooFile.close()
    break
  except Exception, e: # catch all other errors and post them before closing
    print e
    yahooFile.close()
    break
