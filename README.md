# Yoga with Carmen
[View the live project here]()

Yoga with Carmen is a website built for the yoga teacher Carmen Ferraro. The website allows Carmen to showcase her work, publish classes, set maximum available spaces, and display them on a calendar. Users can sign up, view, comment, and like posts, book classes, and comment on their reservations. The purpose of the website is mainly informative. It provides an exhaustive description of the disciplines practiced, allowing users who want to start a yoga journey to have a better understanding of the courses.
Yoga with Carmen targets people interested in yoga and would like to start or keep practicing it; it also targets people with physical pain problems due to bad posture and helps them resolve them through exercise.

## FEATURES:
### Navbar
- The fully responsive navigation bar appears on all pages;
- It includes links to the Logo, Home page, About, Classes, Blog, Sign-in, and Sign Up page and is identical on each page to allow for easy navigation.
- When the user is logged in, the navbar also displays a link to Book and Reservations, which are restricted areas;
- This section will allow the user to easily navigate from page to page across all devices without reverting to the previous page via the ‘back’ button.

### Callout Section
 <img src ="">

- It displays a message that encourages the user to sign up;
- It includes a link to the Sign Up page to facilitate the process.


### Introduction Section
 <img src ="">

- The introduction section will allow the user to have a quick overview of the purpose of the site and the yoga types practiced;
- In this section, the user will see the benefits of this practice. This should motivate the user to participate in the classes.

### Today's Classes Section
 <img src ="">

- This section  is displayed when there is/are a class/es on the current day;
- It shows the class details so that the user can make a booking or have a reminder;
- When there are no classes on the current day, the section doesn't show.

### Quotes Section
 <img src ="">

- This section provides the  user feedback about the course;
- It motivates the user to subscribe and participate in the classes.

### Footer
 <img src ="">

- The footer section includes links to Carmen's social media sites;
- The links will open to a new tab to allow easy navigation for the user;
- The footer is helpful to the user as it encourages them to keep connected via social media;
- This section appears on all pages.

### Yoga Benefits Section
 <img src ="">

- This section explains to the user the additional values yoga can bring to their life.

### My Passion For Yoga Section
<img src ="">

- Describes Carmen's first steps into yoga discipline and the journey that brought her to become a yoga teacher;
- The experience presented in the section gives the user the feel of a human connection since he can now relate to Carmen as a real person.

### Yoga Class Section
<img src ="">

- This section has an image to allow the user to have a visual acknowledgment of the exercises practiced in the class;
- This section has a button that opens a modal whit the full description of what the class involves to allow the user to understand which yoga type suits them best;
- The modal contains a button that redirects the user to the booking page;
- If the user is not signed in, the button in the modal doesn't display.

### Post Section
<img src="">

- This section has an image to allow the user to have a visual acknowledgment of what the post is about;
- It has a title that links to the specific page of the post;
- Under the title is displayed the date when the post was published and the number of likes.

### Post Page Title Section
<img src="">

- This section displays the title of the post on which the user previously clicked;
- Under the title, it displays the username of the publisher and the date when the post was published.

### Post Page Content Sction
<img src="">

- This section displays the content of the post that the user chose.

### Like Section
<img src="">

- This section displays the number of likes that the relevant post received;
- If signed in, the user can click on the heart icon to leave a like and click again to remove it;
- This section adds interactivity to the website and allows to leave effortless feedback to show appreciation;
- If not signed in, the user can only view the likes, and clicking on the icon won't have any effect.

### Messages Section
<img src="">

- This section displays the number of comments that the relevant post received.

### Comments Section
<img src="">

- This section displays the approved comments written by the admin and users, along with the username and date related to them;
- The comments are ordered by date, with the most recent at the top;
- This section allows the user easily follow the conversation.

### Comments Form Section
<img src="">

- This section displays a form that allows the user to leave feedback;
- Through this section, the user can interact with other users;
- Once the comment is submitted, the user receives feedback about the successful submission and the approval status.


### Booking Form Section
<img src="">

- This section displays a form to make a reservation for a class;
- The dropdown menu displays the classes present on the calendar, and the user can choose from them;
- Once the form is submitted, the user receives feedback on whether the booking has been successful or not, and in that case, it explains the reason for the failure.

### Calendar Section
<img src="">

- This section displays a table with the time slots and the days of the current and next week;
- The days row updates automatically so that the current week is always close-up;
- Every time a class is published is displayed on the calendar in the relevant cell;
- This disposition facilitates the view of the classes for a better time planning for the user.

### Reservations Section
<img src="">

- This section displays the classes booked by the logged-in user and the relative details;
- If the user leaves a note about a class, it displays under the relevant reservation;
- Every reservation has a delete button that, when clicked, calls a modal to receive confirmation of deletion;
- This section is a reminder for the user of the booked classes.

### Notes Section
<img src="">

- This section displays notes written by the user;
- Every note is under the reservation it refers to;
- This section is private, so only the logged-in user can access it;
- Next to each note, there is an edit button that links to an edit note page;
- Next to the edit button, there is a delete button that, when clicked, calls a modal to confirm the deletion.

### Add Notes Section
<img src="">

- This section displays a form that allows the user to add a note to a reservation;
- The user can choose the reservation to comment on from a dropdown menu.

### Edit Notes Section
<img src="">

- This section displays a form that allows the user to edit a note;
- The updated note takes the place of the previous one under the relevant reservation.

### Login Section
<img src=""> 

- This section allows the user to create a private account through which they can book classes, write notes, like and comment on posts; 
- The section displays a paragraph for users that already have an account, inviting them to click on the sign-in button to redirect them to the sign-in form;
- The section has a form requesting the user's information to create an account;
If the form is not filled correctly, it displays error  messages relative to the issue;
- Once the form is filled up correctly, the submission redirects the user to the home page and shows a success message.

### Sign In Section
<img src="">



### Logout Section
<img src="">

- The section requests the user a logout confirmation;
- Once logged out, the user is redirected to the home page and won't be able to access the restricted areas;
- After the logout, a feedback message displays to acknowledge the user about the outcome of the action.




## Data Model:
<img src="readme-images/chart.png">

## Testing:

<table>
<thead>
<tr>
<th>Action or Event</th>
<th>Expected Result</th>
<th>Successful?<th>
</tr>
</thead>
<tbody>
<tr>
<td>Run the program</td>
<td>Show welcome message and request of operation to execute</td>
<td>Yes</td>
</tr>
<tr>
<td>Type a number, not in the options range or a non-number</td>
<td>- Error message appears without stopping the program<br>
- Request again a valid input</td>
<td>Yes</td>
</tr>
<tr>
<td>To update a worksheet: type a number between 1 and 7</td>
<td>Access to month options</td>
<td>Yes</td>
</tr>
<tr>
<td>Type a number between 1 and 12</td>
<td>Request the value of the expense</td>
<td>Yes</td>
</tr>
<tr>
<td>Type a number less than 0 or a non-number</td>
<td>- Error message appears without stopping the program<br>
- Request again a valid input</td>
<td>Yes</td>
</tr>
<tr>
<td>Enter valid data</td>
<td>- Update the relevant worksheet and inform the user;<br>
    - If the entry is of a monthly bill, only one value per month will be allowed;<br>
    - If the entry is for car or food expenses, it's possible to add more values for the same month;<br>
    - Update the monthly total of the selected expense in the total worksheet and inform the user;<br>
    - Update Year Total in the total worksheet and inform the user;<br>
    - Access the monthly budget for the selected expense and compare it to the respective total by sending a message to the user;<br>
    - State the difference between monthly budget and total;<br>
    - If the value for the monthly budget is not present, inform the user;<br>
    - Access the yearly budget for the selected expense and compare it to the respective total by sending a message to the user;<br>
    - If the value for the yearly budget is not present, try to calculate it.<br>If calculation is not possible due to missing information, inform the user
    - State the difference between yearly budget and total;<br>
    - Request to exit the game or continue with a new operation.
</td>
<td>Yes</td>
</tr>
<tr>
<td>Type "y"</td>
<td>Restart the program</td>
<td>Yes</td>
</tr>
<tr>
<td>Type "n"</td>
<td>Exit the program</td>
<td>Yes</td>
</tr>
<td>Type anything else</td>
<td>- Error message appears without stopping the program<br>
- Request again a valid input</td>
<td>Yes</td>
</tr>
<tr>
<td>To set a monthly budget: type 8</td>
<td>Access to expense type options</td>
<td>Yes</td>
</tr>
<tr>
<td>Type a number not in the options range or a non-number</td>
<td>- Error message appears without stopping the program<br>
- Request again a valid input</td>
<td>Yes</td>
</tr>
<tr>
<td>Enter valid number</td>
<td>Access to month options</td>
<td>Yes</td>
</tr>
<tr>
<td>Enter valid number</td>
<td>Request relevant budget input</td>
<td>Yes</td>
</tr>
<tr>
<td>Enter budget data</td>
<td>- Update budget worksheet and inform the user;<br>
    - Access the monthly total for the selected expense and compare it to the respective budget by sending a message to the user;<br>
    - State the difference between monthly budget and total;<br>
    - Access the yearly budget for the selected expense and compare it to the respective total by sending a message to the user;<br>
    - If the value for the yearly budget is not present, try to calculate it.<br>- If calculation is not possible due to missing information, inform the user;<br>
    - State the difference between yearly budget and total;<br>
    - Request to exit the game or continue with a new operation.</td>
<td>Yes</td>
</tr>
<tr>
<td>To view totals: type 9</td>
<td>Access to total type options: by month or by expense type</td>
<td>Yes</td>
</tr>
<tr>
<td>Type 1</td>
<td>Access to month option</td>
<td>Yes</td>
</tr>
<tr>
<td>Select month number</td>
<td>- Print a message with the total of the expenses for the relevant month;<br>- Request to exit the game or continue with a new operation.</td>
<td>Yes</td>
</tr>
<tr>
<td>Type 2</td>
<td>Access to expense type options</td>
<td>Yes</td>
</tr>
<tr>
<td>Type expense type number</td>
<td>- Print a message with the yearly total of the selected expense type;<br>- Request to exit the game or continue with a new operation.</td>
<td>Yes</td>
</tr>
<tr>
</tbody>
</table>

### Validator Testing:
- PEP8 
No errors were returned when passing through the official [PEP8 validator]();

## Bugs:
The initial idea was to create a worksheet for every expense.
When looping through the values of numerous worksheets, the program would have raised a 429 "Too many requests" error.
Reducing the number of worksheets fixed the problem.

When calculating the monthly bill totals, if there was an empty cell in the column, the program would have raised an int() error since " " can't be converted into an integer. 
Adding a ternary operator in the function to convert all column values into integers fixed the problem.

## Deployment:
- In GitHub, create a list of requirements in requirements.txt by using this command in the terminal: **pip3 freeze > requirements.txt**;
- Commit and push these changes;
- Create an account on [Heroku](https://www.heroku.com/):
  - On the homepage, click sign-up and fill out the form;
  - Click **Create free account**;
  - Click the link provided in the confirmation email sent by Heroku;
  - Set a password and login;
  - Proceed and accept the terms of service;
- Click the **Create new app** button;
- Name your app by typing the chosen name under **App name**;
- Select your region and click the **Create app** button;
- On the menu bar, click on **Settings**;
- In the **Config Vars** section, click on **Reveal Config Vars**;
- In the field for **KEY** enter **CREDS**;
- Go back to the workspace, open creds.json, and copy the content;
- In the field for **VALUE** paste the creds.json file, and click **Add**;
- Add another Config Var underneath by entering **PORT** in the **KEY** field, **8000** in the VALUE field, and clicking the **Add** button;
- Scroll down to the **Buildpacks** section and click on **Add buildpack**;
- Select **Python** and click **Save changes**;
- Click on **Add buildpack** again, select **Node.js** and click **Save changes**;
- Scroll up to the main menu bar and click on **Deploy**;
- In the **Deployment method** section, select **GitHub**;
- Click **Connect to GitHub**;
- Enter the name of your repository in the search bar and click **Search**;
- Once your repository it's shown underneath, click on **Connect**;
- Scroll down to the **Manual deploy** section;
- Click on **Deploy branch** making sure the branch to deploy is **master**;
- Wait until you see the message **Your app was successfully deployed**;
- Click on **View** to make sure your mock terminal is up and running.

## Credit:
- Code Institute's Love sandwiches walkthrough project: it helped to connect API, build the basic structure of my project and deploy it;
- [Ternary operator tutorial](https://www.tutorialspoint.com/ternary-operator-in-python): helped to solve the previously mentioned bug;
- [Grammarly](https://app.grammarly.com/): helped to correct grammar errors.

### Media:
[Lucidchart](https://www.lucidchart.com): used for the diagram in README.md

## Libraries:
[Gspread](://docs.gspread.org)
[Google auth](https://pypi.org/project/google-auth/)