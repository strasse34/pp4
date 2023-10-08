# MigMigShipment Project Testing Document

[Back to the README](README.md)

## Table of Contents

## Performance and Accessibility
### Initial Results
For testing site performance and Accessibility, I used [google lighthouse.](https://developer.chrome.com/docs/lighthouse/overview/) In my initial test, I received a lower score due to several identified issues. <br>
**Desktop: Home Page**<br>
![First lighthouse score: desktop](static/docs/images/testing/lighthouse-desktop-homepage-1.png)<br>
**Mobile: Home Page**<Br>
![First lighthouse score: mobile](static/docs/images/testing/lighthouse-mobile-homepage-1.png)
<br>
To enhance the performance and achieve a better score, I implemented the following changes:
### Optimization
**Hero Image Optimization**
- **Image Compression:** The primary issue was with the hero image, which was too large. I compressed the image multiple times to reduce its file size.
- **Image Format:** I converted the image format from JPG to WebP, which provides better compression without compromising quality.
- **Responsive Images:** To optimize mobile performance, I used a smaller image specifically for the mobile version, ensuring faster loading on smaller screens.

**Aria Labels**<br>
I added aria-label attributes to all relevant links throughout the website. This enhances accessibility and ensures that screen readers provide meaningful descriptions for links.

**Bootstrap CDN Duplication**<br>
I identified and resolved the issue of duplicating Bootstrap CDNs in the HTML head section. By removing one of them, I streamlined the page loading process.

**Image Ratio Standardization**<br>
In the quote section, I standardized the aspect ratios of images to maintain consistency. This not only improved visual appeal but also eliminated layout reflows, contributing to better performance.
### Final Score after Optimisation
Below are the final results of google lighthouse scores:<br>
**Desktop: Home Page**<br>
![Final lighthouse score: descktop, home page](static/docs/images/testing/lighthouse-desktop-homepage-2.png)<br>
**Mobile: Home Page**<br>
![Final lighthouse score: mobile, home page](static/docs/images/testing/lighthouse-mobile-homepage-2.png)<br>
**Desktop: My Flight Page**<br>
![Final lighthouse score: descktop, my flight page](static/docs/images/testing/lighthouse-desktop-myflightpage.png)<br>
**Mobile: My Flight Page**<br>
![Final lighthouse score: mobile, my flight page](static/docs/images/testing/lighthouse-mobile-myflightpage.png)<br>

## Code Validation
### HTML Valication
To validate my HTML code, I utilized the [W3C HTML Validator](https://validator.w3.org/). I encountered a few errors initially, but I was able to address and resolve each of them. <br>
**Initial Validation:**<br>
![HTML Initial validation](static/docs/images/testing/w3c-homepage-not-auth-1.png)
**Final Validation:**<br>
![HTML Final validation](static/docs/images/testing/w3c-homepage-not-auth-2.png)
I got no error for all of other pages. 

### CSS Validation
I also ran my CSS file through the [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) and found that it had no issues or errors.
![CSS file validation](static/docs/images/testing/w3c-css.png)

### JS Validation
I used [JSHint](https://jshint.com/) to test the only function in my base template and below is the result:<br>

![JS test](static/docs/images/testing/js.png)

### Python Validation
I used [CI Python Linter](https://pep8ci.herokuapp.com/) to validate my Python code and resolved all minor issues. Here are the final test results.
**Admin**<br>
![Python test: admin.py](static/docs/images/testing/admin.png)
**Forms**<br>
![Python test: forms.py](static/docs/images/testing/forms.png)
**Models**<br>
![Python test: models.py](static/docs/images/testing/model.png)
**App Urls**<br>
![Python test: app urls.py](static/docs/images/testing/app-url.png)
**Views**<br>
![Python test: views.py](static/docs/images/testing/views.png)
**Project Urls**<br>
![Python test: project url.py](static/docs/images/testing/project-url.png)

## Manual Testing
I conducted manual testing based on user stories, defining and testing multiple scenarios for each story.<br>

**User Story: As a user, I can make an account, so that I can use web app services.**
| Test Case | Steps | Expected Result | Pass/Fail |
| --- | ---- | --- | --- |
| Test Case 1:<br> Verify Successful Register | 1- Navigate to the Registration page.<br> 2- Fill in valid registration details.<br> 3- Click the "Register" button. | User should be redirected to the Home page with a success message. | Pass |
| Test Case 2:<br> Verify Invalid Register Attempt | 1- Navigate to the Registration page.<br> 2- Fill in incomplete or invalid registration details.<br> 3- Click the "Register" button. | User should see an error message indicating invalid registration data (e.g., incomplete form or existing username/email). | Pass |
| Test Case 3:<br> Verify "Cancel" Button navigation| 1- Navigate to the Registration page.<br> 2- Heat the "Cancel" button. | User should be directed to the Home page. | Pass |
<br>

**User Story: As a user, I can use my username and password, so that I can log in to my account.**
| **Test Case** | **Steps** | **Expected Result** | **Pass/Fail** |
| --- | --- | --- | --- |
| Test Case 1:<br> Verify Successful Login | 1- Navigate to the Login page.<br> 2- Enter valid username and password.<br> 3- Click the "Login" button. | User should be redirected to the Home page with a successful message. | Pass |
| Test Case 2:<br> Verify Invalid Login Attempt | 1- Navigate to the Login page.<br> 2- Enter incorrect username or password.<br> 3- Click the "Login" button. | User should see an error message indicating invalid login credentials. | Pass |
| Test Case 3:<br> Verify "Cancel" Button navigation| 1- Navigate to the "Login" page.<br> 2- Heat the "Cancel" button. | User should be directed to the Home page. | Pass |
<br>
<br>

**User Story: As a guest visitor user, I can see all the flight cards and other information on the first page, so that I can get familiar with the app and view the basic flight information.**
| **Test Case** | **Steps** | **Expected Result** | **Pass/Fail** |
| --- | --- | --- | --- |
| Test Case 1:<br> Verify Viewing first page of the website as a Guest | 1- Open the web app as a guest visitor (not logged in).<br> 2- Observe the hero image, flight cards including flight information, quotes and footer displayed on the first page. | All flight cards and relevant information are visible and accessible to the guest visitor on the first page. | Pass |
| Test Case 2:<br> Verify Not navigation to Traveler's Contact Detial page| 1- Open the web app as a guest visitor (not logged in).<br> 2- Click on button "Contact Traveler" on each card. | The guest visitor can click on the button but he/she is redirected to the sign-up page instead of viewing the contact details. | Pass |
| Test Case 3:<br> Verify navigation to Registration page | 1- Open the web app as a guest visitor (not logged in).2- Click on the "Join Us!" on hero image or "Register" in navbar. | The guest visitor should be directed to the Registration page where he/she can register for an account if they choose to do so. | Pass |
<br>

**User Story: As a logged-in user, I can click on flight cards, so that I can see the complete flight details and traveler's contact details.**
| **Test Case** | **Steps** | **Expected Result** | **Pass/Fail** |
| --- | --- | --- | --- |
| Test Case 1:<br> Verify viewing Home page | 1- Log in to the web app as a registered user. | After log in the user can access the homepage containing all flight cards without encountering any errors or redirection issues. | Pass |
| Test Case 2:<br> Verify viewing Traveler's Contact Info page | 1- Log in to the web app as a registered user.2- Click on the "Contact Traveler" button associated with a flight card. | The user should be able to click on the "Contact Traveler" button and redirected to Traveler Contact Details page where there are the contact information of the traveler associated with the selected flight card, including name, email, or other contact details provided by the traveler. | Pass |
| Test Case 3:<br> Verify navigation back to Upcoming Flights page from "Traveler's Contact" page | 1- Log in to the web app as a registered user.<br> 2- Click on the "Contact Traveler" button on one of the flight card to be directed to Traveler's Contact Details page.<br> 3- After viewing traveler's contact info, click on a "Home" navigation in navbar. | The user should be able to easily navigate back to the list of flight cards on the "Home" page after viewing traveler's contact info. | Pass |
<br>

**User Story: As a user, after authentication, I can add a new flight card, so that other users can see my flight card.**

| **Test Case** | **Steps** | **Expected Result** | **Pass/Fail** |
| --- | --- | --- | --- |
| Test Case 1:<br> Verify viewing Add Flight page by clicking on "Add Flight" navigation on navbar | 1- Log in to the web app as a registered user.<br> 2- Navigate to the 'Add Flight' page by clicking on the 'Add Flight' navigation link in the navbar. | The user should be directed to the 'Add Flight' page without encountering any errors. | Pass |
| Test Case 2:<br> Verify adding flight using form when all fields are filled out correctly | 1- Log in to the web app as a registered user.<br> 2- Navigate to the Add Flight page.<br> 3- Fill out all the required fields on the Add Flight form with valid information.<br> 4- Click the "Add Flight" button. | The flight card should be successfully added, and the user should receive a success message. The user directed to home page and his/her new flight card should be visible to other users in Home page and Contact Traveler page. The user also see his/her new card in My Flights page. | Pass |
| Test Case 3:<br> Verify getting an error when origin and destination are the same | 1- Log in to the web app as a registered user.<br> 2- Navigate to the Add Flight page.<br> 3- Fill out the Origin and Destination fields with the same location.<br> 4- Click the "Add Flight" button. | The user should receive an error message indicating that the origin and destination cannot be the same. | Pass |
| Test Case 4:<br> Verify getting an error when origin, destination, name, and date of flight match an existing flight | 1- Log in to the web app as a registered user.<br> 2- Navigate to the Add Flight page.<br> 3- Fill out the Origin, Destination, Name, and Flight Date fields with information that matches an existing flight card.<br> 4- Click the "Add Flight" button. | The user should receive an error message indicating that a flight with the same origin, destination, name, and date already exists. | Pass |
| Test Case 5:<br> Verify getting an error when flight date ss already passed | 1- Log in to the web app as a registered user.<br> 2- Navigate to the Add Flight page.<br> 3- Fill out the Flight Date field with a date that has already passed.<br> 4- Click the "Add Flight" button. | The user should receive an error message indicating that the flight date cannot be in the past. | Pass |
| Test Case 6:<br> Verify getting an error when a field is left empty | 1- Log in to the web app as a registered user.<br> 2- Navigate to the Add Flight page.<br> 3- Leave one or more required fields empty on the Add Flight form.<br> 4- Click the "Add Flight" button. | The user should receive an error message indicating that the empty field(s) need to be filled out. | Pass |
| Test Case 7:<br> Verify "Cancel" Button navigation| 1- Navigate to the Add Flight page.<br> 2- Heat the "Cancel" button. | User should be directed to the Home page. | Pass |
<br>




