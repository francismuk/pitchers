# One Minute Pitch
## An application that allows users to make one minute pitches and get feedback and votes on them.


## By Francis Mukuha

## Description
This application is  a web application that allows users to submit a pitch. Also, other users are allowed to vote on submitted pitches and leave comments to give their feedback on the pitches. For a user to submit a pitch, vote on a pitch or give feedback on a pitch they need to have an account. <br>

The pitches are organized by categories. Examples of categories: <br> 
- pickup lines
- interview pitches
- product pitches
- promotion pitches

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
| Register to be a user | Your email : jane@doe.com <br> Username : jane101 <br> Password : doe1 | New user is registered |
| Log in | Your email : jane@doe.com <br> Password : doe1 | Logged in |
| Display pitch categories | N/A | List of various pitch categories |
| See pitches from selected category | **Click** a category | Directed to a page with a list of pitches from the selected category |
| Create a pitch | **Click Create A Pitch** | An authenticated user is directed to a page with a form where the user can create and submit a pitch |
| See a pitch | **Click** on a pitch | A user is directed to a page containing the pitch, its comments and its votes |
| Comment on a pitch | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a pitch |
| Upvote on a pitch | **Click** on upvote glyphicon | The votes on the pitch increases by one |
| Downvote on a pitch | **Click** on downvote glyphicon | The votes on the pitch decreases by one |

## Prerequsites
    - Python 3.6 required

## Set-up and Installation
    - Clone the Repo
    - Edit the start.sh file with your api key from the news.org website
    - Install python 3.6
    - Run chmod a+x start.py
    - Run ./start.py
    

## Technologies used
    - Python 3.6
    - News API 
    - HTML
    - Bootstrap
    - CSS

### [License](LICENSE)
MIT LIcense
Copyright (c) Francis Mukuha W
