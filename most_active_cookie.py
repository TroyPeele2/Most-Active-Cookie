#!/usr/bin/env python

import sys
import csv

cookies = sys.argv[1]
targetDate = sys.argv[3]

dictionary = {}

with open(cookies) as csvfile:
    content = csv.reader(csvfile)

    highestRepetition = 0
    answer = []

    # loop through each row in the csv file
    for row in content:
        cookie = row[0]
        cookieTimestamp = row[1][:10]

        # check if the cookie timestamp is equal to are target date
        if cookieTimestamp == targetDate:

            # if cookie isn't in dictionary set value to 1 else increase value by 1
            if cookie not in dictionary:
                dictionary[cookie] = 1
            else:
                dictionary[cookie] += 1

            # check if the dictionary key is greater to or equal to the highestRepetition
            if dictionary[cookie] > highestRepetition:
                answer = cookie
                highestRepetition = dictionary[cookie]

            elif dictionary[cookie] == highestRepetition:
                answer = answer + ',' + cookie

    # loop through dictionary and print keys that match the highest repetition
    for key in dictionary:
        if dictionary[key] == highestRepetition:
            print(key)
