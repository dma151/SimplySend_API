# Project Overview
## Project Links
- []()
## Project Description

SimplySend is a very primitive messaging app that is made to solidify understanding of relational databases 
and simply have another option to reach out to a friend if they don't want to sign up for something else,
like Meta, to use facebook messenger, or have an MacOS to user iMessage

## Wireframes

- [Wireframe](project4-wireframe.md)
- [React Structure](#) Coming soon

## MVP/Post MVP
#### MVP

Functional app where a user can send a message to another user and when the other user signs in they can see it
- Users can register/Sign in
- Signed in User can use CRUD to manage friends
- Signed in User can view list of Friends
- Signed in User can view list of conversations

#### PostMVP

- Create notifications for updated messages
- Create an instant update on conversation model if users are both logged in
- CSS styling all the components for a pleasant chat experience
- Add images to friends
- Incorporate use of emojis
- Be able to have conversations with groups of people

## Models/Components

| Models(MVP) | Description |
| --- | :---: |
| User | Use of the app that can add friends and message them |
| Conversations | Database that stores conversation between 2 Users |
| Friend | Relational Model between Users |


| Components | Description |
| App | Renders all other Components |
| NavBar | Has app logo and Navigation options |
| Register | Users can register for the app |
| SignIn | USers sign in here and if successful takes them to the homepage |
| UserHome | User homepage when signed in |
| Conversation | Shows previous messages between 2 users and enables users to message on another |

#### Time Table

| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: | :---: | :---: | :---: |
| App | H | 1hr | 1hr | 1hr |
| NavBar | H | 2hr |  |  |
| Register | H |  |  |
| SignIn | H |  |  |
| UserHome | H |  |  |
| Conversation H |  |  |
| Total(MVP) | H | 19.5hr | 16hr | 16hr |
| Total(PostMVP) | L | 15hr | 7hr | 5hr |

## Framework Used

- React
- Django

## Additional Libraries

- [React Bootstrap](https://react-bootstrap.netlify.app/)

## Code Snippet
