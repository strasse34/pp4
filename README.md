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

![ERD](/static/docs/db-structure.png)

**Database Design**

In the database design for my application, **User** is implemented using Django Allauth, simplifying user authentication and management. The **User** table contains fields for *username*, *password*, and *email*, with the *username* serving as the primary key.

The core data of the application is stored in the **FlightDetails** table. This table captures essential information about flights and travelers, such as *origin*, *destination*, *flight_date*, *weight_capacity*, *slug*, and more. The *traveler* field establishes a relationship with the **User** table, allowing each flight to be associated with a specific user.

To manage the status of flights, the **Status** table has been introduced. It includes a *slug* field as the primary key, along with *active* and *archived* fields to track the status of each flight.

This database structure efficiently organizes and manages data for my application, ensuring seamless user authentication and comprehensive flight details management.


**Future Models**

As part of the ongoing development of my application, I envision an additional models to enhance user interaction and flexibility. One such model is the **ContactRequest** model, designed to facilitate secure communication between travelers and other users.

The **ContactRequest** model will enabling users to send and receive contact requests. When a traveler posts a flight, he/she can receive requests from other users interested in the posted flight details. The traveler will have the option to selectively reveal the contact details to specific users, fostering trust and privacy.

This addition will enhance the user experience, allowing for seamless communication and negotiation between travelers and potential partners. As my application continues to evolve, these future models will play a pivotal role in expanding its functionality and user engagement.
