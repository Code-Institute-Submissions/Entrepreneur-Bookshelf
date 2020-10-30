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

# Entrepreneur's Bookshelf

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

- A "Contact Me" link which readers can use to get in touch with the developer. The link points to the developer's email address.

### 1.4 App Wireframes (TO DO) 💻📱

Below you will find the app's wireframes. These were generated using Balsamiq. There are two versions of the wireframes. Choose your option:

- Wireframes for the <a href="https://drive.google.com/file/d/1bCmX4HrQt4wVbTsTArFjPO-Wf3a5Vp_f/view?usp=sharing" rel="noopener" target="_blank">desktop & mobile version in PDF</a>.
- Wireframes for the <a href="https://drive.google.com/file/d/1sfSxslhGBw88hK4E2KWCFZT2NFAwRp1U/view?usp=sharing" rel="noopener" target="_blank">desktop & mobile version in Balsamiq</a>.

### 1.5 Design Decisions 🎨 🖌

First and foremost, the essential elements that had to be in place were:

- **Responsiveness**: The app has to be fully responsive and adapt to different screen sizes.
- **Interactivity**: The site has to provide users with interactivity and with more than just one type to demonstrate different managements of JS and CRUD development.
- **Simplicity**: The app has to be simple, easy to navigate, read and interact.

This project was developed to be presented as Milestone 3 for CI's Full Stack Software Development course. MS3 requires the explicit use of Python, Flask, MongoDB and CRUD development to provide site visitors with interactivity and data management, so the decision was made to focus on a simple overall app, but with clear, interactive elements and management levels in it.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<span id="features"></span>

## 2. Features (TO DO) ⚙

- **Navigation bar:** It allows users to easily access all the sections of the webpage and content on the King Metric's app, at all times. It also provides a direct button taking them to the "Convert" section.
- **Home section:** It welcomes users with a quick pitch about King Metric and those still using the Imperial System. It also provides a big button taking users to the "Convert" section.
- **Footer:** It allows users to easily access all the sections of the webpage and content on the King Metric's app, at all times. It also provides a direct button taking them to the "Convert" section. Additionally, it provides users with direct links to the app where the content was taken from for the "Origins" and "The Others" section.
- **Origins section:** It allows users to learn a bit about the history of the Metric System and where it came.
- **The Others section:** It enables users to learn a bit about who is still officially using the Imperial System.
- **Convert section:** It enables users to convert Imperial units to the Metric System. It provides conversion for units in Length, Area, Volume and Weight. It also provides a reset button, to clear the converter for new calculations if necessary.
- **Contact section:** It allows users to get in touch with the developer through a simple and fully functional contact form.

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
  - The project used the **MongoDB** database service to store the readers, books and categories.
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

### 4.3 Testing User Stories (TO DO) 🙆‍♀️

Going over the user stories indicated in the UX section to ensure that they work as intended.

1. Learn a bit more about the history of the Metric System.

   1. Go to the "Origins" section through the top menu or by scrolling down the page.
   2. Scroll down through the page to read the piece of history about the origins of the Metric System.
   3. Learn with it that the French invented it between 1790 and 1800.
   4. Learn with it that this was done during the French Revolution.
   5. Try to accomplish the steps both on desktop and mobile views.

2. Learn who is still officially using the Imperial System.

   1. Go to the "The Others" section through the top menu or by scrolling down the page.
   2. Scroll down through the page to read the piece of information about the countries that are still officially using the Imperial System.
   3. Interact with Google Maps, which highlights the three countries.
   4. Learn with it that the USA, Myanmar and Liberia are the only countries still officially using the Imperial System.
   5. Learn with it that the UK is not on that list. 😉 😉
   6. Try to accomplish the steps both on desktop and mobile views.

3. Convert Imperial measurements to the Metric System.

   1. Go to the "Convert" section through the menu or footer button. The "Home" section also provides one additional button with the main content.
   2. Change the property and check if the rest of the converter reacts to it (the unit selector must change).
   3. Change the unit and check if the rest of the converter reacts to it.
   4. Input a value in the input field and check if the converter reacts to it. (here is when the converter runs the conversion).
   5. Maintain the inputted value and change the property and unit selectors and check if the converter reacts to it, and recalculates.
   6. Change the inputted value and check if the converter reacts to it by recalculating.
   7. Click on the "Reset Converter" button and check if the converter resets to its original values.
   8. Try to accomplish the steps both on desktop and mobile views.

4. Get in touch with the developer behind the project.

   1. Go to the "Contact" section through the menu or footer options.
   2. Try to submit an empty contact form and check that an error message about the required fields appears.
   3. Try to submit the contact form with an invalid email address and check that the error message appears.
   4. Try to submit the contact form with all inputs valid and check that the information is processed and a confirmation message is presented.
   5. Try to submit the contact form with all inputs valid and verify that a confirmation message is presented immediately after.
   6. Try to acknowledge the confirmation message and check that the contact form is cleared.
   7. Try to submit the contact form with all inputs valid and verify that an email is sent with a confirmation of the message sent.
   8. Try to accomplish the steps both on desktop and mobile views.

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
5. He deployed the project using <a href="https://www.heroku.com/" rel="noopener" target="_blank">Heroku</a>.

There are no differences between the deployed and the developed version. Carlos used one branch: master.

You can run and view the project by following this URL: <a href="https://betahope.github.io/king-metric/" rel="noopener" target="_blank">View Project</a>.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<span id="credits"></span>

## 6. Credits 👉

### 6.1 Code Snippets (TO DO) 🧬

- Knowledge for usage of Google Maps API: <a href="https://developers.google.com/maps/documentation/javascript/tutorial?hl=es" rel="noopener" target="_blank">Google Documentation</a>.
- Inspiration for coding improvement on the Google Maps API: <a href="https://www.youtube.com/watch?v=Zxf1mnP5zcw" rel="noopener" target="_blank">Traversy Media</a>.
- Inspiration for the converter: <a href="https://www.w3schools.com/howto/howto_js_length_converter.asp" rel="noopener" target="_blank">W3Schools</a>.
- Inspiration for the contact form: <a href="https://github.com/betahope/resume-project" rel="noopener" target="_blank">Resume Project (Part of CI curriculum)</a>.
- Inspiration for the fraction number in Hero section: <a href="https://stackoverflow.com/questions/7525977/how-to-write-fraction-value-using-html" rel="noopener" target="_blank">Stack Overflow</a>.

### 6.2 Media 📸

- Background image in Hero section: <a href="https://www.pexels.com/photo/white-10-feet-steel-tape-162500/" rel="noopener" target="_blank">Pexels</a>.
- King Metric logo: <a href="https://drive.google.com/file/d/11uMF7-ZxtWjsPS5vrtC6LwDzR1vIIWox/view?usp=sharing" rel="noopener" target="_blank">Created with Keynote</a>.
- Content for "Origins" section: <a href="https://en.wikipedia.org/wiki/Introduction_to_the_metric_system" rel="noopener" target="_blank">Wikipedia</a>.
- Content for "The Others" section: <a href="https://www.worldatlas.com/articles/which-countries-use-the-imperial-system.html" rel="noopener" target="_blank">WorldAtlas</a>.
- Font Awesome icons: <a href="https://fontawesome.com/" rel="noopener" target="_blank">Font Awesome</a>.
- Flags for Google Maps: <a href="https://www.iconfinder.com/iconsets/flags_gosquared" rel="noopener" target="_blank">IconFinder</a>.
- Image with people measuring (France): <a href="https://en.wikipedia.org/wiki/Introduction_to_the_metric_system" rel="noopener" target="_blank">Wikipedia</a>.
- Lato, Google Font: <a href="https://fonts.google.com/specimen/Lato?query=lato" rel="noopener" target="_blank">Lato</a>.

### 6.3 Acknowledgements 🙏

- **Jonathan Munz _(My CI Mentor)_**: Thanks for your support as a mentor. You have provided excellent guidance, feedback and inputs into my ideas and development. Looking forward to working together again on the next milestones.
- **CI Slack Community**: Through several conversations and calls, I continuously improve my knowledge as an engineer, and I grow as a person.

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_
