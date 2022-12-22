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

- At the very bottom, there is a footer with social network links;

### The Footer
 <img src ="">

- The footer section includes links to Carmen's social media sites;
- The links will open to a new tab to allow easy navigation for the user;
- The footer is helpful to the user as it encourages them to keep connected via social media;
- This section appears on all pages.

### Yoga Benefits Section
 <img src ="">

- This section explains to the user the additional values yoga can bring to their life;

### About Page
<img src="">
The page describes the benefits of yoga;
It gives an insight into what moved Carmen to this discipline and how yoga affects her life.


### Input Section
<img src="readme-images/input.png">

- This section requests the user to enter the expense value to be registered or the budget's value to be set.
- If the input choice is not a positive number, the program displays a customized message error.


### Feedback Section
<img src="readme-images/feedback.png">

- In this section, the program sends feedback to the user explaining how it handles the input data by printing the worksheet updated, the month, and the new value. Updating a value also triggers an update of monthly and yearly totals; messages of the main steps of the operations are displayed here too.

### Budget Section
<img src="readme-images/budget.png">

- This section shows messages about the comparison between
monthly and yearly expenses and their respective budgets.
- If the comparison is not possible, another sentence explains the reason on the terminal.
- This section is displayed if:
  - The first choice is to update an expense;
  - The first choice is to set a monthly budget.

### Restart/Leave Section
<img src="readme-images/restart.png">

- In this section, the program requests the user to choose between exiting the app or restarting the program.
- If the input choice is: a letter but not y or n, not a letter at all, or more than one letter, the program displays a customized message error.


### Expense Type Section
<img src="readme-images/expense-type.png">

- In this section, the program requests to enter a number to choose the expense type.
- This section is displayed if:
  - The first choice is to set a monthly budget;
  - The first choice is to view a total and the choice of Total Type Section is 2.
- If the input choice is not in the number range or not a number at all, the program displays a customized message error.


### View Total Section
<img src="readme-images/total.png">

- In this section, the program requests to choose which total to display: the total of expenses by month or the total of a specific expense type by year.
- If the input choice is not in the number range or not a number at all, the program displays a customized message error.

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