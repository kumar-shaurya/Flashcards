# Flashcard App 🧠

## App Idea & Features Implemented

This is a simple, cross-platform flashcard application. It's designed to help you study and memorize information using digital flashcards. The app has a clean, user-friendly interface that makes it easy to navigate and interact with your flashcard decks.

### Key Features:

* **Create and Manage Cards**: Easily add new flashcards with a question and a corresponding answer. You can create a deck on any topic you like.

* **Intuitive Navigation**: Navigate through your flashcard deck with simple "next" and "previous" buttons.

* **Flip Cards**: Tap on a flashcard to reveal its answer and test your knowledge.

* **Progress Tracking**: Keep track of your progress with a counter that shows which flashcard you are currently on (e.g., "Q 1 / 10").

* **Persistent Data**: All your flashcards are automatically saved, so you won't lose your deck when you close the application.

* **Delete Cards**: Easily delete flashcards from your deck when you no longer need them.

* **User-Friendly Design**: The app features a simple and elegant dark-themed UI that is easy on the eyes.

---

## Tech Stack & Libraries Used

This application is built with a minimal and efficient tech stack to ensure broad compatibility and performance on various platforms.

* **Beeware**: The core framework used to build this cross-platform application. Beeware allows us to write the app in Python and deploy it on different platforms (like Windows, macOS, Linux, and mobile devices) from a single codebase.

* **Toga**: Toga is Beeware's native, cross-platform UI toolkit. It's used to create all the graphical elements of the app, such as buttons, labels, and input fields.

* **JSON**: The built-in Python `json` library is used to save and load the flashcard data, ensuring that your cards are saved between sessions.

---

## Steps to Run the Project

To get the flashcard app up and running on your machine, follow these simple steps.

1. **Clone the Repository**
   Start by cloning the project from GitHub to your local machine:

   ```git clone [https://github.com/kumar-shaurya/Flashcards.git](https://github.com/kumar-shaurya/Flashcards.git)```
   
   ```cd Flashcards```
   
3. **Install Beeware**
   If you don't alredy have Beeware installed, you'll need to set it up. It is recommended to use a Python virtual environment.

   ```python3 -m venv venv```
   
   ```source venv/bin/activate```
   # On Windows, use
   ```venv\Scripts\activate```
   
   ```pip install beeware```
   
5. **Run the Project**
   Now you can use Beeware's command-line tool to run the app.

   ```briefcase dev```
   
   This command will build and run the app in a development environment, allowing you to see your app in action.

6. **Screenshots**
   !Main Screen(https://github.com/user-attachments/assets/7b95f07b-9468-47b0-a272-46ba1560a0b7)
   
   !Answer after flipping(https://github.com/user-attachments/assets/8feda987-c2de-4602-a549-d0a9b060ff88)
   
   !Add cards(https://github.com/user-attachments/assets/9a67beb2-1325-4328-a4ff-81f028377f78)
   
   !About(https://github.com/user-attachments/assets/d49adde1-420b-4b40-bfb6-e765f914746f)






