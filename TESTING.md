# Testing

[Back to README.md file](README.md)

## Table of Contents
1. [Testing User Stories](#testing-user-stories)
2. [DevTools](#dev-tools)
    * [Responsiveness](#responsiveness)
    * [Console Debugging](#console-debugging)

3. [Manual Testing](#manual-testing)

4. [Automated Testing](#automated-testing)
    * [Code Validation](#code-validation)
    * [Browser Validation](#browser-validation)
    
5. [User Testing](#user-testing)
    * [Mentor Review](#mentor-review)
    * [User Review](#user-review)

## Testing user Stories

## DevTools

## Manual Testing

I manually tested each page and feature on the website. By going through ass of these processes, I was able to finely comb throug the entire site and pick up on an problems.

### Sitewide Features
- The navbar remains fixed on all pages to allow for users to navigate around the site easily regardless of their scroll position. All nav links render the appropriate page without errors.
- The brand logo returns the user to the home page from all pages.
- On medium screen sizes and below, the navbar collapses into a mobile navbar element, triggerable by clicking on the burger icon. Each link within this mobile nav renders the correct template.
- The footer contains the brand logo and a copyright claim. The social links appear to the right-hand side of the footer and all open in a new window to display the appropriate personal finance account on Twitter, Instagram and YouTube.
- A favicon is correctly displayed in the browser tab of every page.

### Home (all users)

- The Homepage renders for all users who have not logged in correctly on all screen sizes. The searchbar allows users to input text and pressing both the return key or the button to the right-hand side submits the query to the database. The query returns any results which matches the user's input, including slices of words, for example 'pysch' for psychology. Results display on the All Books page (see [All books](#all-books)).

- To the right-hand side of the searchbar are two call to actions: one for login (see [Login](#login)) and one for signup (see [signup](#signup)). Clicking these buttons takes the user to each page respectively. Hovering over each button causes the background colour to lighten slightly, prompting the user to click.

<img width="1461" alt="home-logged-out" src="https://user-images.githubusercontent.com/68863341/111531663-bf3b2f00-875c-11eb-8ace-c8a251f5c9e8.png">


- The 'Top Picks' section contains the suitable amount of book covers for the screen size and each links to the appropriate individual book page on click. The 'All Books' button just below takes the user to the All Books page (see [All books](#all-books)).

### Home (logged in user)
- For the logged in user, the home page displays the same as for those who are not logged in, with the exception of the call to action buttons for login and signup. This is because they are no longer relevant for a user who has already acted upon these call to actions. With the new available space, the searchbar becomes centered in the middle of the page.

<img width="1454" alt="home-logged-in" src="https://user-images.githubusercontent.com/68863341/111531679-c6623d00-875c-11eb-9e07-94981ec52d10.png">

### All Books
- The All Books page displays the same for those logged in and not logged in. The searchbar at the top of the page allows user to input text and search the database for matching results by using either the button to the right-hand side or the return key. If results are found, a message below is rendered telling the user "Showing results for '[user input]'." Below this a 'Show All Books' button appears which correctly renders the originally All Books page with all books displayed when clicked. 

<img width="1410" alt="search-results" src="https://user-images.githubusercontent.com/68863341/111531764-e0038480-875c-11eb-9c95-9010bc743c9b.png">

- If there are no results matching the user's search input, an alternative message stating "Sorry, no results for '[user input]' is displayed. The 'Show All Books' button displays in this case also.

<img width="1424" alt="search-no-results" src="https://user-images.githubusercontent.com/68863341/111531791-e8f45600-875c-11eb-9c7f-b64c11e992f9.png">

- To the right-hand side fo the searchbar is a yellow button with a + icon. For a user who is logged in, on hover a Materialize tooltip displays to indicate they can add a book recommendation. It returns the Add Book page when clicked (see [Add Book](#add-book)). For the user who is not logged in, on hover a Materialize tooltip is displayed advising them to log in if they wish to add a book recommendation. When clicked it renders the Login page (see [Login](#login)).
- The main body of the page displays all books from the database, contained within Materialize cards of equal size. There is up to four books per row displayed on larger and as little as one per row on mobile. Each card contains a book image, title, author-year, category and user who it was added by. If no image_url is associated with the book, the placeholder image in the website style is displayed in its place.

<img width="1454" alt="placeholder-book-image-example" src="https://user-images.githubusercontent.com/68863341/111534006-64570700-875f-11eb-9d72-f4f3d9c3f25e.png">

- Click on the book title, image or ellipsis icon renders a page with only the selected book on it and further information.

### Display Individual Book (all users)


### Display Individual Book (logged in user)
- The Display Book page renders a template with all of the information associated with a particular book on its own page. This is achieved by using the unique book _ _id_ in the URL. The book title, author, category, full description and user who it was added by are all displayed correctly. 

<img width="1452" alt="display-book-id-url" src="https://user-images.githubusercontent.com/68863341/111532026-2b1d9780-875d-11eb-8e64-5b7f4eeda31c.png">

- In the top left-hand corner, a button which allows the user to go 'Back To All Books' is displayed.
- Below the book description are a number of user buttons and links. The 'Buy Now' button opens a new window and returns the UK Amazon page for the book. If no link is associated with the book then the button appears as disabled.

<img width="1454" alt="not-available" src="https://user-images.githubusercontent.com/68863341/111532330-7172f680-875d-11eb-9533-48e61cbd61c2.png">

- The button with the outline of a bookmark icon allows the user to save the particluar book to their reading list. On click, the flash message 'Bookmarked' appears at the top of the page.

<img width="1458" alt="bookmarked" src="https://user-images.githubusercontent.com/68863341/111532562-b139de00-875d-11eb-80e2-98db1f19a0f2.png">

-The action can be confirmed by navigating to the profile page (see [Profile](#profile)) where the book will now display in one of the collapsibles in the 'My Reading List' section.

<img width="1456" alt="bookmarked-confirm" src="https://user-images.githubusercontent.com/68863341/111532708-dfb7b900-875d-11eb-969a-0d03b75ea3d7.png">

- For users who have added the book which is being displayed to the database themselves (i.e. it is their recommendation), two controls also appear next to the Buy Now and bookmark buttons: 'Edit' and 'Delete'. They are distinguished from the generic buttons by their yellow background colour. Clicking on the 'Edit' button renders the 'Edit Book' page (see [Edit Book](#edit-book)) and clicking on the 'Delete Button' renders triggers a warning which requires the user to confirm they wish to delete the book. 

<img width="1452" alt="confirm-book-delete" src="https://user-images.githubusercontent.com/68863341/111532880-1261b180-875e-11eb-9733-08613350a8a8.png">

- If they confirm using the 'OK' button, the book is removed from the database and the user is returned to the My Profile page and a flash message saying 'Book Deleted' appears at the top of the screen.

### Login
- The Login in page renders a form with the following input fields: username and password. Each field flashes red if left empty, which is the expected response of the Materialize 'validate' feature. If a user enters details which match the username and password of a user in the database's 'users' collection, the user is redirected to their profile page and all navbar links appear. If the details do not match, a flash message at the top of the screen states 'Incorrect Username and/or Password' and resets the form.
- The flashing add user button in the top right-hand corner displays a Materialize tooltip 'New Here?' when a user hovers over it. Clicking the button renders the signup page template (see [Signup](#signup)).
- If all details match a user in the database, the user is redirected to their profile (see [Profile](#profile)).

### Signup
- The Signup page renders a form with the following input fields: username, password and email. All are make as invalid with a red line if they do not conform to the requirements. Usernames must be a minumum of 5 characters and only numbers and letters. Password must be a minimum of 6 characters and only numbers and letters. Email addresses must contain an @ symbol. If a user tries to submit a form with inputs that do not match this format, a message appears next to the problematic field.
- If a user enters a username that already exists in the database, a flash message appears stating 'Username already exists' and resets the form.
- If a user submits the form and all fields are valid, the user is redirected to the My Profile page and a flash message 'Registration Successful!' appears at the top of the page.
- The flashing existing user button in the top right-hand corner displays the tooltip 'Have An Account?' when a user hovers over it. Clicking the button takes the user to the login page (see [Login](#login)).

### Add Book
- The Add Book page is only visible to logged in users. It can be accessed from the navbar, the user's profile and the All Books page. 
- The page displays a form with 7 fields, 5 of which are required. These 5 fields are: title, author, category, year and description.
- The category field allows the user to select one option from a dropdown. 
- The year field always keyboard input or the use of up and down arrows to navigate to a particular year. The range is restricted to between 1980 and 2021.
- The description is a textarea field and limited to 200 characters for optimum display purposes.
- The two optional fields - Image URL and Purchase Link require the prefix https:// to ensure a valid URL is entered. If not, the Materialize input field indicates the error with a red invalid line.
- The cancel button discards the form and returns the user to the page they were last on. Thus, navigating to the Add Book page via the navbar returns the user back to the homepage, via their profile back to their profile, and via All Books back to All Books.

### Profile
- The profile page displays the current logged in user's username as the main heading of the page. In the top right-hand corner is a floating action button containing user settings which, when hovered over, drops down two further user settings. These two buttons take the user to the Delete User (see #delete-user) and Edit User (see #edit-user) pages respectively.
- For a user who has not yet bookmarked any books to their reading list and/or not added any book recommendations to the website, a yellow + button appears in these section in the place of content. Clicking the button in the 'My Reading List' section takes the user to the All Books page (see #all-books) and clicking the button in the 'My Recommendations' section takes the user to the Add Book page (see #add-book).

<img width="1109" alt="empty-user-profile" src="https://user-images.githubusercontent.com/68863341/111533076-4b9a2180-875e-11eb-8b2b-bff4f8540c3d.png">

- If a user has bookmarked a book, The title and author of the book appear in a collapsible head element and further information associated with it appears in the collapsing body element.

<img width="1281" alt="reading-list" src="https://user-images.githubusercontent.com/68863341/111533294-8603be80-875e-11eb-8bec-343b0292cf2a.png">

- The collapsing element is toggle up and down on click. The book can be removed from the reading list by clicking the bookmark button on the right-hand side of the element and an unbookmarked flash message displays.

<img width="1282" alt="unbookmarked" src="https://user-images.githubusercontent.com/68863341/111533203-6cfb0d80-875e-11eb-97ef-2fd34c8598d1.png">

- If a user has added recommendations to the site, they appear in the same style as the reading list in the 'My Recommendations' section below it. The buttons on the right-hand side allow the user to both edit and delete the book.

<img width="1281" alt="my-recommendations" src="https://user-images.githubusercontent.com/68863341/111533262-7dab8380-875e-11eb-9550-a2ba51f684bf.png">

- Each 'Buy Now' link in the collapsing element of the book display opens a new window and takes the user to the external site where they can purchase the book.

### Edit Book
- The Edit Book page can be navigated to by the indivudual book's display page or from a user's profile. A book can only be edited by a user if they added the book to the site via the Add Book page (see #add-book).
- All the fields present on the Add book page funtion in the exact same way as on the Add Book page (see [Add Book](#add-book)).
- All fields are already populated with the current values associated with the book. This way, the userr can change just the year, for example, and do not have to reenter all other fields.

<img width="1185" alt="edit-book" src="https://user-images.githubusercontent.com/68863341/111533357-97e56180-875e-11eb-9a3f-6194c49d0f8e.png">

- Pressing the 'Cancel' button returns the user to their profile page or the individual book page depending on which they accessed the edit button from.
- Pressing the Edit button successful updates the values for the book in the database and redirects the user to the 'My Recommendations' section on their profile where they can see the changes made.

<img width="1186" alt="book-edited" src="https://user-images.githubusercontent.com/68863341/111533411-a59ae700-875e-11eb-8a0f-3497bcc5f595.png">
<img width="741" alt="book-edited-db" src="https://user-images.githubusercontent.com/68863341/111533418-a7fd4100-875e-11eb-892b-18fe716efcbf.png">

### Edit User
- The Edit User page is accessible via the floating action button on the Profile page (see [Profile](#profile)). The page renders the same form as the signup page with the same format requirements (see [Signup](#signup)).

<img width="539" alt="user-settings" src="https://user-images.githubusercontent.com/68863341/111533457-b21f3f80-875e-11eb-9b61-db78b76a630d.png">

- The fields are already populated with the current information about the user, except for the password. 
- The 'Cancel' button takes the user back to their profile page.
- The 'Edit' button updates the user's information in the database, returns the user to their profile.

<img width="1416" alt="user-edited" src="https://user-images.githubusercontent.com/68863341/111533510-c5320f80-875e-11eb-8ded-9151d8f9b92b.png">
<img width="869" alt="user-edited-db" src="https://user-images.githubusercontent.com/68863341/111533522-c82d0000-875e-11eb-91a4-92a9e9b23c1a.png">

### Delete User
- The Delete User page is accessible via the floating action button on the Profile page (see [Profile](#profile)). The button redirects the user to a simple page with a simple warning message 'Are you sure you want to delete your profile [username]?'.
- The 'Cancel' button returns the user to their profile.
- The 'Delete Profile' button removes the document matching the user's ObjectId from the database and returns the user to the Signup page and displays the flash message 'User deleted'. Manual testing did reveal and error here - the process of deleting the user from the database worked successfully, however, my route had neglected to remove the session user and thus display the navbar tabs for a user not logged in (see image below). Clicking the Logout tab broke the page since their was not a session['user'] in place as required for the rendering of the page. This was fixed by including `session.clear()` in the `delete_user` route in app.py.

<img width="1419" alt="user-deleted" src="https://user-images.githubusercontent.com/68863341/111533632-eabf1900-875e-11eb-981b-a0d949887864.png">

### Logout
- The Logout page is only visible in the navbar to users who are logged in and only able to be navigated to via the navbar.
- A message appears showing the username of the user who is currently logged in. Clicking the 'Logout' button removes the session user, redirects the user to the Login page (see [Login](#login)) and displays the flash message 'You have been logged out'.
- The 'Return To Profile' page (see [Profile](#profile)) correctly redirects the user to their profile page should they change their mind about logging out.

## Automated Testing

### Code Validation

- This project used the W3C Markup Validation Service to validate HTML code. The only errors returned which needed attention were a few incorrect uses of anchor tags and duplicate IDs, which were missed because they were in a Jinja for loop. Other errors raised were those thrown by the use of the Jinja templating language and the absence of a Doctype, since all pages are an extended from base.html. These errors were not thrown when the code was validated via a URL, but I had to use the direct input option for a few pages,  which did. Thus, these errors could be ignored. Only one validation screenshot has been attached for demonstration purposes, since there were too many to include every one.

<img width="1301" alt="home-validate" src="https://user-images.githubusercontent.com/68863341/111221319-3f815900-85d2-11eb-9b7e-d5fe7c8dd97c.png">

- This project used the W3C CSS Validation Service to validate CSS code. No issues were found.

<img width="1484" alt="css-validate" src="https://user-images.githubusercontent.com/68863341/111220315-eebd3080-85d0-11eb-9c25-d8f2f4a52265.png">

- This project used the JSHint website to validate Javascript code. No issues were found.

<img width="1198" alt="js-validate" src="https://user-images.githubusercontent.com/68863341/111220433-13190d00-85d1-11eb-9699-485fc892284f.png">

- This project used PEP8 Online to vaildate Python code. No issues were found.

<img width="1342" alt="pep8-validate" src="https://user-images.githubusercontent.com/68863341/111221444-68095300-85d2-11eb-935a-83d68f0da939.png">

### Browser Validation

Chrome - displays correctly [(view here)](static/images/README-images/chrome-display.png).

Safari - displays correctly [(view here)](static/images/README-images/safari-display.png).

[Autoprefixer CSS online](https://autoprefixer.github.io/) was used to add the necessary prefixers to CSS so that the live website renders across all other browsers.

### Device Validation

The live deployment of this project displays correctly on all of the following device types which were tested via DevTools:

- iPhone 5C
- iPhone 6/7/8
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone X
- iPhone 6/7/8 Plus
- iPad
- iPad Pro
- Laptop with touch
- Laptop with MDPI screen
- Laptop with HiDPI screen

## User Testing

### Mentor Review

### User Review

