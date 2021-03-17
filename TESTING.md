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

### Home (all users)

- The Homepage renders for all users who have not logged in correctly on all screen sizes. The searchbar allows users to input text and pressing both the return key or the button to the right-hand side submits the query to the database. The query returns any results which matches the user's input, including slices of words, for example 'pysch' for psychology. Results display on the All Books page.

- To the right-hand side fo the searchabr are two call to actions: one for login and one for signup. Clicking these buttons takes the user to each page respectively. Hovering over each button causes the background colour to lighten slightly, prompting the user to click.

- The 'Top Picks' section contains the suitable amount of book covers for the screen size and each links to the appropriate individual book page on click. The 'All Books' button just below takes the user to the All Books page.

### Home (logged in user)
- For the logged in user, the home page displays the same as for those who are not logged in, with the exception of the call to action buttons for login and signup. This is because they are no longer relevant for a user who has already acted upon these call to actions. With the new available space, the searchbar becomes centered in the middle of the page.

### All Books
- The All Books page displays the same for those logged in and not logged in. The searchbar at the top of the page allows user to input text and search the database for matching results by using either the button to the right-hand side or the return key. If results are found, a message below is rendered telling the user "Showing results for '[user input]'." Below this a 'Show All Books' button appears which correctly renders the originally All Books page with all books displayed when clicked. If there are no results matching the user's search input, an alternative message stating "Sorry, no results for '[user input]' is displayed. The 'Show All Books' button displays in this case also.
- To the right-hand side fo the searchbar is a yellow button with a + icon. For a user who is logged in, on hover a Materialize tooltip displays to indicate they can add a book recommendation. It returns the Add Book page when clicked. For the user who is not logged in, on hover a Materialize tooltip is displayed advising them to log in if they wish to add a book recommendation. When clicked it renders the Login page.
- The main body of the page displays all books from the database, contained within Materialize cards of equal size. There is up to four books per row displayed on larger and as little as one per row on mobile. Each card contains a book image, title, author-year, category and user who it was added by. If no image_url is associated with the book, the placeholder image in the website style is displayed in its place.
- Click on the book title, image or ellipsis icon renders a page with only the selected book on it and further information.

### Display Individual Book (all users)


### Display Individual Book (logged in user)
- The Display Book page renders a template with all of the information associated with a particular book on its own page. This is achieved by using the unique book _ _id_ in the URL. The book title, author, category, full description and user who it was added by are all displayed correctly. In the top left-hand corner, a button which allows the user to go 'Back To All Books' is displayed.
- Below the book description are a number of user buttons and links. The 'Buy Now' button opens a new window and returns the UK Amazon page for the book. If no link is associated with the book then the button appears as disabled and is has the text 'Not Available' instead.
- The button with the outline of a bookmark icon allows the user to save the particluar book to their reading list. On click, the flash message 'Bookmarked' appears at the top of the page. The action can be confirmed by navigating to the My Profile page where the book will now display in one of the collapsibles in the 'My Reading List' section.
- For users who have added the book which is being displayed to the database themselves (ie it is their recommendation), two controls also appear next to the Buy Now and bookmark buttons: 'Edit' and 'Delete'. They are distinguished from the generic buttons by their yellow background colour. Clicking on the 'Edit' button renders the 'Edit Book' page and clicking on the 'Delete Button' renders triggers a warning which requires the user to confirm they wish to delete the book. If they confirm using the 'OK' button, the book is removed from the database and the user is returned to the All Books page.

### Login
### Signup
### Add Book
### Profile
### Edit User
### Delete User
### Logout

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

