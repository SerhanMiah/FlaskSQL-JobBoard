# FlaskSQL-JobBoard
#### Video Demo:  <URL https://www.youtube.com/watch?v=UPHEz1tlYCw>
#### Description:
  ## Final Project 

For my final project, I built a full-stack web application using a combination of Flask, Python, CLI, AJAX, JavaScript, NodeJS, React, Bootstrap, Insomnia, and SQLite3. The project consists of a backend API built with Flask that connects to a frontend web application built with React and Bootstrap. The API is powered by a SQLite3 database and supports CRUD operations for managing resources.

One of the main features of the project is its CLI interface, which allows users to interact with the backend API using a command-line interface. The CLI is built with Python and supports a variety of commands for querying, creating, updating, and deleting resources.

The frontend web application is built with React and uses AJAX to communicate with the backend API asynchronously. The user interface is designed using Bootstrap and Jinja templates and provides a seamless experience for browsing and managing resources.

To test the API and debug any issues, I used Insomnia, a powerful REST API client that allows me to send HTTP requests and inspect responses in real-time. Overall, this project helped me gain a deeper understanding of full-stack web development and gave me hands-on experience with a wide range of technologies and tools.


## Code Installation:

Clone or download the repo then in your Terminal run the following commands:

* Clone or download the repository: This step involves downloading the source code of the Flask application from the GitHub repository.
* Install back-end dependencies: This step involves installing the required packages or modules that the Flask application depends on using the pip install command.
* Enter environment for project: This step creates a virtual environment for the project using the python3 -m venv command. This isolates the application's dependencies from the system-level dependencies and ensures that the application runs smoothly.

* Enter environment for project: This step creates a virtual environment for the project using the python3 -m venv command. This isolates the application's dependencies from the system-level dependencies and ensures that the application runs smoothly.

* Activate the environment: This step activates the virtual environment using the source venv/bin/activate command, so that any subsequent commands run within the virtual environment.

* Run application: This step starts the Flask application using the python run.py command.


## The Brief

* Build a full-stack application by making your backend and your frontend
* Use by using Flask to create a backend to serve your data from a Postgres database
* Consume your API with a separate front end built with JinJa, CSS, Bootstrap, SASS
* Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models
* Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut
* Be deployed online so it's publicly accessible.


## Technologies used:

### Front end:
* CSS
* HTML
* JINJA

### Back end:
* Python
* Flask
* FlaskSQL
* Table Plus
* pyJWT

### Dev Tools:
* VS code
* Yarn
* Insomnia
* Git
* Github
* Google Chrome dev tools
* Excalidraw (wireframing)
* Slack

## Phase

This project consisted of four phase

### Phase 1 - (Planning):

By using LucidChart, simply another tool for planning like Excalidraw but specifically for detailing Entity Relationships. The above is showing how I would link OneToMany and ManytoMany relationship between the user, venue, category, review and join apps and models. 	
Throughout my planning, I used Git and GitHub for version control and decided that since I am working on this solo it would be good practice to work on branches and add, commit and push changes regularly. During the project, I created a Trello with a completed task list. To ensure that I focus on one task at a time and to make sure that I complete the work. By creating a to-do list I was able to keep on top of the project.


### Phase 2: Creating the Models with Flask, FlaskSQL:

During the second phase of my project, I used Flask and FlaskSQL to create the backend of my web application. Firstly, I created a new file named app.py and imported the Flask module, which allowed me to create a new instance of the Flask class. Then, I defined routes to handle incoming requests using the render_template method to generate a page on the local host.

To use FlaskSQL, I installed the Flask-SQLAlchemy extension, which allowed me to create a database for my application. I defined a model for the database using a Python class, which defined the structure of the database.

Using the Python shell, I created the database and used the model to create tables inside the database. Once the database tables were created, I was able to use them in my Flask app to retrieve data. For example, I used the User model to query all users and returned them to the user interface.

Overall, Flask and FlaskSQL were instrumental in creating the backend of my web application, and there are many other aspects of Flask development that I was able to explore and implement to build a robust web application.


### Phase 3 - Redoing the models and connecting to Railway Postgres 

Overall, I was very pleased with the outcome of the Flask application and the seamless integration of the database. In the third phase, I took the initiative to overhaul most of the models to enable users to track their job applications more efficiently, establishing database relationships between the Job and Application models.

To enhance the job searching experience, I added more detailed information to the Job model, such as the job's active status, salary range, posting date, and more. This helped me to create a job search experience similar to Indeed.

After refining the database, I decided to migrate to PostgreSQL. I used Railway to create the database and connected it using a PostgreSQL URL connection specified in the environment model.


### Phase 4 Styling the Frontend

Over the past few days, I have poured my creative energy into designing a website that truly reflects my personal style. By leveraging the powerful combination of FlaskSQL, Jinja, and SASS, I was able to add a level of sophistication and polish to the site's design that truly sets it apart.

In addition to aesthetics, I also devoted time to optimizing the site for mobile devices through code refactoring and implementation of CSS media. I also integrated Flask pagination, which ensures that visitors to the site can easily navigate through its many pages.

These enhancements have truly elevated the site's functionality and aesthetics to new heights, making it a truly immersive and engaging experience for all who visit.

## Wins & Challenges

### Win
* During my experience using Flask, I faced a challenge with SQL and building relationships between models. It required a creative approach to dealing with models that had multiple or single relationships in the backend. However, this challenge was a significant win for me as I gained valuable experience and knowledge in working with FlaskSQL.
* One of my biggest accomplishments during this project was integrating Cloudinary into my Flask app. I was able to successfully upload and retrieve image URLs, which was a valuable addition to the app's functionality. This win not only enhanced the app's aesthetics but also provided a better user experience for users interacting with the app. Overall, using Flask and integrating various functionalities, such as Cloudinary, was a challenging but rewarding experience that allowed me to improve my skills and knowledge in web development.

### Challenges
* One of the most significant challenges I faced while developing the Flask app was organizing and routing the application. As the number of routes grew, it became increasingly difficult to manage and maintain them. To address this issue, I turned to Flask Blueprints, which helped me to organize the routes and separate the application's functionality into smaller, more manageable pieces. However, as the routes became more complex, it still required a considerable amount of effort and creative thinking to ensure they were correctly organized and routed.


### Bugs
* One of the major bugs I encountered was related to updating the job board, specifically allowing users to track their applications. While implementing this feature, I struggled with using Jinja, which was a new framework for me. Although challenging, I found the experience to be rewarding as it allowed me to expand my skills and knowledge. However, I still need to go back and complete the bug fix for this feature.


## Future Content and Improvements:

* I would like to fix the edit review button so that only users who made the comments/reviews can edit or delete their reviews.
* I would like to update some of the stylings and see if I could get the like, dislike and attend working on the project.

## Key learnings
Working on my latest project was a unique and rewarding experience, as it was my first time using Flask to build a Rest-API that connects to the frontend using Postgres. Having previously worked with MongoDB and Django, I was thrilled to explore a new framework that offered a more intuitive and responsive development experience.

Although there was a bit of a learning curve when it came to understanding Flask's routing and permission systems, once I became familiar with these concepts, I was able to build my app and models quickly and with relative ease. The framework's flexibility and versatility enabled me to develop complex and sophisticated applications without being slowed down by tedious and time-consuming coding.

One of the most enjoyable aspects of working with Flask was the speed at which I was able to see results. With this framework, I was able to rapidly prototype and iterate on my project, allowing me to get a working prototype up and running in no time. However, I did come to realize that having a strong understanding of how relationships work between different models was crucial for creating a robust and functional application.

All in all, working with Flask was a fantastic experience that allowed me to expand my knowledge and skills as a developer, while also delivering a high-quality project that met all of my requirements.
