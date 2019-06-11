## HackHunterdon2019
Hack Hunterdon 6/8-6/9 2019\
**Voted as a Finalist by the Judges**


# The Idea
For this hackathon, the idea was to create a project that would assist the user in 
"voting with their dollar". The whole idea behind this is to support companies with favorable
business practices by spending your money at these companies. We wanted to create a way for users
to be not only mindful about any unethical practices a company may be apart of, but also suggest less
problematic companies. We decided to target the largest online retailer as our platform for our application:
Amazon. From there we figured out how to implement this idea.

# The Implementation
This project was split up into smaller to work on pieces that would eventually come together in the end to
represent the final project. The pieces that this project was broken into are listed below:
* Chrome Extension and HTML Injection
* Web Scraping
* Databasing
* Recommendation System

__Chrome Extension and HTML Injection__\
The chrome extension was the entire front end for this project. This was where the user interacted with the
application. The point of the extension was it is a place for the user to enter in companies they do not
want to support to start a recommendation system for that user, and the html injection was used to update a 
product page to remind a user that they had blocked that specific company along with recommendations for other 
products that the user could buy instead.

__Web Scraping__\
Due to not being able to easily access the Amazon product API, the team resorted to web scraping to find company 
and product information. The chrome extension would send the URL of the current page to our server where the company
and the links for other similiar products were found in the html. This information was then sent to the recommendation
system and to the database for further processing.

__Databasing__\
The databasing was used to store information on users and companies. We had to first store what users had outright blocked
certin companies so that we could get recommendations later on. We then also had to keep track of different companies with a scaled
number determining if these companies were considered problematic or not. This information all played a critical part in its 
interactions with our recommendation system.

__Recommendation System__\
The recommendation went through a few key changes as the hackathon went along. The initial conception of the recommendation system 
existed as a k-means clustering algorthim to determine what comapnies are like other companies based on the initial data given by the user.
This system was finished, but never implemented into the final build of this project in favor of a more crowd sourced approach to the problem.
We ended up with an algorithim comparing user bans with similair products on Amazon to come up with a final recommendation of a project that
was then sent back to the chrome extension to be injected into the page.

# Tools we Used
* Javascript/NodeJS
* AWS EC2/ AWS RDS
* Python/Flask/Selenium/Beautiful Soup

