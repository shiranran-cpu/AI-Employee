# AI-Employee

> Hire AI employees. Build products in minutes.

<p align="center">
  <img src="assets/demo.gif" width="900">
</p>

<p align="center">
  <strong>PM · Designer · Frontend · Backend · QA</strong><br>
  An AI company that turns ideas into working software.
</p>

<p align="center">
  <a href="#">Demo</a> •
  <a href="#">Documentation</a> •
  <a href="#">Discord</a> •
  <a href="#">Roadmap</a>
</p>

---

## What is AI-Employee?

AI-Employee is a multi-agent software company.

Instead of using a single AI assistant, AI-Employee creates an entire team of AI employees that collaborate to build products.

You provide an idea.

The AI company does the rest.

```bash
ai-company create "Build a fitness tracking app"
```

Output:

```text
👨‍💼 Product Manager
Writing PRD...

🎨 Designer
Creating UI wireframes...

👨‍💻 Frontend Engineer
Building React pages...

⚙️ Backend Engineer
Generating APIs...

🧪 QA Engineer
Writing tests...
```

Result:

```text
fitness-app/
├── frontend/
├── backend/
├── tests/
├── docs/
└── docker-compose.yml
```

---

## Features

### AI Product Manager

* Product Requirement Documents
* User Stories
* Feature Planning
* Roadmap Generation

### AI Designer

* Wireframes
* UI Specifications
* Design Systems
* User Flow Diagrams

### AI Frontend Engineer

* React
* Next.js
* Tailwind CSS
* TypeScript

### AI Backend Engineer

* FastAPI
* Node.js
* PostgreSQL
* Authentication

### AI QA Engineer

* Unit Tests
* Integration Tests
* Bug Reports
* Test Plans

---

## Architecture

```text
                Human CEO
                     │
                     ▼
              CEO Agent
                     │
 ┌──────────┬─────────┼─────────┬──────────┐
 │          │         │         │          │
 ▼          ▼         ▼         ▼          ▼

PM      Designer   Frontend   Backend     QA
Agent     Agent     Agent      Agent     Agent
```

Each employee has:

* Role-specific memory
* Specialized prompts
* Independent decision making
* Cross-team communication

---

## Quick Start

### Installation

```bash
git clone https://github.com/yourname/AI-Employee.git

cd AI-Employee

pip install -r requirements.txt
```

### Configure API Key

```bash
cp .env.example .env
```

```env
OPENAI_API_KEY=your_key_here
```

### Run

```bash
python main.py
```

---

## Example

Input:

```text
Build a SaaS platform for resume optimization
```

AI-Employee generates:

```text
✓ Product Requirement Document

✓ UI Design

✓ Frontend Source Code

✓ Backend APIs

✓ Database Schema

✓ Automated Tests

✓ Docker Deployment
```

---

## Why AI-Employee?

Most AI tools give you:

```text
One AI Assistant
```

AI-Employee gives you:

```text
An Entire AI Company
```

---

## Roadmap

### v1

* PM Agent
* Designer Agent
* Frontend Agent
* Backend Agent
* QA Agent

### v2

* CEO Agent
* Team Collaboration
* Memory System

### v3

* SaaS Generator
* One-click Deployment
* CI/CD Automation

### v4

* Growth Agent
* Marketing Agent
* Customer Support Agent
* Sales Agent

---

## Tech Stack

* Python
* FastAPI
* LangGraph
* OpenAI Compatible APIs
* Next.js
* Docker

---

## Contributing

Pull requests are welcome.

If you have ideas for new AI employees, open an issue.

---

## License

MIT License

---

<p align="center">
  Build your next startup with AI employees.
</p>
