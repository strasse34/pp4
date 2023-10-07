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





