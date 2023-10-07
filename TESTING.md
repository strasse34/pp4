# MigMigShipment Project Testing Document

[Back to the README](README.md)

## Table of Contents

## Performance and Accessibility

For testing site performance and Accessibility, I used [google lighthouse.](https://developer.chrome.com/docs/lighthouse/overview/) In my initial test, I received a lower score due to several identified issues. <br>

**Desktop: Home Page**
![First lighthouse score: desktop](static/docs/images/testing/lighthouse-desktop-homepage-1.png) <br>


**Mobile: Home Page**
![First lighthouse score: mobile](static/docs/images/testing/lighthouse-mobile-homepage-1.png) <br>

To enhance the performance and achieve a better score, I implemented the following changes:

### Hero Image Optimization:

Image Compression: The primary issue was with the hero image, which was too large. I compressed the image multiple times to reduce its file size.
Image Format: I converted the image format from JPG to WebP, which provides better compression without compromising quality.
Responsive Images: To optimize mobile performance, I used a smaller image specifically for the mobile version, ensuring faster loading on smaller screens.
### Aria Labels:

I added aria-label attributes to all relevant links throughout the website. This enhances accessibility and ensures that screen readers provide meaningful descriptions for links.
Bootstrap CDN Duplication:

I identified and resolved the issue of duplicating Bootstrap CDNs in the HTML head section. By removing one of them, I streamlined the page loading process.
### Image Ratio Standardization:

In the quote section, I standardized the aspect ratios of images to maintain consistency. This not only improved visual appeal but also eliminated layout reflows, contributing to better performance. <Br>
Below are the final results of google lighthouse score:<br>

**Desktop: Home Page**
![Final lighthouse score: descktop, home page](static/docs/images/testing/lighthouse-desktop-homepage-2.png)
**Mobile: Home Page**
![Final lighthouse score: mobile, home page](static/docs/images/testing/lighthouse-mobile-homepage-2.png)
**Desktop: My Flight Page**
![Final lighthouse score: descktop, my flight page](static/docs/images/testing/lighthouse-desktop-myflightpage.png)
**Mobile: My Flight Page**
![Final lighthouse score: mobile, my flight page](static/docs/images/testing/lighthouse-mobile-myflightpage.png)













