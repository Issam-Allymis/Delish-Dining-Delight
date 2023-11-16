# DelishDiningDelight Project portfolio 4

![banner](https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/c7a21173-3058-4e18-beea-f59872654ce6)

The blog's initial design and feature set deviated from my original intent. Originally conceived with a broader range of functionalities, I opted for a simplified approach due to time constraints and the realization that a more intricate project would be challenging to deliver within the available timeframe. The complexity became overwhelming, and it became evident that meeting the desired standards would be a considerable challenge given the time limitations incurred during my academic pursuits.
So, I have put together this simple recipe blog that's all about easy vibes and good food. Picture a laid-back design splashed with colors and mouth-watering images, urging the user to get outdoors and whip up some tasty dishes! If you're feeling chatty, you can sign up to drop comments and likes on your favorite recipes. 
And for the behind-the-scenes magic, I have hooked up the admin side. Admins can create, read, update, delete posts and comments, also known as (CRUD). It's like a backstage pass to keep things in check.
The goal? Blend simplicity with eye candy and throw in some interactive flair. The result? A cozy corner where you're not just scrolling through recipes, but diving into the conversation and sharing your foodie delicious thoughts.

## UX

### User Stories
**New User:**
* Sign Up: As a new user, I want to sign up to access exclusive features.

**Existing User**
* Sign In: As an existing user, I want to sign in to save and share my favorite recipes.
* Reset Password: As an existing user, I want to reset my password if I forget it.
* Homepage Navigation: As a user, I want to easily navigate the homepage to discover new recipes.
* View Recipe Reviews: As a user, I want to view reviews from others on a recipe.
* Leave Recipe Reviews: As a user, I want to leave reviews on recipes I've tried.
* Like/comment Recipes: As a user, I want to like/comment on recipes to show appreciation.
* Comment Confirmation: As a user, I want to receive a notification popup confirming the submission of my comment.

**Site Admin**
* View All Recipes: As a site admin, I want to view all recipes to monitor the variety of content.
* Review Recipe Submissions: As a site admin, I want to review and approve submitted recipes before they are published.
* Remove Inappropriate Content: As a site admin, I want to remove recipes that violate community guidelines.
* Recommend Featured Recipes: As a site admin, I want to feature certain recipes on the homepage for increased visibility.

**Future Features** 
* Remove Recipes: As a user, I want to remove recipes from my saved list.
* Submit Recipe: As a user, I want to submit my own recipes to share with the community. 
* Save Recipes: As a user, I want to save recipes to my profile for quick access.
* Remove Recipes: As a user, I want to remove recipes from my saved list.
* Submit Recipe: As a user, I want to submit my own recipes to share with the community.
* Recipe Rating: As a user, I want to rate recipes to help others find the best ones.
* Recipe Recommendations: As a user, I want to receive personalized recipe recommendations based on my preferences.
* Styled Email Notifications: As a user, I want email notifications about recipe updates to be visually appealing.
* Update Recipe: As a user, I want to update my submitted recipes.
* Delete Recipe: As a user, I want to delete my submitted recipes. 


### Site Goals
* This blog is crafted with a visually pleasing and informative design that is intuitive and easy to navigate
* This blog allows users to easily sign in, enabling them to like/unlike and comment on each recipe.

### Tasks
The tasks during the development of this project were closely aligned with Code Institute's "I Think Therefore I Blog" walkthrough project, following a specific order:

### Before the project commencement
* Design Wireframes
* Create a repository in GitHub
* Establish Project, Epics, User Stories, and prepare the Kanban board

### Creating the project in Gitpod
* Initiating the project in Gitpod
* Setting up the Django project
* Deploying to Heroku
* Creating database models
* Constructing the Admin site
* Configuring templates
* Installing Allauth for sign-in, sign-up, and log-out pages
* Incorporating Crispy forms to enhance the styling of the Django Admin account
* Conducting manual and automatic testing, as well as validation checks for each page
* Final deployment

## Visual Design
### Wireframes
I utilised [Canva](https://www.canva.com/) to craft the initial wireframes, outlining the intended appearance and structure of the blog. However, as the development progressed, I made the decision to omit certain features that were initially planned.
### Home Page Desktop
![WhatsApp Image 2023-11-14 at 14 55 04 (5)](https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/fc67555c-3c53-42b7-94e3-918127ba647d)

### Home Page Mobile
![WhatsApp Image 2023-11-14 at 14 55 04 (4)](https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/0117e1a5-39e0-4eb6-a628-854e537ce50f)

### Form Desktop
![WhatsApp Image 2023-11-14 at 14 55 04 (3)](https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/f9f95ae7-53b6-47ce-b3ce-3e91070c9ae0)

### Form Mobile
![WhatsApp Image 2023-11-14 at 14 55 04 (2)](https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/2e2ec2e2-663d-4d1e-9ffa-e7f5685163ce)

### About Us Desktop
![WhatsApp Image 2023-11-14 at 14 55 04 (1)](https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/0eddbf68-c731-4f99-8d8d-395707164e4a)

### Abous Us Mobile
![WhatsApp Image 2023-11-14 at 14 55 04](https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/c8c6c3a3-7e7b-41f3-9fe8-55026e07d16a)

## Colours
<img width="150" alt="colour" src="https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/de4096c5-02de-4bec-96f4-f0ad3b3036c4">

<img width="62" alt="colour 2" src="https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/b96eea47-a491-4242-9089-8c78514c6e22">

<img width="47" alt="colour 1" src="https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/c6209b92-3c33-4e4d-b16d-a6da631a0964">

<img width="49" alt="colour 3" src="https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/75f0fb7b-27bf-481d-9d1f-25bd194dad60">

<img width="67" alt="colour 4" src="https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/ed3348d4-cfc3-441b-a921-539aa1a486b6">

I selected black, red, and grey for their eye-friendly appeal, and the straightforward, laid-back aesthetic significantly enhances the prominence of the images.

## Fonts
I explored font options for this web design on the [Google Fonts](https://fonts.google.com/) website, settling on these fonts to impart a sense of elegance and cleanliness to the overall look.

## Icons
<img width="386" alt="footer" src="https://github.com/Issam-Allymis/Delish-Dining-Delight/assets/126810074/b181bc8f-b843-49f1-9d92-64d83aac0585">

The social media icons featured in the footer are sourced from the [Font Awesome](https://fontawesome.com/)
website.


## Technologies Used
### Languages
* **HTML**: Responsible for page markup.
* **CSS**: Utilized for styling purposes.
* **Python**: Implemented to develop Django functionality, including building models, forms, and views for the app.
* **JavaScript**: Applied for automatic disappearance of alerts.

### Framework, Libraries & Programs
* **Django**: Employed for constructing the app's models, forms, and views.
* **Bootstrap**: Utilized to ensure the site's responsiveness.
* **Summernote**: Implemented to empower the admin with the ability to add styling while creating a new blog post.
* **Google Fonts**: Incorporated for diverse font styles.
* **Crispy Forms**: Utilized to enhance the visual appeal of the admin form/login interface.
* **Font Awesome**: Applied for integrating appealing icons into the design.

