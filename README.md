<p id="top"></p>

![Entrepreneur's Bookshelf Icon](https://i.imgur.com/JJC2MEUt.jpg)

---

## Index

- <a href="#project">Project Definition 📃</a>
- <a href="#ux">UX 💻</a>
- <a href="#features">Features ⚙</a>
- <a href="#technologies">Technologies Used 🔩</a>
- <a href="#testing">Testing 🧪</a>
- <a href="#deployment">Deployment 🚀</a>
- <a href="#credits">Credits 👉</a>

---

<span id="project"></span>

# Entrepreneur's Bookshelf 📚

This project presents a to-read list focused on entrepreneurship, with book categories focused on the different areas that an entrepreneur must manage and consider.

One of the purposes of this project is to demonstrate the developer skills with Python, Flask and MongoDB. You will be able to see this in the section of the app:

- The app has a base.html page and the other pages are an extension of it.
- Logics are built within each HTML page to show specific information.
- All book's data are stored on MongoDB, and the app continuously pulls and pushes information as required.
- The reader registration, allowing readers to create an account.
- The login and logout, allowing readers to access and exit their accounts.
- The editing option, allowing readers to edit (update) the books they list.
- The reading option, allowing readers to mark books as read, which removes the book from the list.
- The admin profile, which allows for management of the app's categories.
- The search function, allowing readers to search within the books listed by keyword.

You can run and view the project by following this URL: <a href="https://flask-book-manager-project.herokuapp.com/" rel="noopener" target="_blank">View Project</a> 🚀.

_This project is for educational purposes only._

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<span id="ux"></span>

## 1. UX 💻

### 1.1 Who is this app for? 👨‍👩‍

This app is for entrepreneurs interested in keeping track of their reading priorities to improve their knowledge and skills related to starting and running a business, therefore, improving their probability of success.

Readers will also have a chance to see books that other entrepreneurs are reading.

### 1.2 What is it that they want to achieve? 🎯

Readers visit the app for different reasons. They want to:

- Keep track of their entrepreneurship reading.
- Learn about what others entrepreneurs are reading.
- Get in touch with the developer behind the project.

### 1.3 How my project is the best way to help them achieve those things? 👨‍💻

The Entrepreneur's Bookshelf provides all the necessary features to allow readers to keep track of their reading. Much like what a to-do list offers, this app offers a to-read list focused on entrepreneurship.

It also provides a clear vision of what other entrepreneurs are reading, giving them inspiration for their next books.

#### 1.3.1 Keep track of their entrepreneurship reading. ✅

The app allows entrepreneurs to:

- Register and create an account.
- Add new books to the reading list (Book title and author).
- Set a read by date to each book.
- Set priority for essential books.
- Edit the books they added.
- Mark books as read and remove them from their list.

#### 1.3.2 Learn about what others entrepreneurs are reading. 📚

The app allows entrepreneurs to:

- Go through all the books that are listed in the app.
- Easily check the book's title, author, category and the ready by date set by the entrepreneur.
- Search for specific keywords and view only the books matching it.

#### 1.3.3 Get in touch with the developer behind the project. 📧

The app provides:

- A "Get in Touch" link in the footer which readers can use to get in touch with the developer. The link points to the developer's email address.

### 1.4 App Wireframes 💻📱

As the project was inspired by the to-do list from the CI Full-Stack course, no wireframes were developed, as the design maintains most of the same structure.

There are clear differences between the to-do mini-project and this one. However, the developer did not consider them to be sufficient on their own to require any wireframes.

### 1.5 Design Decisions 🎨 🖌

First and foremost, the essential elements that had to be in place were:

- **Responsiveness**: The app has to be fully responsive and adapt to different screen sizes.
- **Interactivity**: The site has to provide users with interactivity and with more than just one type to demonstrate different managements of JS and CRUD development.
- **Simplicity**: The app has to be simple, easy to navigate, read and interact.

This project was developed to be presented as Milestone 3 for CI's Full Stack Software Development course. MS3 requires the explicit use of Python, Flask, MongoDB and CRUD development to provide site visitors with interactivity and data management, so the decision was made to focus on a simple overall app, but with clear, interactive elements and management levels in it.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<span id="features"></span>

## 2. Features ⚙

- **Navigation bar:** It allows readers to easily access all the sections of the app and content, at all times.
- **Home page:** It welcomes readers with the list of all books already entered in the bookshelf. It also provides easy navigation. If a reader is logged in, they will also be able to edit their books and mark them as read.
- **Footer section:** It allows readers to know the purpose of the app, get in touch with the developer and know a bit more about him by visiting his website.
- **Registration:** It allows visitors to register as readers in the app.
- **Logging In:** It allows registered readers to access their accounts.
- **Adding a new book:** It allows readers to add books to their to-read list.
- **Profile page:** Readers can view all books they have yet to read. It also allows them to edit the book if needed, and mark them as read.
- **Manage Categories page:** It allows the admin of the app to manage the book categories. That includes adding new categories, editing and deleting existing ones.
- **Logging Out:** It allows registered readers that are logged in into their accounts, to log out from them.

### 2.1 Potential Features/Improvements 🧰

- **Archiving books:** Instead of marking books as read and removing them from the readers' view, there's potential to archive them, and not delete them from the database.
- **Recovering archived books:** Give readers an option to unarchive the books that they marked as read in the past.
- **Adding already listed books to their profile:** Allow readers that are reviewing books listed by other readers, also to add them to their own to-read list.
- **Readers communication:** To allow readers to communicate with each other.
- **Sorting:** Give readers an option on how they would like to sort the list of books.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<span id="technologies"></span>

## 3. Technologies Used 🔩

### 3.1 Languages 🗣

- <a href="https://en.wikipedia.org/wiki/HTML5" rel="noopener" target="_blank">**HTML/HTML5**</a>
  - The project used **HTML/HTML5** as this is the essential language of web apps.
- <a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets" rel="noopener" target="_blank">**CSS/CSS3**</a>
  - The project used **CSS/CSS3** to provide the styles for the app.
- <a href="https://en.wikipedia.org/wiki/JavaScript" rel="noopener" target="_blank">**JavaScript**</a>
  - The project used **JavaScript** to provide the interactivity for the app.
- <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" rel="noopener" target="_blank">**Python**</a>
  - The project used **Python** to assist with the development of the app and the communication with the database.

### 3.2 Frameworks ⌨

- <a href="https://materializecss.com/" rel="noopener" target="_blank">**Materialize CSS**</a>
  - The project used the **Materialize CSS** framework to help design the app faster and easier.
- <a href="https://flask.palletsprojects.com/en/1.1.x/" rel="noopener" target="_blank">**Flask**</a>
  - The project used the **Flask** framework to assist with the Python development.

### 3.3 IDEs 🖥

- <a href="https://www.gitpod.io/" rel="noopener" target="_blank">**Gitpod**</a>
  - The project used the **Gitpod** IDE to develop the app.

### 3.4 External Hostings 🏢

- <a href="https://github.com/" rel="noopener" target="_blank">**GitHub**</a>
  - The project used the **GitHub** hosting service to save the project in a repository.
- <a href="https://www.heroku.com/" rel="noopener" target="_blank">**Heroku**</a>
  - The project used the **Heroku** service to deploy, manage, and scale the app.
- <a href="https://www.mongodb.com/" rel="noopener" target="_blank">**MongoDB**</a>
  - The project used the **Atlas - MongoDB** database service to store the readers, books and categories.
- <a href="https://imgur.com/" rel="noopener" target="_blank">**Imgur**</a>
  - The project used the **Imgur** service to host and access images online.
- <a href="https://drive.google.com/" rel="noopener" target="_blank">**Google Drive**</a>
  - The project used the **Google Drive** service to host and access others files and documents online.

### 3.5 Other Tools 🧰

- <a href="https://autoprefixer.github.io/" rel="noopener" target="_blank">**Auto-Prefixer**</a>
  - The project used the **Auto-Prefixer** to add CSS compatibility with other browsers.
- <a href="http://jigsaw.w3.org/css-validator/" rel="noopener" target="_blank">**W3C CSS Validation Service**</a>
  - The project used the **W3C CSS Validation Service** to validate the CSS code.
- <a href="https://validator.w3.org/" rel="noopener" target="_blank">**W3C Markup Validation Service**</a>
  - The project used the **W3C Markup Validation Service** to validate the HTML code.
- <a href="https://hackmd.io/" rel="noopener" target="_blank">**HackMD**</a>
  - The project used the **HackMD** to edit the README file.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<span id="testing"></span>

## 4. Testing 🧪

### 4.1 Testing Tools ⚗

- <a href="https://developers.google.com/web/tools/chrome-devtools" rel="noopener" target="_blank">**Chrome DevTools**</a>
  - The project used **Chrome DevTools** to test variations to the CSS rules and ideas to its optimisation.
  - The project also used it to <a href="https://developers.google.com/web/tools/chrome-devtools/device-mode" rel="noopener" target="_blank">**Simulate Mobile Devices**</a> and test the app behaviour on mobile views.
- <a href="https://en.wikipedia.org/wiki/IPhone_12" rel="noopener" target="_blank">**iPhone 12**</a>
  - The project used an **iPhone 12** mobile device to test the app in a real mobile environment.
- <a href="https://en.wikipedia.org/wiki/IPad_(2017)" rel="noopener" target="_blank">**iPad (5th Generation)**</a>
  - The project used an **iPad (5th Generation)** mobile device to test the app in a real mobile environment.

### 4.2 Testing Planning ✅

Details about how testing was conducted and the outcomes.

#### 4.2.1 Planning. 📑

The developer decided that testing was going to be conducted in parallel with the project development, which means that regularly, during the development of the project, the developer used Chrome DevTools to test the behaviour of the project both in desktop and mobile views.

The JS interactive elements and database management were tested with its development, to make sure that the code was providing the expected outcomes consistently.

Testing the project in mobile devices was conducted towards the project's end, and only once all main sections were implemented and tested with CDT.

#### 4.2.2 Implementation. 🔨

As indicated above, CDT was the primary tool used to test the project regularly.

Here's how this looked like:

- Chrome browser was used as the primary tool.
- On one tab, Gitpod open with the project.
- On a second tab, the preview of the project, using the "python3" method inside Gitpod.
- On that second tab, CDT open to visualise and test styles, behaviour and use the console.

Once the project was deployed via Heroku, the project was tested with the mobile devices mentioned above.

#### 4.2.3 Results. 📊

Since the testing was ongoing, the results of it were many during that period. Most of the issues were related to code not doing what the developer wanted:

- **CSS rules not working**: CDT used to review the reasons, detect the root of the problem and apply the fix back to the CSS rules.
- **JS code not working**: Console used to review the potential reasons. Once possible solutions were detected, they were tested with the code and eventually fix the problem.
- **Python code not working**: Checking back and forth the code and its logic to detect the root of the problem and apply the necessary fixes to accomplish expected outcomes.

#### 4.2.4 Outcomes. 🚀

The eventual outcome of each testing was detecting issues, evaluating the reasons and finding the solutions.

Once the root of each issue is detected, then the applied solution is coded into the corresponding code, whether that's the HTML, CSS, JS or Python.

**With each error detected and fixed, the developer's knowledge increased.**

### 4.3 Testing User Stories 🙆‍♀️

Going over the user stories indicated in the UX section to ensure that they work as intended.

1. Keep track of their entrepreneurship reading.

   1. If they are not yet registered, visit the registration page through the top menu option titled "Register".
   2. If they are registered, login into their account through the top menu option titled "Log In".
   3. They have two ways of checking their listed book. One way is through the home page (menu option titled "Home"), where their books will be the only ones with the options to be edited and mark as read. The second way is through their profile (menu option titled "Profile"), where they will only have a list of their books.
   4. They can add new books to their to-read list through the top menu option titled "New Book".
   5. They can edit their books by clicking the "Edit" button next to each of them.
   6. They can mark their book as read by clicking the "Read" button next to each of them, which will remove that book from their list.
   7. Try to accomplish the steps both on desktop and mobile views.

2. Learn about what others entrepreneurs are reading.

   1. They don't need to register to learn about what other entrepreneurs are reading. It's not a requirement.
   2. They can go to the home page through the top menu option titled "Home" or by simply visiting the app.
   3. They will be able to scroll through all the books listed in the app. By clicking on them, the collapsible element will open, presenting them with the book's category, author and which entrepreneur added it.
   4. All book's collapsible elements have a main header which contains the book's title and the 'read by date' set by the entrepreneur.
   5. Try to accomplish the steps both on desktop and mobile views.

3. Get in touch with the developer behind the project.

   1. They don't need to register to get in touch with the developer behind the project. It's not a requirement.
   2. They can go to the footer scrolling to the bottom of any of the app's pages.
   3. Under the "Links" title they will see the option to contact the developer at "@ Get in Touch!".
   4. They can click on it, which will trigger the creation of a new email addressed to the developer.
   5. Try to accomplish the steps both on desktop and mobile views.

#### 4.3.1 Testing "Hacking" User Stories 👨🏼‍💻

1. Protecting admin sections from users forcing themselves into admin sections.

   1. A reader may try to force themselves into the "Manage Categories" section for admins by placing "/get_categories" at the end of the app's URL.
   2. A reader may try to force themselves into the "Edit Category" page for admins by placing "/edit_category/<category_id>" at the end of the app's URL.
   3. In both instances, the app will validate that it's the admin accessing it. Otherwise, it will show an error message stating "No Admin Logged In".

### 4.4 Bugs & Problems 🐛

There were no brand-new or relevant bugs/problems during the development of this project.

The usual suspects were always there because of my lack of experience and mistyping the code.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<span id="deployment"></span>

## 5. Deployment 🚀

Carlos developed this project using Gitpod’s IDE. He pushed all developments to the corresponding repository inside his GitHub account.

He followed the steps below:

1. He first created the repository inside his GitHub account. <a href="https://github.com/betahope/Entrepreneur-Bookshelf" rel="noopener" target="_blank">Repo URL</a>.
2. He launched the project on Gitpod from the repository, using Gitpod's Chrome extension.
3. He continued his work and development on Gitpod.
4. He pushed all relevant and significant changes to the repository, from Gitpod, regularly.
5. He deployed the project using <a href="https://devcenter.heroku.com/categories/deployment" rel="noopener" target="_blank">Heroku</a>.

**Note:** It's important to create your env.py file where you store your sensitive information, making sure .gitignore has it.

There are no differences between the deployed and the developed version. Carlos used one branch: master.

You can run and view the project by following this URL: <a href="https://flask-book-manager-project.herokuapp.com/" rel="noopener" target="_blank">View Project</a>.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<span id="credits"></span>

## 6. Credits 👉

### 6.1 Code Snippets 🧬

- Knowledge for usage of Materialize CSS: <a href="https://materializecss.com/" rel="noopener" target="_blank">Materialize CSS</a>.
- Inspiration and initial base code for the app: <a href="https://github.com/Code-Institute-Solutions/TaskManagerAuth" rel="noopener" target="_blank">Code Institute To-Do List Mini-Project</a>

### 6.2 Media 📸

- Entrepreneur's Bookshelf icon: <a href="https://www.iconfinder.com/icons/1055107/bookshelf_books_library_icon" rel="noopener" target="_blank">IconFinder</a>.
- Font Awesome icons: <a href="https://fontawesome.com/" rel="noopener" target="_blank">Font Awesome</a>.
- Poppins, Google Font: <a href="https://fonts.google.com/specimen/Poppins" rel="noopener" target="_blank">Poppins</a>.

### 6.3 Acknowledgements 🙏

- **Jonathan Munz _(My CI Mentor)_**: Thanks for your support as a mentor. You have provided excellent guidance, feedback and inputs into my ideas and development. I am looking forward to working together again in the next milestone.
- **CI Slack Community**: Through several conversations and calls, I continuously improve my knowledge as an engineer, and I grow as a person.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_
