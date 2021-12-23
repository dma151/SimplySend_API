# Project Overview
## Project Links
- [Front End Repository](https://github.com/dma151/SimplySend_APP)
- [Back End Repository](https://github.com/dma151/SimplySend_API)
- [Published App](https://dma151.github.io/SimplySend_APP/)

## Project Description

SimplySend is a very primitive messaging app that is made to solidify understanding of relational databases 
and simply have another option to reach out to a friend if they don't want to sign up for something else,
like Meta, to use facebook messenger, or have an MacOS to user iMessage

## Wireframes

- [Wireframe](project4-wireframe.jpg)
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
| Friend_Request | Relational Model between Users |


| Components | Description |
| --- | :---: |
| App | Renders all other Components |
| NavBar | Has app logo and Navigation options |
| Landing | Holds the registration and sign in functionality |
| UserHome | User homepage when signed in |
| Conversation | Shows previous messages between 2 users and enables users to message on another |
| Friend Request | A modal function that sends the friend request |
| NewConversation | A modal function that creates a new conversation |

#### Time Table

| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: | :---: | :---: | :---: |
| Backend Models/Views | H | 7hr | 15hr | 15hr | 
| App | H | 1hr | 1hr | 1hr |
| NavBar | H | 2hr | 2hr | 2hr |
| Landing | H | 3hr | 5hr | 5hr |
| UserHome | H | 5hr | 12hr | 12hr |
| Conversation H | 5hr | 15hr | 15hr |
| Total(MVP) | H | 23hr | 40hr | 40hr |
| Total(PostMVP) | L | 15hr | 0 | 0 |

## Framework Used

- React
- Django

## Additional Libraries

- [React Bootstrap](https://react-bootstrap.netlify.app/)
- [JavaScript Cookie](https://github.com/js-cookie/js-cookie)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Cors Headers](https://github.com/adamchainz/django-cors-headers)

## Code Snippet

The largest amount of time I spent for this project would probably go to this snippet of code. I did not know how to initialize the Conversation Model that only had a foreign key as a field inside with 2 participating users. After countless hours of research I had to simply redefine the create method for the Serializer and also use a new type of serializer we haven't used in class

```
    class FriendSerializer(serializers.StringRelatedField):
        def to_internal_value(self, value):
            return value
```
```
    def create(self, validated_data):
        print(validated_data)
        participants = validated_data.pop('participants')
        conversation = Conversation()
        conversation.save()
        for email in participants:
            participant = get_object_or_404(User, email=email)
            conversation.participants.add(participant)
        conversation.save()
        return conversation
```

## Future Changes

- Deconstruct the participants and create a contact model thats related to the user model
- Change backend message authors to their emails
- Change the styling and colors of the messages/conversations so its more aesthetically appealing
- Fully implement the CRUD functionality in the front end for conversations and friends
- Upgrade the rendering of the friends list, conversation list, and messages with constant updates