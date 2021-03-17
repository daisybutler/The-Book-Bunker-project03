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

### Home (all users)
### Home (logged in user)
### All Books
### Display Individual Book (all users)
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

