# EventBuddy

EventBuddy is an event management platform designed to simplify the organization and execution of various types of events, such as weddings, birthdays, corporate conferences, and college fests. With EventBuddy, organizers can easily track tasks, manage budgets, communicate with participants, and manage vendors.

## Features

- **Multi-Event Management**: Create and manage events for weddings, birthdays, conferences, and college fests.
- **Task Assignment & Tracking**: Easily assign and track tasks for your team members.
- **Budget Management**: Track the expected and actual budgets for every event.
- **Participant Chatroom**: Integrated chatroom feature for event participants.
- **Vendor Management**: Manage vendors, their ratings, and contact information.

## Screenshots

### Event Dashboard
![Event Dashboard](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.13.59%20PM.jpeg)

### Vendor Management
![Vendor Management](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.35.37%20PM.jpeg)

### Event Creation Form
![Event Creation](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.41.10%20PM.jpeg)

### Expense Management
![Budget Overview](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.38.07%20PM.jpeg)

### Participant Chatroom
![Participant Chatroom](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.26.31%20PM.jpeg)

### Task Assignment
![Task Assignment](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.13.59%20PM.jpeg)

### My Tasks
![Tasks](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.34.55%20PM.jpeg)

### Vendor Ratings
![Vendor Ratings](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.19.30%20PM.jpeg)

### Assigned Tasks
![Assigned Task](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.19.12%20PM.jpeg)

### Calendar Integration
![Calendar](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.23.20%20PM.jpeg)

### Notification
![Notification](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.33.57%20PM.jpeg)

### Profile
![Profile](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/Images/WhatsApp%20Image%202024-09-28%20at%202.54.00%20PM.jpeg)

## Installation

To set up this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/VipulMore11/HackDeck_KD_eventbuddy.git
   ```

2. Navigate into the project directory:
   ```bash
   cd HackDeck_KD_eventbuddy
   ```

3. Install the required dependencies for the backend:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the backend development server:
   ```bash
   python manage.py runserver
   ```

6. Open your web browser and visit `http://127.0.0.1:8000` to access the backend API.

## Frontend Setup

1. Navigate to the frontend directory (assuming it’s a separate directory within the repository):
   ```bash
   cd frontend
   ```

2. Install the required dependencies for the frontend:
   ```bash
   npm install
   ```

3. Start the frontend development server:
   ```bash
   npm start
   ```

4. Open your web browser and visit `http://localhost:3000` to access the EventBuddy frontend.

## Usage

1. **Create an Event**: Navigate to the "Create Event" page to start organizing your event. You can input details such as the event type, budget, date, and more.
2. **Assign Tasks**: Use the task assignment feature to delegate responsibilities to your team members.
3. **Budget Management**: Keep track of expected vs actual expenses using the budget management tool.
4. **Chatroom**: Event participants can communicate directly through the integrated chatroom.
5. **Vendor Management**: Add and rate vendors based on their performance.

## API Endpoints

- `/api/events/` - Retrieve, create, and manage events.
- `/api/tasks/` - Manage tasks associated with an event.
- `/api/vendors/` - View and manage vendors for an event.
- `/api/participants/` - Manage participants for a specific event.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push the changes to your fork (`git push origin feature/your-feature-name`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/VipulMore11/HackDeck_KD_eventbuddy/blob/main/LICENSE) file for details.

---

Feel free to reach out with any questions or feedback regarding EventBuddy!
