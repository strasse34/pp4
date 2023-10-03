# MigMigShipment

(Developed by Reza Mirzaie)

![Mockup image]()

[Live webpage](https://migmig-bcca17837059.herokuapp.com/)

[Repository](https://github.com/strasse34/pp4-migmig)


## Introduction

Welcome to MigMigShipment, a solution for efficient parcel shipping! MigMigShipment connects individuals in need of swift parcel delivery with travelers heading in the same direction. The platform streamlines the process of sending parcels, providing a reliable and cost-effective alternative to traditional shipping services. Whether you're a traveler willing to help others while earning extra income or someone looking to ship a package swiftly and securely, MigMigShipment is here to make the process seamless. 

This project is part of the Code Institute's Full Stack Diploma Program. I used technologies of Django, Python, JavaScript, CSS, and HTML to build it. Data is stored in a PostgreSQL database.

### Project Goals

The primary goal of this project is to provide a significant solution for individuals in urgent need of parcel delivery. It aims to bridge the gap for fast and reliable delivery services, especially for long-distance shipments. With this app, a traveler and a parcel holder can seamlessly connect and negotiate the delivery cost, making it a convenient and efficient way to get parcels to their destinations quickly. This project envisions making the process of urgent parcel delivery smoother and more accessible for everyone involved.

### Data Base Design

The Entity Relationship Diagram (ERD) illustrates the structure of the database which lies at the core of the functionality of the site:

![ERD](static/docs/images/db-structure.png)


In the database design for my application, **User** is implemented using Django Allauth, simplifying user authentication and management. The **User** table contains fields for *username*, *password*, and *email*, with the *username* serving as the primary key.

The core data of the application is stored in the **FlightDetails** table. This table captures essential information about flights and travelers, such as *origin*, *destination*, *flight_date*, *weight_capacity*, *slug*, and personal traveler information. The *traveler* field establishes a relationship with the **User** table, allowing each flight to be associated with a specific user.

To manage the status of flights, the **Status** table has been introduced. It includes a *slug* field as the primary key, along with *active* and *archived* fields to track the status of each flight.

This database structure efficiently organizes and manages data for my application, ensuring seamless user authentication and comprehensive flight details management.


**Future Models**

As part of the ongoing development of my application, I envision an additional models to enhance user interaction and flexibility. One such model is the **ContactRequest** model, designed to facilitate secure communication between travelers and other users.

The **ContactRequest** model will enabling users to send and receive contact requests. When a traveler posts a flight, he/she can receive requests from other users interested in the posted flight details. The traveler will have the option to selectively reveal the contact details to specific users, fostering trust and privacy.

This addition will enhance the user experience, allowing for seamless communication and negotiation between travelers and potential partners. As my application continues to evolve, these future models will play a pivotal role in expanding its functionality and user engagement.

## User Experience - UX

The application was developed considering the four planes of User Experience:

### EPICS and User Stories

#### EPIC-1: User registration
- As a user, I can make an account, so that I can use web app services.
- As a user, I can use my username and password, so that I can log in to my account.
- As a user, after authentication, I can see my username on the website after login, so that I can be sure that I am logged in.
#### EPIC-2: Add flight details cards
- As a user, After authentication, I can add a new flight card, so that other users can see my flight card.
- As a logged in user, while filling out the form, I can select the airport from the dropdown list. so that I can find the origin and destination airports easily.
- As a logged in user, I can click on flight cards, so that I can see the complete flight details and traveler's contact details.
#### EPIC-3: Manage cards
- As a user, after authentication, I can edit my posted cards. so that I can change the card information and repost it.
- As a user, after authentication, I can archive my posted cards. so that I can move those cards from the public page to my flight page.
- As a user, after authentication, I can delete my posted cards. so that I can remove card information from the database.
- As a user, I want to see the updated date after I or other users edit a card, So that I and other users will understand that the card has been modified.
- As a user, I want flight cards to be archived when they cross the flight date. so that other users will not misunderstand outdated flight cards.
#### EPIC-4: Landing page
- As a guest visitor user, I can see all the flight cards and other information on the first page, so that I can get familiar with the app and view the basic flight information.
- As a guest visitor user, I can search among available cards, so that I can find proper flight cards quickly and easily.


#### Target Audience

The MigMigShipment application is designed to cater to a diverse audience with varying needs and preferences. Our primary target audience includes individuals and businesses seeking a reliable and efficient solution for the urgent delivery of parcels over long distances. Travelers who are frequently on the move and willing to carry parcels can also benefit from our platform by earning extra income while traveling.

### Scope
#### Core Website Functionality
- Implement a registration/login/log out features for access to core site functionality.
- Implement a form to add new flight details and traveler's contact details (flight card) to the site.
- Implement a feature to edit the filght cards.
- Implement a feature to  archive  the filght cards.
- Implement a feature to delete the filght cards.

#### Responsiveness
- Implement responsive design for smooth desktop, tablet, and mobile device access.

### Structure
The website has 10 pages for the users who get registerred.
#### Current Pages
- **Home Page** includes signup/login links in navigation bar, a banner to catch eyes, all the active flight cards which have posted with all users with ability of search, and quote sections to share user's experiences. Banner and quote space are hided after user authentication.
- **Register Page** allows the user to create an account to access the core functionality of the site.
- **Login/Logout Pages**  allow the registerred user to authenticate or log out of their account.
- **Add Flight Page**  allow the authenticated user to recorde new flight card to data base.
- **My Flight Page**  allow the authenticated user to see all the flight cards which have posted by that user.
- **Contact Traveler Page**  allow the authenticated user to see traveler's contact details.
- **Edit Flight Page**  allow the authenticated user to edit their recorded cards.
- **Archived Flight Page**  get confirmation from an authenticated user for archiving a specific cards.
- **Archived Flight Page**  get confirmation from an authenticated user for deleting a specific cards.

### Colors and Fonts used
#### Color
I've based my website's color scheme on the lively Migmig cartoon character, which serves as the app's logo. I opted for the Migmig character because of its inherent speediness, which aligns perfectly with the core emphasis on speed within my app. The character's swift nature serves as a fitting representation for the importance I place on speed in my application. By using [Coolors.co](https://coolors.co/) to extract colors from the character, I've created a cohesive and engaging design.
![Palette](static/docs/images/palette.png)
#### Font
II've used two distinct fonts in my website design:
- **Caveat:** This font is applied to the website's name to create a harmonious connection with the logo, adding a touch of personalization and uniqueness.
- **Roboto:** For the main body text, I've chosen the 'Roboto' font. It's a popular and easy-to-read typeface that ensures a comfortable reading experience for visitors.
#### Wireframes
- [Home (Not authenticated)](static/docs/images/wireframes/home-not-login.png)
- [Home (Authenticated)](static/docs/images/wireframes/home-loggedin.png)
- [Add Flight](static/docs/images/wireframes/add-flight.png)
- [My Flight](static/docs/images/wireframes/my-flight.png)
- [Contact Traveler](static/docs/images/wireframes/contact-traveler.png)

### Agile Development
Githup was used to complete this project. The project was completed in 5 iterations.
- **Iteration 1**: I started by defining the user profile.
- **Iteration 2**: In the second phase, I focused on creating the database, designing forms, and developing the relevant pages.
- **Iteration 3**: Styling and visual enhancements were completed during the third iteration.
- **Iteration 4**: The fourth phase addressed any remaining "would-have" features and resolved any lingering uncertainties or issues. 
- **Iteration 5**: In the fifth and final iteration, I conducted testing, deployed the project, and documented the entire process.

### Existing Features

#### Header and Navigation
**For authenticated users**
![Navbar and  header when user is not authenticated](static/docs/images/screenshots/navbar-not-auth.png)
**For unauthenticated users**
![Navbar and  header when user is authenticated](static/docs/images/screenshots/navbar-auth.png)
#### Alarm
**Successful Message**
![Messages for successful operation](static/docs/images/screenshots/alarm-success.png)
<br>
**dismissed Message**
![Messages for unsuccessful operation](static/docs/images/screenshots/alarm-error.png)
#### Hero Image
![Hero image](static/docs/images/screenshots/banner.png)
#### Page Title and Search bar
The search bar is available on both authenticated and unauthenticated home pages. Users can select an airport from the list to find relevant flights. 
![Page Title and Search bar](static/docs/images/screenshots/page-title-searchbar.png)
#### Upcomming Flights (Home page)
The upcoming flight list is identical for both authenticated and unauthenticated users. Each page displays six cards, and users can navigate between pages using a button at the bottom of the card space.
![Upcomming Flights page (home)](static/docs/images/screenshots/hompage.png)
#### Flight Card in home page
The flight cards on the home page feature the poster's username, the card's creation or update date, and essential flight details. Notably, traveler contact details are intentionally omitted. To access complete information, only registered users can click the 'Contact Traveler' button.<br>
![Flight Card in home page](static/docs/images/screenshots/card-home.png)
#### Quote 
![Quote section](static/docs/images/screenshots/quote.png)
#### Footer 
![Footer](static/docs/images/screenshots/footer.png)
#### My Flights page
This page showcases all the cards created by the logged-in user. It comprises both active cards (status=1, indicating flights with future dates still visible on the homepage) and archived cards (status=0, which can either be manually archived by the user or automatically when the flight date becomes outdated). Active cards offer three options for editing, archiving, and deleting, while archived cards have a single option for deletion.
![My flighs page](static/docs/images/screenshots/my-flights.png)
#### Flight Card in my flights page
Each card displays the traveler's photo, name, and contact information. Account holders can also post on behalf of travelers who are not registered on the website. When a user archives a card, effectively removing it from the homepage, the card is visually marked with the word 'Archived' at the top, and the 'edit' and 'archive' buttons are no longer displayed.
![Cards in my flights page](static/docs/images/screenshots/card-my-flights.png)
#### Edit, archive and delete pages

#### Contact Traveler page
On the Traveler's Contact Details page, you will find a single card. This card shares many similarities with the cards on the 'My Flights' page, featuring both flight details and traveler contact information. However, it is presented in a distinct style.
![Edit, archive and delete pages](static/docs/images/screenshots/edit-archive-delete.png)
#### All_Aut pages
![All-auth pages](static/docs/images/screenshots/all-auth.png)
#### Buttons


