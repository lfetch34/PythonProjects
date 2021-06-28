# Luke Fetchko
# Dr. Wooster
# CSCI U236
# This is a program that combines the features of a sports API named sportsipy to retrieve information such as team names,
# win and loss records, and roster information for any team in the NHL, NFL, or MLB.
# The user will be asked which league they would like to retrieve information from and will be presented with the team names
# and the win and loss records of all teams from the corresponding league chosen.
# It will then ask if the user would like to see the roster of a specific team and display all of the team names with their abbreviations.
# Then the user will be prompted to enter the abbreviation of the desired team they want to see the roster of.
# If they chose to view the roster, then they will be asked if they would like to download a few images of the team's logo.
# To download images, this program makes use of Selenium to automate web browsing and clicking like a normal user would.
# It also uses the os, time, requests, pandas, io, PIL, and hashlib modules to accomplish the downloading of images.
# Image scraping technique and implementation come from the Scraping Images article provided by Dr. Wooster

# Needed import statements from sportsipy module
from sportsipy.mlb.teams import Teams as MLB
from sportsipy.nfl.teams import Teams as NFL
from sportsipy.nhl.teams import Teams as NHL
from sportsipy.mlb.roster import Roster as MLBR
from sportsipy.nfl.roster import Roster as NFLR
from sportsipy.nhl.roster import Roster as NHLR

# Needed import statements and modules to make downloading images possible
from selenium import webdriver
import os
import time
import requests
import pandas as pd
import io
from PIL import Image
import hashlib
# Driver path of the chrome browser executable on my computer, to use this program on another machine, Selenium must be installed,
# and a chrome driver for the user's chrome version.
# The driver path is the file path of where the executable is located on the user's specific machine
DRIVER_PATH=''
# Function definition of fetch_image_urls, takes a query string, a max links to fetch integer, a webdriver from Selenium, and a sleep between interactions integer as parameters
# Returns a set of image urls found
# Code contributed from Fabian Bolser at https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d
def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)    
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls
# Function definition of persist_image
# Takes a folder path string and url string as parameters
# Does not return a value but uses an image url to open an image and download the image and displays success or error and the file path of the image
# Code contributed from Fabian Bolser at https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d
def persist_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")
# Function definiton of search_and_download which combines the fetch_image_urls and persist_image functions to accomplish searching and downloading images
# Takes a search term string, a driver path string, a target path string, and a number of images integer as parameters
# No return value but accomplishes the searching and downloading of a specified number of images of a specific search term to a target folder
# Code contributed from Fabian Bolser at https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d
def search_and_download(search_term:str,driver_path:str,target_path='./images',number_images=2):
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)
        
    for elem in res:
        persist_image(target_folder,elem)
# Begin program execution with infinite loop
while True:
    # Ask user which league they would like information from
    league = input('Which sports league would you like team names and records from? (Enter NHL or NFL or MLB)')
    print()
    # If the league wanted is MLB
    if league.upper() == 'MLB':
        # Create Teams object for MLB teams
        mlbteams = MLB()
        # Iterate through MLB teams object and print the team name, number of wins, and number of losses
        for team in mlbteams:
            
            print(team.name,'\nWins: ' + str(team.wins), 'Losses: ' + str(team.losses))
            print()
        # Ask user if they would like to see the 2020 roster of a team
        mlbros = input('Would you like to see the 2020 roster of a specific team? (Enter Y or N)')
        print()
        # If the user does want to see a roster
        if mlbros.upper() == 'Y':
            # Print out the team names along with their abbreviations
            for team in mlbteams:
                print(team.name,'\nAbbreviation: ' + str(team.abbreviation))
                print()
            # Prompt user to enter the abbreviation of the team they want the roster for
            abb = input('Enter the three letter abbreviation for the team you want the roster of: ')
            print()
            print('Loading roster.. this may take a few minutes')
            print()
            # Create MLB Roster object for the specified team
            wanted = MLBR(abb.upper(),2020)
            # Iterate through players of wanted roster and print player names
            for player in wanted.players:
                print(player.name)
            print()
            # Ask user if they would like to download images of the team's logo
            mlb_imgs = input("Would you like to download a few images of this team's logo? (Enter Y or N)")
            print()
            # If so, then iterate through teams and find the name of the team with the matching abbreviation
            if mlb_imgs.upper() == 'Y':
                team_name = ''
                for team in mlbteams:
                    if abb.upper() == team.abbreviation:
                        team_name = team.name
                # Search term string which is the desired team name concatenated with logo
                search_term = team_name + ' logo'
                # Call search_and_download function to search and download desired images
                search_and_download(search_term=search_term,driver_path=DRIVER_PATH)
                print()
            
            
            
    # If the league wanted is NFL        
    elif league.upper() == 'NFL':
        # Create Teams object for NFL teams
        nflteams = NFL()
        # Iterate through NFL teams object and print the team name, number of wins, and number of losses
        for team in nflteams:
            
            print(team.name,'\nWins: ' + str(team.wins), 'Losses: ' + str(team.losses))
            print()
        # Ask user if they would like to see the 2020 roster of a team
        nflros = input('Would you like to see the 2020 roster of a specific team? (Enter Y or N)')
        print()
        # If the user does want to see a roster
        if nflros.upper() == 'Y':
            # Print out the team names along with their abbreviations
            for team in nflteams:
                print(team.name,'\nAbbreviation: ' + str(team.abbreviation))
                print()
            # Prompt user to enter the abbreviation of the team they want the roster for
            nflabb = input('Enter the three letter abbreviation for the team you want the roster of: ')
            print()
            print('Loading roster.. this may take a few minutes')
            print()
            # Create NFL Roster object for the specified team
            nflwanted = NFLR(nflabb.upper(),2020)
            # Iterate through players of wanted roster and print player names
            for player in nflwanted.players:
                print(player.name)
            print()
            # Ask user if they would like to download images of the team's logo
            nfl_imgs = input("Would you like to download a few images of this team's logo? (Enter Y or N)")
            print()
            # If so, then iterate through teams and find the name of the team with the matching abbreviation
            if nfl_imgs.upper() == 'Y':
                nfl_team_name = ''
                for team in nflteams:
                    if nflabb.upper() == team.abbreviation:
                        nfl_team_name = team.name
                # Search term string which is the desired team name concatenated with logo
                nfl_search_term = nfl_team_name + ' logo'
                # Call search_and_download function to search and download desired images
                search_and_download(search_term=nfl_search_term,driver_path=DRIVER_PATH)
                print()

    # If the league wanted is NHL
    elif league.upper() == 'NHL':
        # Create Teams object for NHL teams
        nhlteams = NHL()
        # Iterate through NHL teams object and print the team name, number of wins, and number of losses
        for team in nhlteams:
            
            print(team.name,'\nWins: ' + str(team.wins), 'Losses: ' + str(team.losses), 'OT Losses: ' + str(team.overtime_losses))
            print()
        # Ask user if they would like to see the 2020 roster of a team
        nhlros = input('Would you like to see the 2020 roster of a specific team? (Enter Y or N)')
        print()
        # If the user does want to see a roster
        if nhlros.upper() == 'Y':
            # Print out the team names along with their abbreviations
            for team in nhlteams:
                print(team.name,'\nAbbreviation: ' + str(team.abbreviation))
                print()
            # Prompt user to enter the abbreviation of the team they want the roster for
            nhlabb = input('Enter the three letter abbreviation for the team you want the roster of: ')
            print()
            print('Loading roster.. this may take a few minutes')
            print()
            # Create NHL Roster object for the specified team
            nhlwanted = NHLR(nhlabb.upper(),2020)
            # Iterate through players of wanted roster and print player names
            for player in nhlwanted.players:
                print(player.name)
            print()
            # Ask user if they would like to download images of the team's logo
            nhl_imgs = input("Would you like to download a few images of this team's logo? (Enter Y or N)")
            print()
            # If so, then iterate through teams and find the name of the team with the matching abbreviation
            if nhl_imgs.upper() == 'Y':
                nhl_team_name = ''
                for team in nhlteams:
                    if nhlabb.upper() == team.abbreviation:
                        nhl_team_name = team.name
                # Search term string which is the desired team name concatenated with logo
                nhl_search_term = nhl_team_name + ' logo'
                # Call search_and_download function to search and download desired images
                search_and_download(search_term=nhl_search_term,driver_path=DRIVER_PATH)
                print()
    # If league input is invalid, tell user
    else:
        print('Invalid input')
        print()
    # Ask user if they would like to run the program again   
    cnt= input('Would you like to run the program again? (Y or N)')
    print()
    # If not, break out of infinite loop, and terminate program
    if cnt.upper() == 'N':
        break
