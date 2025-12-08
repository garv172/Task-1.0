# Task-1.0
Overview

Task-1.0 implements backend APIs to add, edit, delete, and fetch comments for a given task using clean, REST-compliant CRUD principles.
This project also includes automated tests to ensure reliability, correctness, and long-term maintainability of each API endpoint.

The goal is to provide a scalable, modular backend for comment management that can be integrated into any task-based application.

🚀 Features

Fully functional REST APIs

CRUD operations for comments

Follows clean backend principles

Input validation

Error handling

Automated tests for each endpoint

Extensible architecture for future tasks

🧰 Tech Stack

Node.js / Express.js (or Flask / Django / Spring — update as needed)

Database: MongoDB / PostgreSQL / MySQL

Testing: Jest / Mocha / PyTest / JUnit

#Tools: Postman, npm, Git

🔧 API Endpoints (Typical Example)
Method	Endpoint	Description
POST	/tasks/:taskId/comments	Add a new comment
GET	/tasks/:taskId/comments	Get all comments for a task
PUT	/comments/:commentId	Update a specific comment
DELETE	/comments/:commentId	Delete a comment

(Modify these based on your actual implementation.)

🛠️ Getting Started
1. Clone the repository
git clone https://github.com/garv172/Task-1.0.git
cd Task-1.0

2. Install dependencies
npm install


(Modify: pip install -r requirements.txt for Python, etc.)

3. Configure environment variables

Create a .env file:

DB_URL=your_database_url
PORT=3000

4. Start the server
npm start

5. Run automated tests
npm test

📘 Creating Your PR
Title

Provide a clear, specific title describing the change.

Good: “Add PUT API to update comments + test cases”

Bad: “Changes done”

# Description

Fill out the entire PR description. This serves as documentation for future developers.

# Why this change is needed

Explain the purpose (e.g., added new API, improved validation, fixed bug, added tests).
Context prevents confusion and avoids future issues.

# API / Database Changes

Document any updated or newly added routes or database fields.
If none, mention “None.”

# Screenshots / Output Samples

Include:

Curl responses

Postman screenshots

Example JSON output

This speeds up code reviews.

Testing

# Describe how you tested the change:

Automated tests

Manual API tests via Postman

Edge cases

Meta Information
Assignee

Assign the PR to yourself — you own this change.

# Labels

Use relevant labels:

feature

bug

documentation

testing

enhancement

Helps with filtering and tracking.
