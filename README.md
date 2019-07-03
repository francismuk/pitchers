# One Minute Pitch
## An application that allows users to make one minute pitches and get feedback and votes on them. 3-7-2019


## By Francis Mukuha

## Description
This application is  a web application that allows users to submit a pitch. Also, other users are allowed to vote on submitted pitches and leave comments to give their feedback on the pitches. For a user to submit a pitch, vote on a pitch or give feedback on a pitch they need to have an account. <br>

The pitches are organized by categories. Examples of categories: <br> 
- pickup lines
- creative pitches
- jokes

## User Stories
As a user I would like:
* to view the different categories
* to see the pitches other people have posted
* to submit a pitch in any category
* to comment on the different pitches and leave feedback
* to vote on the pitch and give it a downvote or upvote

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email <br> Username <br> Password  | New user is registered and welcome email sent to the user |
| Log in | Your email <br> Password  | Logged in |
| Display pitch categories | N/A | List of various pitch categories |
| See pitches from selected category | **Click** add category | Directed to a page with a list of pitches from the selected category |
| Create a pitch | **Click Create A Pitch** | An authenticated user is directed to a page with a form where the user can create and submit a pitch |
| See a pitch | **Click** on a pitch | A user is directed to a page containing the pitch, its comments and its votes |
| Comment on a pitch | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a pitch |


## Prerequsites
    - Python 3.6 required

## Set-up and Installation
    - Clone the Repo
      (git clone https://github.com/francismuk/pitchers)
    - Edit the start.sh file with your api key from the news.org website
    - Install python 3.6
       (sudo apt-get install python3.6)
    - Run chmod a+x start.py
    - Run ./start.py
    

## Technologies used
    - Python 3.6
    - News API 
    - HTML
    - Bootstrap
    - CSS

### [License](https://opensource.org/licenses/MIT)
MIT LIcense
Copyright (c) Francis Mukuha W
