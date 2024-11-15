# Ticket Management System

An advanced **Ticket Management System** designed to streamline task management, improve team collaboration, and ensure transparency in progress tracking. This system provides a hierarchical approach to task management with **Tasks**, **Stories**, and **Epics**, allowing seamless organization of work across different roles and permissions.

---

## 📝 Features

### Task Management
- Create tasks with detailed descriptions.
- Assign tasks to specific users or team members.
- Update task statuses:
  - **To Do**
  - **In Progress**
  - **PO Review**
  - **Done** (Restricted to Product Owners only).
- Link tasks to **Stories** for better traceability.

### Story Management
- Create stories to group related tasks.
- Link stories to **Epics** for higher-level organization.
- Track the status and progress of associated tasks.

### Epic Management
- Create Epics to organize large-scale features or projects.
- Link multiple stories to an epic for holistic project tracking.

### Role-Based Permissions
- **Product Owner (PO)**:
  - Can change task statuses to **Done**.
  - Full control over tasks, stories, and epics.
- **Developer**:
  - Can create tasks and update statuses up to **PO Review**.
- **Manager**:
  - View and oversee all tasks, stories, and epics.
  - Assign tasks and manage team collaboration.
- **Team Member**:
  - Basic access to create and update tasks assigned to them.

### Team Collaboration
- Define **Teams** with a schema for managing members and roles.
- Assign team members to specific tasks, stories, or epics.

### Schema-Driven Data Management
- **User Schema**: Manages user details, roles, and permissions.
- **Task Schema**: Tracks task details, status, assignees, and associated stories.
- **Story Schema**: Organizes tasks and links to Epics.
- **Epic Schema**: Represents large-scale features or projects.
- **Team Schema**: Manages team members and their roles.

---

## 📦 Project Structure

```
.
├── README.md                # Project documentation
├── app/
│   ├── database.py          # Database connection and initialization
│   ├── models/              # All schemas and database models
│   │   ├── user.py          # User schema
│   │   ├── task.py          # Task schema
│   │   ├── story.py         # Story schema
│   │   ├── epic.py          # Epic schema
│   │   └── team.py          # Team schema
│   ├── routes/              # API endpoints for the system
│   │   ├── user_routes.py   # User-related endpoints
│   │   ├── task_routes.py   # Task-related endpoints
│   │   ├── story_routes.py  # Story-related endpoints
│   │   ├── epic_routes.py   # Epic-related endpoints
│   │   └── team_routes.py   # Team-related endpoints
│   └── utils/               # Utility functions and helpers
├── tests/                   # Test cases for the system
├── requirements.txt         # Python dependencies
└── config.py                # Project configuration
```

---

## 🛠️ Tech Stack

- **Backend**: Python ( FastAPI )
- **Database**: MongoDB with Motor for async operations
- **Frontend**: React.js or Angular for the user interface
- **Authentication**: OAuth2 or JWT-based authentication
- **Containerization**: Docker for environment consistency


---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- MongoDB installed and running


### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sidharth-sanal-01/TaskManagementAPI.git
   cd TaskManagementAPI
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv env
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Update `config.py` with your MongoDB connection details.

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🧪 Testing

1. Install test dependencies:
   ```bash
   pip install pytest
   ```

2. Run tests:
   ```bash
   pytest
   ```

---

## 🎯 Future Enhancements

- **Integrate Notifications**: Email or in-app notifications for status updates.
- **Kanban Board**: Visualize tasks and stories in a Kanban-style interface.
- **Advanced Reporting**: Generate team performance reports.
- **Third-Party Integrations**: Sync with tools like JIRA, Slack, or GitHub.
- **Mobile App**: Build a companion mobile app for on-the-go access.

---

## 🤝 Contribution

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message"
   ```
4. Push the changes:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

---

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## ✨ Author

- **Your Name**
- GitHub: [@sidharth-sanal-01](https://github.com/sidharth-sanal-01)
- Email: sidharthsanal02@gmail.com

---

With this **Ticket Management System**, manage your team's workflow efficiently and keep track of all your tasks, stories, and epics in one place! 🎉