# The Gamer's Forum

The Gamer's Forum is a website for gamers of all creeds (console, PC or mobile) to discuss all things video gaming. The website is divided up into different gaming related topics, under which posts can be created and users can also then reply to any post that they would like to either add to or express an opinion on. Only registered users are able to add posts or replies. Owners of posts are also able to edit and delete their posts. There is also a contact form should a user need to send a message to admin for whatever reason.

![Image of application pages on different screen sizes](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/am_i_responsive.JPG)

[Link to deployed site](https://the-gamers-forum.herokuapp.com/)

## UX

### Imagery

My application doesn't feature any imagery as such, however it does make use of Font Awesome icons where needed to add a bit of visual enhancement. 

### Typography

The fonts used for my website are "Audiowide" for the site name "The Gamer's Forum" and then "Merriweather" for all other text on the site. 

### Colour scheme

The colour scheme on my site features darker blue and green colours as follows:

![Image of #006473](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/006473.JPG) - Used for the header background and also main button colour<br>
![Image of #2F4858](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/2f4858.JPG) - Used for the footer background and also darker coloured fonts<br>
![Image of #FDDE6C](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/fdde6c.JPG) - Used for the site name "The Gamer's Forum", as seen in the header<br>
![Image of #81AD36](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/81ad36.JPG) - Used for a hover colour for links and some lighter coloured text<br>
![Image of #FFEFCA](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/ffefca.JPG) - Used for the background on the topic overview cards on the homepage<br>
![Image of #299A5E](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/299a5e.JPG)  - Used a hover font colour for the topic overview cards on the homepage<br>
![Image of "whitesmoke"](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/whitesmoke.JPG) - Used for light coloured text where needed<br>

### Schema

Please see below an overview of the schema for my application:

![Image of schema overview](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/schema.JPG)<br>

The details of each schema is as follows:

- Topic table<br>
![Image of topic schema](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/topic_schema.JPG)
- Post table<br>
![Image of post schema](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/post_schema.JPG)
- Reply table<br>
![Image of reply schema](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/reply_schema.JPG)
- Contact table<br>
![Image of contact schema](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/contact_schema.JPG)<br>
As can be seen above, the builtin Django user table as well as the topic, post and reply tables are all linked so that if a user is removed from the system, all of their associated posts and replies would be removed too.<br>
Like-wise, if a topic was removed, all associated posts and replies would be too. Also, removing a post deletes all associated replies. The contact table is standalone and used only for the Contact Us function.

### Wireframes

Please see below the desktop view wireframes for my application:

Homepage:<br>
![Wireframe of homepage](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_home.JPG)<br>
Topic detail page:<br>
![Wireframe of topic detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_topic_detail.JPG)<br>
Post detail page:<br>
![Wireframe of post detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_post_detail.JPG)<br>
Login page:<br>
![Wireframe of login page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_login.JPG)<br>
Logout page:<br>
![Wireframe of logout page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_logout.JPG)<br>
Sign up page:<br>
![Wireframe of signup page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_signup.JPG)<br>
Post add page:<br>
![Wireframe of add post page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_add_post.JPG)<br>
Contact us page:<br>
![Wireframe of contact us page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_contact_us.JPG)<br>

To see all the wireframes, including those for mobile and tablet as well, link is as follows:

[Link to all wireframes](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/pp4_wireframes.pdf)<br>

As can be seen, the final design of my application differs slightly from the wireframes. This is due to further discussion with my mentor as the project went on, as well as other design tweak choices.<br>
An example would be with the mobile homepage view, the topic card elements all run the full width of the screen in the final version, instead of being in a 3 x 2 grid layout. 

### User Stories:

#### New users:

- As a site user I can view topics to find related posts 
- As a site user I can register an account to be able to use features reserved for site members
- As a site user I can log into the website so that I can participate in the community fully
- As a site user I can log out of my account so that it remains secure if the site is visited from a shared PC for instance
- As a site user I can view posts in detail to be able to read them fully
- As a site user I can make new posts to ask questions or state an opinion
- As a site user I can edit my posts so that I can update them if needed
- As a site user I can delete my posts so that I can remove them if no longer needed
- As a site user I can post replies to existing posts so that I can express my opinion about them
- As a site user I can fill out a contact form if I wish to make site admin aware of issues or feedback
- As a site admin I can manage topics so that I can add to, modify or remove them
- As a site admin I can remove posts if they breach community rules
- As a site admin I can remove replies to posts if they breach community rules
- As a site admin I can remove users if they breach community rules


#### Returning users:

- As a returning site user I can see whether any new topics have been added
- As a returning site user I can see if any new posts have been added since my last visit
- As a returning site user I can see whether any replies have been added to any of my posts
- As a returning site user I can see whether any new features have been added to the site

#### Frequent users:

- As per returning users

## Features

### Existing Features

The application features a header containg a nav element which is responsive and collapes for narrower viewports; you would see a "hamburger" icon to the right of the nav element, with the nav links below that, if viewed on a smaller screen:

![Image of header](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/header.JPG)<br>

The homepage features an overview of topics to select from as well as some of the most recent posts:

![Image of homepage](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/homepage.JPG)<br>

There is a footer containing links to social media pages:

![Image of footer](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/footer.JPG)<br>

There is a login page:

![Image of login page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/login.JPG)<br>

There is a logout page:

![Image of logout page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/logout.JPG)<br>

There is also a sign up page:

![Image of sign up page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/signup.JPG)<br>

Clicking on a topic reveals the detail page for that topic:

![Image of topic detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/topic_detail.JPG)<br>

There is a page to add a new post (only visible to logged in users):

![Image of post add page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/add_post.JPG)<br>

When adding a post, there are messages to show whether this has been successful or not:

![Image of post add success message](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/post_add_success.JPG)<br>
![Image of post add failure message](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/post_add_failure.JPG)<br>

Clicking on a post shows the post detail view, which also allows for replying to a post (only logged in users can reply):

![Image of post detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/post_detail.JPG)<br>

If a logged in user replies to a post, there is a confirmation:

![Image of post reply confirmation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/reply_add_confirmation.JPG)<br>

If a user is the owner of a post, they will also see "Edit" and "Delete" buttons below the post:

![Image of edit and delete buttons](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/edit_delete.JPG)<br>

There is a page for editing of existing posts:

![Image of post edit page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/edit_post.JPG)<br>

When editing a post, there are messages to show whether this has been successful or not:

![Image of post edit success message](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/post_edit_success.JPG)<br>
![Image of post edit failure message](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/post_edit_failure.JPG)<br>

If a user chooses to delete one of their posts, there is an "are you sure" modal and then confirmation message:

![Image of post delete modal](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/delete_post.JPG)<br>
![Image of post delete confirmation message](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/post_delete_confirmation.JPG)<br>

Finally, there is a contact us page for any user (logged in or not) to submit a message to admin:

![Image of contact us page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/contact_us.JPG)<br>

### Features Left to Implement

- Allow users to upload images for their posts or replies
- Allow users to upvote \ downvote posts
- Add a function allowing users to flag posts or replies to admin for review

## Technologies Used

### Languages

- HTML - Required for the render templates
- CSS - Used to provide required custom styling for the templates
- JavaScript - Used to provide custom code to automatically dismiss messages
- Python - The language that the Django framework is based on

### Libraries

- Bootstrap - Used for various components in the templates as follows:
    - Navbar - For navigation element in header
    - Card - For the display of topic and post details
    - Modal - Used for the post delete confirmation popup
    - Grid - To configure layout of page elements
    - CSS - Used for element styling
    - JavaScript - Used for automation of components

### Frameworks

- Django - Full stack framework used to build this application

### Platforms

- GitHub - Where code repository resides with Git version control
- Gitpod - IDE used for development with Git version control
- Heroku - Where the deployed application is served from
- Cloudinary - Where static files are stored for the deployed application

### Services

- [Mycolor.space](https://mycolor.space/) - Used for working out colour palette
- [favicon.io](https://favicon.io/favicon-generator/) - Used to generate favicon

## Testing

- As a site user I can view topics to find related posts<br><br> 
The user will land on the homepage when visting the site and can click on any of the topics to view them in more detail:
![Image of homepage](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/homepage.JPG)<br>
![Image of topic detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/topic_detail.JPG)<br>
- As a site user I can register an account to be able to use features reserved for site members<br><br>
There is a link in the nav element for "Sign Up" that takes the user to a page where they can sign up:<br>
![Image of sign up page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/signup.JPG)<br>
- As a site user I can log into the website so that I can participate in the community fully<br><br>
From the nav element, the user clicks "Login" to be taken to the login page:<br>
![Image of login page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/login.JPG)<br>
- As a site user I can log out of my account so that it remains secure if the site is visited from a shared PC for instance<br><br>
The user would click "Logout" on the nav element to navigate to the logout page:<br>
![Image of logout page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/logout.JPG)<br>
- As a site user I can view posts in detail to be able to read them fully<br><br>
From either the homepage or from within a topic detail screen, clicking on a post will show it in detail:<br>
![Image of post detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/post_detail.JPG)<br>
- As a site user I can make new posts to ask questions or state an opinion<br><br>
When viewing a topic detail screen, a logged in user can click the "Add Post" button to add a new post:<br>
![Image of post add page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/add_post.JPG)<br>
- As a site user I can edit my posts so that I can update them if needed<br><br>
As the owner of a post, a user can click on the "Edit" button to visit the post update screen:<br>
![Image of edit and delete buttons](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/edit_delete.JPG)<br>
![Image of post edit page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/edit_post.JPG)<br>
- As a site user I can delete my posts so that I can remove them if no longer needed<br><br>
The owner of the post can click on the "Delete" button to bring up the delete post modal:<br>
![Image of edit and delete buttons](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/edit_delete.JPG)<br>
![Image of post delete modal](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/delete_post.JPG)<br>
- As a site user I can post replies to existing posts so that I can express my opinion about them<br><br>
A logged in user will have the option to post a reply when on a post detail screen:<br>
![Image of post detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/post_detail.JPG)<br>
- As a site user I can fill out a contact form if I wish to make site admin aware of issues or feedback<br><br>
Any site user, logged in or not, can click on the "Contact Us" nav link to visit the contact us page:<br>
![Image of contact us page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/contact_us.JPG)<br>
- As a site admin I can manage topics so that I can add to, modify or remove them<br><br>
A site admin would login via the admin link (https://the-gamers-forum.herokuapp.com/admin) and then access the admin panel:<br>
![Image of admin login page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/admin_login.JPG)<br>
![Image of admin panel page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/admin_panel.JPG)<br>
- As a site admin I can remove posts if they breach community rules<br><br>
A site admin would be able to do this from the admin panel:<br>
![Image of admin panel page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/admin_panel.JPG)<br>
- As a site admin I can remove replies to posts if they breach community rules<br><br>
A site admin would be able to do this from the admin panel:<br>
![Image of admin panel page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/admin_panel.JPG)<br>
- As a site admin I can remove users if they breach community rules<br><br>
A site admin would be able to do this from the admin panel:<br>
![Image of admin panel page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/features/admin_panel.JPG)<br>

The application has been tested using the Chrome, Edge and Firefox browsers at full width on a 1080p and 4K monitor, as well as a Samsung Galaxy S20 FE 5G handset. The following emulated device sizes were checked:<br>
<br>

- Chrome \ Edge
    - Galaxy S5
    - Pixel 2 XL
    - iPhone 6/7/8
    - iPhone X
    - iPad
    - iPad Pro
- Firefox
    - Galaxy S10/S10+
    - Galaxy S20 Ultra
    - iPad
    - iPhone 11 Pro
    - iPhone 12/13 +
    - iPhone SE 2nd gen

In all cases, the application behaved as expected. I have tested and confirmed that the following functionality works:

- Clicking on a topic overview from the homepage takes you to a topic detail view
- Clicking on a post overview from either the homepage or under a topic detail view opens the post detail view
- Only logged in users can see the "Add Post" button or reply to a comment
- When logged in, the nav links will only show "Home \ Logout \ Contact Us" 
- When logged out, the nav links show "Home \ Login \ Sign Up \ Contact Us"
- Only the owner of a post, when logged in, can see the "Edit" and "Delete" buttons for their post
- Adding a new post via the add post screen works as expected
- Editing a post works as expected
- Deleting a post works as expected
- Submitting a message via the Contact Us page functions as expected
- An admin user can manage users, topics, posts and replies from the admin panel

### Bugs

While developing my application, the following bugs arose:

<strong>Solved:</strong>
<br> 

- Static files not loading
    - When initially creating base.html, I forgot to include {% load static %} at the top so got an error when trying to link to static files. This was corrected by adding the right syntax. 
- Link to database not working
    - During development, Heroku updated the DB path following some maintenance and so I initially couldn't connect to the DB from my development environment following this. Once the path was updated in my application, the issue was resolved.
- Account view templates not working
    - While creating the templates for the allauth views, I accidentally created the template folder as "templates/accounts", which won't work... I renamed this to "templates/account" and all worked as expected.
- Topic detail view not working
    - When configuring the URL for the topic detail view, I incorrectly set the url path to '<name:name>/' which is of course invalid. Once set to '<str:name>/' this worked as expected.
- Footer obscuring content
    - The footer was hiding content behind it, so I implemented a fix which was to create an empty div and size accordingly and set the "clear" property to both. I have also since removed the "fixed" property from the footer which now behaves as it should. 
- PostEdit view post method not working
    - While adding the post method to the "PostEdit" view, I mistakenly set the form variable to "PostAddForm(data=request.POST)" which would instead try to create a new record. Once amended to "PostAddForm(request.POST, instance=post)" this worked as expected. 
- Authentication checks in views causing errors
    - When adding the authentication checks to the views, in addition to what I've already configured on the templates, this initially caused issues due to me trying to decorate methods as if they were functions... this was corrected by using the "@method_decorator(login_required, name='post')" decorator on the required classes.
- Filter and search fields in admin view not working
    - I configured foreignkey fields in the admin view for the forums app, when initially searching on these, it would crash. This was corrected by adding "__username" to the relevant search and filter fields. 

<strong>Not solved:</strong>  
<br>

- Unsuccessful post edit temporarily shows incorrect post details
    - If unsuccessful at editing a post, when it redirects to post detail it shows what the post would've looked like had the edit worked (presumably taken from the form). If you then attempt to edit again or navigate away and come back to the post, it shows as it should. I was unable to resolve this bug prior to submission and would need to revisit it at a later date. 

### Validator testing

- HTML<br>
All template files validate correctly with no errors:<br><br>
index.html:<br>
![Image of index file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/index_html_validation.JPG)<br>
topic_detail.html:<br>
![Image of topic detail file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/topic_detail_html_validation.JPG)<br>
post_detail.html:<br>
![Image of post detail file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/post_detail_html_validation.JPG)<br>
add_post.html:<br>
![Image of add post file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/add_post_html_validation.JPG)<br>
edit_post.html:<br>
![Image of edit post file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/edit_post_html_validation.JPG)<br>
login.html:<br>
![Image of login file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/login_html_validation.JPG)<br>
logout.html:<br>
![Image of logout file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/logout_html_validation.JPG)<br>
signup.html:<br>
![Image of signup file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/signup_html_validation.JPG)<br>
contactus.html:<br>
![Image of contact us file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/contact_us_html_validation.JPG)<br>
<br>
<br>

- CSS<br>
File validates without any issues:<br>

![Image of css file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/style_css_validation.JPG)<br>
<br>

- Python<br>
All python files tested conform to PEP8 standards:<br><br>

- Forums app:<br>
admin.py:<br>
![Image of forums admin file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/admin_py_forums_validation.JPG)<br>
forms.py:<br>
![Image of forums forms file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/forms_py_forums_validation.JPG)<br>
models.py:<br>
![Image of forums model file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/models_py_forums_validation.JPG)<br>
urls.py:<br>
![Image of forums urls file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/urls_py_forums_validation.JPG)<br>
views.py:<br>
![Image of forums views file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/views_py_forums_validation.JPG)<br>
<br>


- contactus app:<br>
admin.py:<br>
![Image of contactus admin file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/admin_py_contactus_validation.JPG)<br>
forms.py:<br>
![Image of contactus forms file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/forms_py_contactus_validation.JPG)<br>
models.py:<br>
![Image of contactus model file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/models_py_contactus_validation.JPG)<br>
urls.py:<br>
![Image of contactus urls file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/urls_py_contactus_validation.JPG)<br>
views.py:<br>
![Image of contactus views file validation](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/validation/views_py_contactus_validation.JPG)<br>



## Deployment

### Initial deployment

- Gitpod
    - Create new repository from CI template
    - Install Django and required dependencies into Gitpod workspace
    - Create new Django project called "gamersforum"
    - Create procfile as required
    - Run "pip3 freeze --local > requirements.txt" to update requirements file
- Heroku
    - Log into Heroku 
    - Create new app called "the-gamers-forum"
    - Add a PostgreSQL "hobby" database as resource
    - Configure "DISABLE_COLLECTSTATIC = 1" in Config Vars
- Gitpod
    - Create env.py file and add database path from Heroku
    - Add secret key to env.py
    - Configure database path and secret key in settings.py
    - Perform commit and push to GitHub
- Heroku 
    - Under "the-gamers-forum" app, browse to Deploy
    - Connect to Github, select appropriate repository
    - Run Deploy
    - Wait for confirmation that app has deployed

### Final deployment

- Gitpod
    - Ensure all required files up-to-date and that application is working
    - Run "pip3 freeze --local > requirements.txt" to update requirements file
    - Ensure "DEBUG = False" set in settings.py
    - Perform commit and push to GitHub
- Heroku
    - Under "the-gamers-forum" app, browse to Config Vars
    - Remove the value "DISABLE_COLLECTSTATIC = 1" from Config Vars
    - Browse to Deploy and run deployment
    - Wait for confirmation that app has deployed


## Credits 

### Content

All content on the site was created by the developer.

### Media

No media files were used in the development of my project, however Font Awesome icons were used for visual enhancement.

### Acknowledgements
<br>
In addition to the content covered in the LMS and, in particular the "I Think Therefore I Blog" walkthrough project, I used the following resources for additional learning:
<br><br>
https://www.tutorialguruji.com/python/django-pass-multiple-models-to-my-listview/<br>
https://www.youtube.com/watch?v=QvTyqta3OJo<br>
https://www.youtube.com/watch?v=9aEsZxaOwRs<br>
https://stackoverflow.com/questions/51420143/django-pass-known-exact-string-as-a-url-parameter<br>
https://groups.google.com/g/django-users/c/cKd3t7yQzFo?pli=1<br>
https://stackoverflow.com/questions/13881548/sticky-footer-hiding-content<br>
https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/<br>
https://stackhowto.com/python-generate-a-random-alphanumeric-string/<br>
https://www.w3schools.com/cssref/css3_pr_text-shadow.asp<br>
https://stackoverflow.com/questions/40506827/django-how-to-allow-only-the-owner-of-a-new-post-to-edit-or-delete-the-post<br>
https://towardsdatascience.com/decorating-methods-defined-in-a-class-with-python-4b361589440<br>
https://www.fullstackpython.com/django-contrib-auth-decorators-login-required-examples.html<br>
https://stackoverflow.com/questions/11890970/django-user-object-has-no-attribute-user/35480925<br>
https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/<br>
https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains<br>
https://stackoverflow.com/questions/21938028/how-can-i-get-a-favicon-to-show-up-in-my-django-app<br><br>

I would also like to thank my mentor Akshat Garg for all his help, as well as the community on Slack for their advice and guidance. 