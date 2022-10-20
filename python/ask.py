#!/usr/bin/env python3

import requests


class main():
    request=requests.get('http://api.open-notify.org')
    people=requests.get('http://api.open-notify.org/astros.json')
    people_json = people.json()
    answer = "z"

    while answer != "q" or answer != "Q":
        print("\n\n A: Number of people in space \n B: Names of the Astronauts\n Q: Quit \n")
        answer = input("Select an option: ")
        if answer == "a" or answer == "A":
            print("\nThe Number of people in space:",people_json['number'])
            print("---------------------")
        elif answer == "b" or answer == "B":
            for p in people_json['people']:
                print(p['name'])
            print("---------------------")
        elif answer == "q" or answer == "Q":
            exit()
        else:
            print("Invalid argument. Exiting.")
            exit()
