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

![Image of #006473](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/#006473.JPG) - Used for the header background and also main button colour<br>
![Image of #2F4858](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/#2f4858.JPG) - Used for the footer background and also darker coloured fonts<br>
![Image of #FDDE6C](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/#fdde6c.JPG) - Used for the site name "The Gamer's Forum", as seen in the header<br>
![Image of #81AD36](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/#81ad36.JPG) - Used for a hover colour for links and some lighter coloured text<br>
![Image of #FFEFCA](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/#ffefca.JPG) - Used for the background on the topic overview cards on the homepage<br>
![Image of #299A5E](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/#299a5e.JPG)  - Used a hover font colour for the topic overview cards on the homepage<br>
![Image of "whitesmoke"](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/colours/whitesmoke.JPG) - Used for light coloured text where needed<br>

### Schema

Please see below an overview of the schema for my application:

![Image of schema overview](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/schema.JPG)<br>

The details of each schema is as follows:

- Topic table
![Image of topic schema](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/topic_schema.JPG)
- Post table
![Image of post schema](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/post_schema.JPG)
- Reply table
![Image of reply schema](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/reply_schema.JPG)
- Contact table
![Image of contact schema](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/contact_schema.JPG)<br><br>
As can be seen above, the builtin Django user table as well as the topic, post and reply tables are all linked so that if a user is removed from the system, all of their associated posts and replies would be removed too. Like-wise, if a topic was removed, all associated posts and replies would be too. The contact table is standalone and used only for the Contact Us function.

### Wireframes

Please see below the desktop view wireframes for my application:

![Wireframe of homepage](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_home.JPG)<br>
![Wireframe of topic detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_topic_detail.JPG)<br>
![Wireframe of post detail page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_post_detail.JPG)<br>
![Wireframe of login page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_login.JPG)<br>
![Wireframe of logout page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_logout.JPG)<br>
![Wireframe of signup page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_signup.JPG)<br>
![Wireframe of add post page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_add_post.JPG)<br>
![Wireframe of contact us page](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/wireframes/wireframe_contact_us.JPG)<br>

To see all the wireframes, including those for mobile and tablet as well, link is as follows:

[Link to all wireframes](https://raw.githubusercontent.com/domsq/the-gamers-forum/master/screenshots/pp4_wireframes.pdf)<br>

As can be seen, the final design of my application differs slightly from the wireframes. This is due to further discussion with my mentor as the project went on, as well as other design tweak choices.

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

### Features Left to Implement

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

## Testing

## Deployment

## Credits 

### Content

### Media

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
https://stackoverflow.com/questions/40506827/django-how-to-allow-only-the-owner-of-a-new-post-to-edit-or-delete-the-post