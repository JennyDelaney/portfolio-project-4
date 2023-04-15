# Manual Testing

[View the live project here.](https://pp4-fix-it-physio.herokuapp.com/)

### Responsiveness:

![Responsiveness](/static/readme_images/responsiveness.jpg)

### Browser Compatibility:

![browser compatibility](/static/readme_images/browser_compatibility.jpg)

### Bugs:

During development two issues were experienced -

**1.** user_id error:
When I tried to put through an appointment it failed due to a user_id error.
**Resolution:-** I added to the view.py file - booking.user=request.user under the AddAppt view.

**2.** no reverse match when appointment was submitted.
**Resolution:-** I corrected the href on line 10 in 'thank_you.html' to {% url'appt_list' %} from {% url 'booking_app/appt_list' %}.

After Deployment the following error was experienced:-
Error 500 error when changing status of the booking in the back-end.
**Resolution:-** A migration was completed and it was resolved.  Changes had been made to the models.py file without a migration being done.

### Lighthouse:

#### Desktop Device:

![Desktop Device](/static/readme_images/lighthouse_desktop.PNG)

#### Mobile Device:

![Mobile Device](/static/readme_images/lighthouse_mobile.PNG)

### Code Validation:

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [View Results](/static/readme_images/html_validator.png)
		**Resolution:-**
		Error 1 –
		Added a lang=”en” to the html to indicate that the language 		is English.
		Error 2 –
		Removed / after the meta name
		Error 3 –
		Removed stray end tag </span>

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [View Results](/static/readme_images/css_validator.png)

-   Python Validation - [View Results](/static/readme_images/python_validation.jpg)
		**Resolution:-**
		All lines of code showing as being too long was amended

### Testing User Stories from User Experience (UX) Section:

## User Stories Met:
This section is to look back at the User stories we established during the strategy phase of the project. 
We are looking to see if we have met all the goals we set out. 

#### New User: 
* As a new user, I want to register so I can make an appointment.
 **Met on the Sign up/Register page**
* As a new user, I want to make an appointment.
 **Met on the Make an appointment Page**
* As a new user, I want to pick the date and time of my appointment.
 **Met on the Make an appointment Page**
* As a new user, I want to be able to view my appointment.
 **Met on the View my appointment Page**
* As a new user, I want to be able to log in to edit or cancel my appointment.
 **Met on the View my appointment Page**

#### Returning User:
* As a returning user, I want to log in to my account
 **Met on the Log in page**
* As a returning user, I want to make an appointment.
 **Met on the make an Appointment Page**
* As a returning user, I want to view my appointment(s)
 **Met on the View my appointment(s) page**
* As a returning user, I want to be able to edit or cancel my appointment.
 **Met on the View my appointment page**

### Further Testing:

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.