# **Cinerama Cinema**

Cinerama Cinema is a cinema for all film lovers. It offers all kinds of films - blockbusters, sing-alongs, concerts, old classics, documentaries - lets you pre-book snacks and has the cosiest salons that gives the visitors a 1950s Paris feeling. All to give the cinema goers the best experiance! The app is targeted at all adults that enjoy to watch not only blockbusters that are popular right now, but also films that are not commonly shown at cinemas because they are old or perhaps seen as being targeted at a small crowd. 

The app is a booking system for tickets and snacks so that almost everything is done when the user comes to the cinema. All the users have to do at the cinema is to pick up the snacks and pay, then they´re ready to go! The site acts as a repository for bookings as the users can store, update and cancel all their bookings through the app. They can also read about films that they might be interested in watching in the future. 

![AN image of the deployed app on different screen sizes](documentation/LÄÄÄÄÄÄÄÄÄÄÄÄÄNK)

You can find the site [here](LÄÄÄÄÄÄÄÄÄÄÄNK).

## **UX**

### **User Stories**

The user of Cinerama Cinema would be any adult that enjoys watching films, that go to the cinema a lot and therefore needs the ticket and snack booking to be fast and easy. 

#### **EPIC - View Films**
Handles creation of the list of films available to watch at the cinema and the functionality to reveal a text description about each list item.
- As a Site User I can view a list of films so that I can read about them and figure out which one I want to watch.

#### **EPIC - Film Management**
Handles creation of a admin page to allow the admin to manage films shown at the site.
- As a Site Admin I can create, read, update and delete films so that I can manage my film program content.

#### **EPIC - User registration and Login**
Handles the creation of customer registration and login/logout functionality.
- As a Site User I can register an account so that I can book tickets to see a film and eat.
- As a registered Site User I can log in with my username and password so that the system can authenticate me.

#### **EPIC - Booking**
Handles creation of the booking page at the site, containing form that needs to be filled in to book tickets. It also handles creation of user profile page where the user can see it´s bookings.
- As a Site User I can can choose a film to watch, depending on date, by adding a number of tickets so that I can watch a film when I´m free according to my calendar.
- As a Site User I can view the snacks meny and choose snacks so that I can eat and drink during a film.
- As a Site User I can book tickets so that I can watch the film.
- As a Site User I can view all my bookings so that I can keep track of them.
- As a Site User I can edit or cancel a tickets and snacks booking on my profile page so that I can manage my bookings.

### **Design**

The site was built with the goal to give it a feeling of a cinema in Paris in the 1940-1950s, giving the visitors of the site a little hint that this cinema not only offers new blockbuster films. Colors were chosen to make it feel like going into an old salon with dim lighting, large red drapes and golden details. The colors were also chosen with contrast ratio in mind, to make the site as accessible as possible.

The main fonts used are Limelight and Poiret-One. They are imported with [Google Fonts](https://fonts.google.com/). They were chosen because they look like fonts used by cinemas in Paris in the 1940-1950s.


#### **Wireframes**

<details>

<summary>Home page</summary>

![Home Page](documentation/wireframes/home-page1.png)
![Home Page mobile](documentation/wireframes/home-page2.png)
</details>

<details>

<summary>Sign Up</summary>

![Sign Up](documentation/wireframes/sign-up1.png)
![Sign Up mobile](documentation/wireframes/sign-up2.png)
</details>

<details>

<summary>Log In</summary>

![Log In](documentation/wireframes/login1.png)
![Log In mobile](documentation/wireframes/login2.png)
</details>

<details>

<summary>Log Out</summary>

![Log Out](documentation/wireframes/logout1.png)
![Log Out mobile](documentation/wireframes/logout2.png)
</details>

<details>

<summary>Book Tickets</summary>

![Book Tickets](documentation/wireframes/book-tickets1.png)
![Book Tickets mobile](documentation/wireframes/book-tickets2.png)
![Book Tickets](documentation/wireframes/book-tickets3.png)
![Book Tickets mobile](documentation/wireframes/book-tickets4.png)
</details>

<details>

<summary>My Bookings</summary>

![My Bookings](documentation/wireframes/my-bookings1.png)
![My Bookings mobile](documentation/wireframes/my-bookings2.png)
</details>

<details>

<summary>Edit</summary>

![Edit](documentation/wireframes/edit1.png)
![Edit mobile](documentation/wireframes/edit2.png)
</details>

<details>

<summary>Cancel</summary>

![Cancel](documentation/wireframes/cancel1.png)
![Cancel mobile](documentation/wireframes/cancel2.png)
</details>

## **Agile Development**

The app was built using an agile approach, with a GitHub project board, milestones, labels and issues. The GitHub project board can be found [here](https://github.com/users/sarasm93/projects/4). All epics and user stories mentioned above were created with GitHub issues. The agile development iterations are created with milestones. All issues are linked to a milstone. They are also linked to an epic using labels. Labels have also been used to priorities which issues are most important by create labels namned "must have", "should have", "could have" and "wont´t have". 

## **Data models and database**

The below ERD diagram was made using [Lucid Charts](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucid%20charts&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433237648&km_CPC_TargetID=kwd-64262996435&km_CPC_Country=9062397&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=CjwKCAjwwb6lBhBJEiwAbuVUSp5GJupY-n0T0KIxQyga5tojqyWYZIbI3dXIpvdCgxbxCcPYgxb-_RoCMJAQAvD_BwE) and shows the structure of the PostgreSQL database used in this project. The diagram visualises the types of data models required for the project and the relationships between them. 

Django AllAuth was used for the user model and user authentication system.

The booking model was created so the user can create bookings that can be edited and cancelled. 

The film showtime model holds the film program with information about when each film is shown and the price for it. 

The snack model contains the different snacks that can be booked and what they cost.

The Film model holds all information about a film, such as title, description/plot, director, runtime and so on, so that the user can read about a film. 

The genre model was created so that each film can have a genre added to it. This gives the users a quick perception of which films might be interesting to them.

![ERD diagram showing the project data models and the relationships between them - image 1](documentation/models1.png)
![ERD diagram showing the project data models and the relationships between them - image 2](documentation/models2.png)

## **Features**

### **Existing features**

### **Future features**

- User cannot change or cancel booking within 2 days of the film. 
- Users can order several popcorn buckets/sodas of one sizes (rather than only one) per booking. 

The above features are listed in a GitHub Project used as backlog for the app. The backlog is found [here](https://github.com/users/sarasm93/projects/6).

## **Testing**

### **Validator testing**

### **Resolved problems**

### **Bugs**

## **Deployment**

## **Technologies, Languages, Frameworks, Libraries, Servers, Programs and Sites used**

### **Languages**
- HTML
- CSS
- Javascript
- Python

### **Frameworks**
- [Django](https://www.djangoproject.com/) - main Python web framework used to develop this project
- [Materialize](https://materializecss.com) - to make the site responsive and to style user interface templates with the card reveal component, navbar (and sidnavbar for mobile devices), footer, toast messages, dropdown lists in forms, table for user bookings and collapsible view of the booking form for tickets. 

### **Libraries**
- [Psycopg2](https://pypi.org/project/psycopg2/) - Python-PostgreSQL database adapter, in order to use Python code (instead of SQL) to do Postgres commands 
- [urllib3](https://pypi.org/project/urllib3/1.26.15/) - user-friendly HTTP client for Python used by many components in Python, such as requests and pip

### **Servers**
- [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server acting as the web server for the project
- [PostgreSQL]()

### **Programs and Sites**
- [GitHub](https://github.com/)- version control and as agile tool
- [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433237648&km_CPC_TargetID=kwd-33511936169&km_CPC_Country=9062397&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjwnMWkBhDLARIsAHBOftrLqk9mpk7BpbSpfCB82TCw4CoQ4k4-1IqLKE5G5i3Cs5Q-3_ysvx4aAtpTEALw_wcB) - create database model schema
- [Balsamiq](https://balsamiq.com/) - create wireframes 
- [Cloudinary](https://cloudinary.com/) - image hosting and management 
- [ElephantSQL](https://www.elephantsql.com/) - free database service that hosts the PostgreSQL database for this project

## **Credits**

Materialize was used to make the site responsive and to style user interface templates:
- [card reveal component](https://materializecss.com/cards.html) on the films available at the cinema to reveal text about them.
- [navbar](https://materializecss.com/navbar.html) and [sidnavbar for mobile devices](https://materializecss.com/sidenav.html) to make it responsive and look good on all devices
- [footer](https://materializecss.com/footer.html) to make it responsive and look good on all devices 
- [toast messages](https://materializecss.com/toasts.html) to display alert messages when the user interacts with the site
- [dropdown lists in forms](https://materializecss.com/select.html) to make the forms easy to use and nice to look at
- [responsive table](https://materializecss.com/table.html) for user bookings to be displayed in a structured, and responsive, way
- [collapsible view](https://materializecss.com/collapsible.html) to display the film showtimes and booking form for tickets in a strucutred way giving the user a clear overview. 

To filter films on the "Book tickets" page based on their showtime date, code from [Codechit.com](https://www.codechit.com/django-filter-search-form-guide/), [Letscodemore.com](https://www.letscodemore.com/blog/customizing-django-filters-with-css-classes/), [this forum-djangoproject-com page](https://forum.djangoproject.com/t/initialize-a-django-filter-with-date/11565) and [this forum-djangoproject-com page](https://forum-djangoproject-com.translate.goog/t/initialize-a-django-filter-with-date/11565?_x_tr_sl=en&_x_tr_tl=sv&_x_tr_hl=sv&_x_tr_pto=sc&_x_tr_hist=true) was used to create the working code in the project.

Code on lines 309-321 in style.css was taken from [this Stackoverflow site](https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown). It helps to show the error message for invalid input for "Choose number of tickets" field in booking form.

All Javascript code in the script.js file is taken from [Materializecss.com](materializecss.com) and used for initialization of functionality provided by Materialize components used in the project.

Code for alert messages was first taken from the [Django project documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/#displaying-messages). But as I discovered that Materialize toasts could be used instead, the code from the Django project was altered to make the toasters work. I also used this [Pythontutorial.net page](https://www.pythontutorial.net/django-tutorial/django-edit-form/) and this [Stackoverflow page](https://stackoverflow.com/questions/39770562/making-djangos-messages-appear-in-javascript-alert-rather-than-html) to better understand how to use messages.

The Code Institute [Hello Django project](https://github.com/ckz8780/ci-fsf-hello-django/tree/fc660412398ec2f12655110866e92ce41b983913) and [Django Blog project](https://github.com/Code-Institute-Solutions/Django3blog/tree/master) were used to start up this project. They were used to help understand how to build up the app - the build-up of the settings.py file, how to get template inheritance to work, how to connect the style.css file to the base.html, how to create models, how to create functions in views.py, how models are added to/shown in the admin page and so on.

[This Stackoverflow page](https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model) was used to understand how to put validation minimum and maximum values on model fields.

I used [ngangasn.com](https://ngangasn.com/what-is-str-in-django-and-how-it-works/) to help me understand how to return several model fields as a string, so that the film title and date is shown when looking at the added objects to the FilmShowtie model at the admin page. 

When the user gets to the edit booking page, the edit form should be prefilled with the booking information of the booking that is to be edited/update. To make this work I used this [Stackoverflow page](https://stackoverflow.com/questions/604266/django-set-default-form-values) to help me understand how it could be done.

Each registered user should only see it´s own bookings. I used [this Stackoverflow page](https://stackoverflow.com/questions/11833305/django-only-showing-the-users-own-data) to understand how to make this happen in this project.

[This site](https://koenwoortman.com/python-django-form-field-placeholder/) was used to understand how to set placeholder text on extra input form fields added to the django allauth user model. 

The [Django documentation](https://docs.djangoproject.com/en/2.2/ref/validators/#writing-validators) for validation of user input to form was used to understand how to validate that only 1-8 tickets can be booked.

To increase Lighthouse accessability scores by adding form labels I used these pages to understand how to do add the labels and hide them: [Django form documentation](https://docs.djangoproject.com/en/4.2/topics/forms/), [Stackoverflow page on hiding labels](https://stackoverflow.com/questions/40029976/how-to-hide-label-for-css) and [Stackoverflow on labels](https://stackoverflow.com/questions/12597780/how-can-i-hide-a-django-label-in-a-custom-django-form).

To customize the django allauth signup form to include first and last name, I used code from this [Geeksforgeeks.org](https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/) page. The code is used on line 10-23 in forms.py. To make the email field required and unique I used [this](https://stackoverflow.com/questions/23956288/django-all-auth-email-required) and [this](https://stackoverflow.com/questions/27967319/django-allauth-email-login-always-wrong) Stackoverflow page to understand how to do this. 

[This page](https://django-allauth.readthedocs.io/en/latest/configuration.html) was used to understand how to remove the "Remember me" functionality for the user registration, by adding `ACCOUNT_SESSION_REMEMBER = False` in settings.py. 

All information about the films is taken from [Imdb.com](https://www.imdb.com/?ref_=nv_home). Most trailers are hosted at Imdb, but some are hosted on Youtube.com. 

I used [this Geeksforgeeks.com page](https://www.geeksforgeeks.org/best-full-stack-project-ideas/) to get ideas on what kind of project to build.

This [Youtube video](https://www.youtube.com/watch?v=fQo9ivqX4xs) helped me to better understand how a Django app is built and how to use Cloudinary.

This [Pluralsight guide](https://www.pluralsight.com/guides/break-down-agile-user-stories-into-tasks-and-estimate-level-of-effort) was used to better understand how to create good acceptance criteria and tasks for the user stories. 

When creating my GitHub issues template for the user stories, I used Code Institutes example of an issue template shown in [this video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+AG101+2021_T1/courseware/a4e548ca70a3473aa890ba2ab9bf612c/db69a5829de8467eb071e63bde630a2e/). I also used the issue labels shown in [this Code Institute lesson](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+AG101+2021_T1/courseware/a4e548ca70a3473aa890ba2ab9bf612c/71fe6c52cccf477688e924c9889f5fec/?child=first) in my project, as I think they are very useful for prioritization. 

When creating the user stories for this project, I used the stories for Code Institutes Django blog shown in [this lesson](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/) as the starting point and then adjusted them to my project and added more. 

[This Topcoder.com page](https://www.topcoder.com/thrive/articles/project-management-on-github) was used to understand how to create an epic in GitHub. 

When adding a new posts to a model, via the admin site, by default the new posts are shown in the admin site list as '<model name> Object (1)', '<model name> Object (2)' and so on. To show a meaningful string instead, so that each post is understandable the below function was taken from the [Hello Django project](https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py).
`def __str__(self):
    return self.<model field>`

[Tinypng.com](https://tinypng.com/) was used to minimize the image size of all images used.

I used the readme.md file for [The Easy Eater project](https://github.com/AliOKeeffe/PP4_My_Meal_Planner) as inspiration for the readme.md file for this project. I also used the entity-relationship diagram made for that project to help identify what data types to use for the data in this project. More inspiration for the readme was gotten from the [Traffic Sign Memory project](https://github.com/sarasm93/traffic-sign-memory).

The user interface design for this project was inspired by the website for [Spegeln cinema](https://biografspegeln.se/). 

All images used come from Pixabay.com, Unsplash.com and Pexels.com.
- [Barbie](https://pixabay.com/photos/barbie-doll-toy-girl-barbie-doll-2380468/)
- [David Bowie](https://unsplash.com/photos/JIbTSKqnews)
- [Star wars](https://pixabay.com/photos/star-wars-movie-log-support-2172955/)
- [Iron man marathon](https://pixabay.com/photos/iron-man-superhero-edit-hero-man-4228269/)
- [Supermario animerat](https://www.pexels.com/sv-se/foto/konst-sot-fargrik-figur-163077/)
- [The evil doll](https://unsplash.com/photos/LPl7HqeHUJk)
- [Transformers](https://pixabay.com/photos/transformers-optimus-prime-car-1333083/)
- [Mamma mia sing along](https://pixabay.com/photos/the-star-of-pop-music-figure-of-wax-3981219/)
- [Interstellar](https://pixabay.com/photos/moon-landing-apollo-11-nasa-space-4924131/)

[Tinypng](https://tinypng.com/) was used to compress the images.

## **Acknowledgements**

I would like to thank my mentor Antonio Rodriguez for helping me with this project, specifically helping me get the booking form working correctly.