# Notely

## Video Demo: https://youtu.be/l2VvaXVwSJs

## Description

In the modern fast paced world, managing both personal and professional responsibilities can be very overwhelming. Keeping track of tasks, deadlines, and important notes often requires having to use multiple tools, leading to inefficiency and stress. Notely is a web based application which is designed to streamline task and note management with a clean, intuitive interface and robust functionality. Notely combines Flask, SQLite, Bootstrap, and custom CSS to deliver a solution that caters to users oragnisational needs, either for personal productivity or professional task planning.
Core Features of Notely:

## Task Management

Notely is a site designed to help users keep track of their tasks. Users can:
* Create tasks with details such as titles, due dates, and categories (Personal or Work).
* Organise tasks by category enabling a focused approach to managing responsibilities.
* View tasks in a calendar format, which provides a clear overview of any deadlines.
* Easily delete tasks when they are no longer needed.
By dividing tasks into “Personal” and “Work” categories and employing colour-coded markers, Notely ensures users can quickly distinguish between their commitments.

## Note Management

Notes are an essential tool for capturing ideas, reminders, and information. Users can:
* Write and save notes directly within the application.
* Delete notes when they are no longer required.
* View notes in a clear list format, with both titles and contents prominently displayed for easy access.

## Dynamic Calendar Integration

Notely incorporates the FullCalendar library, providing a visually appealing and interactive calendar. This feature allows users to:
* View all tasks at a glance, with intuitive colour coding for easy identification.
* Click on individual tasks to manage them further in the Tasks section.
* See past dates greyed out to focus attention on current and future responsibilities.
The calendar is an invaluable feature for users who prefer a top down view of their schedules, making planning more straightforward and efficient.

## Priority Management

The Home Page of Notely is designed with user productivity in mind. By prominently displaying tasks due today and those for the upcoming week, the application helps users prioritise what’s most important. Tasks are grouped and listed by date, ensuring a clear, structured overview.

## Functionality and Design

Notely’s intuitive design makes it easy for users to navigate between its four main sections:

### Home Page
* Focused on helping users prioritise their immediate responsibilities.
* Displays tasks due today, as well as those upcoming within the week.
* Employs colour-coded categories (blue for Personal and green for Work) to enhance readability and organisation.
### Tasks Page
* Allows users to create tasks with specific details, including title, category, and due date.
* Displays tasks categorised into Personal and Work sections for ease of management.
*Provides a simple delete button to remove completed or unnecessary tasks.
### Calendar Page
* Features a fully interactive calendar utilising by FullCalendar.
* Displays all tasks with colour-coded indicators, improving clarity and quick identification.
* Includes clickable tasks that redirect users to the relevant section for updates or modifications.
### Notes Page
* Offers a clean, simple interface for composing and saving notes.
* Displays all saved notes in a list format, with titles and contents clearly visible.
* Allows users to delete notes as needed, maintaining a clutter-free workspace.

## Technical Details

### Backend: Flask Framework
Notely’s backend is built using Flask, a lightweight and versatile web framework in Python. Flask’s simplicity and scalability make it an ideal choice for this project, allowing seamless integration with the SQLite database and the front-end templates.
### Database: SQLite
SQLite serves as the database for Notely, chosen for its simplicity and compatibility with Flask. It stores all task and note data in a structured format, ensuring quick retrieval and updates. When the app is launched, it automatically checks the database for necessary tables and initializes them if they do not exist.
### Front-End: Bootstrap and Custom CSS
The user interface combines the flexibility of Bootstrap with custom CSS for enhanced styling. This mix ensures that Notely is both responsive and visually appealing across devices. Features like colour-coded tasks, neatly organised forms, and an interactive calendar contribute to a polished user experience.
### FullCalendar Library
The integration of the FullCalendar library elevates the Calendar Page by providing a dynamic and interactive experience. FullCalendar seamlessly integrates with the database to render tasks with appropriate colour codes and interactivity, enabling users to manage their schedules efficiently.

## Design Decisions
The development of Notely involved several key design decisions aimed at maximising usability:
* Task Categorisation and Colour Coding: Dividing tasks into Personal and Work categories helps users focus on relevant responsibilities, while colour coding provides visual clarity.
* Interactive Calendar: The calendar view offers a comprehensive yet straightforward way to view and manage tasks, making planning less daunting.
* Simplicity and Accessibility: By using Flask and SQLite, the app maintains a lightweight, efficient design suitable for users with varying levels of technical expertise.
*Error Handling: Input validation ensures a smooth user experience by guiding users to provide all necessary details, such as task titles or note content.

## Challenges and Future Enhancements
Developing Notely came with its share of challenges, particularly in integrating dynamic task data with the FullCalendar library. The solution involved formatting the database output to match the library’s required input format, which took significant effort to debug and refine.
While the current iteration of Notely is highly functional, there are several areas for potential improvement:
* User Authentication: Adding authentication would enable multiple users to manage their tasks and notes independently.
* Recurring Tasks: Implementing functionality for recurring tasks would simplify scheduling repetitive responsibilities.
* Search Functionality: A search bar for tasks and notes could enhance navigation and accessibility, especially for users managing a large number of entries.
* Mobile App Integration: Developing a mobile version or app could extend Notely’s usability, catering to users wherever they may be.

## Installation and Usage
Setting up Notely is quick and straightforward:
1. Clone the repository using your preferred version control system.
2. Install the required Python packages by running the command: pip install flask
3. Launch the application by running: python app.py
4. Open your web browser and go to http://127.0.0.1:5000 to start using Notely.

## Final Thoughts
Notely represents a practical and user friendly solution for task and note management. By combining intuitive design with powerful features such as an interactive calendar and colour coded task categorisation, the application simplifies personal and professional organisation.

This project is a culmination of the web development concepts learned through the CS50 course and serves as a testament to the capabilities of Flask for building strong web applications. Whether you’re managing deadlines, tracking personal goals, or jotting down ideas, Notely is a tool designed to make life simpler, one task at a time.

