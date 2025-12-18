# Django Minimal Working Example (MWE) - Dynamic Button Page

## Table of Contents
1. [Project Overview](#project-overview)
2. [Objective](#objective)
3. [Technology Summary](#technology-summary)
4. [System Requirements](#system-requirements)
5. [Installation & Setup Instructions](#installation--setup-instructions)
6. [Minimal Working Example (MWE)](#minimal-working-example-mwe)
7. [AI Prompt Journal](#ai-prompt-journal)
8. [Common Issues & Fixes](#common-issues--fixes)
9. [References](#references)

---

## Project Overview
This project is a **Django minimal working example** that demonstrates the fundamentals of Django development.  
It features:
- A single styled page
- A button that, when pressed, cycles through messages in a defined order using **Django sessions**
- Use of templates, static files (CSS), and basic server-side functionality

---

## Objective
**Goal:** Learn Django fundamentals through AI-assisted exploration and create a functional minimal project.  
**End Result:** A web page displaying dynamic messages via a button press.

---

## Technology Summary
- **Django:** A high-level Python web framework for building web applications
- **Use Cases:** Backend development, APIs, dynamic websites
- **Real-World Example:** Instagram, Disqus, and other popular websites use Django

**Core Django Concepts Covered:**
- Project and app structure
- MVT architecture (Model-View-Template)
- Views and URL routing
- Templates and static files (CSS)
- Handling POST requests and sessions

---

## System Requirements
- Python 3.10+
- Django 6.0
- Code editor (VS Code, PyCharm, etc.)
- Terminal / Command Prompt

---

## Installation & Setup Instructions

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd hello_project


Create virtual environment (optional but recommended)

python -m venv venv
source venv/Scripts/activate  # Windows


Install Django

pip install django


Apply migrations

python manage.py migrate


Run the development server

python manage.py runserver


Open your browser and navigate to:

http://127.0.0.1:8000/

"""
inimal Working Example (MWE)
View (home/views.py)
from django.shortcuts import render

def home_view(request):
    messages = [
        "That's what's meant to happen!",
        "You pressed the button! 🎉",
        "Action completed successfully!",
        "Hello! Keep clicking!",
        "Django at work! ✅"
    ]
    
    index = request.session.get('message_index', 0)
    message = ""
    if request.method == "POST":
        message = messages[index]
        index = (index + 1) % len(messages)
        request.session['message_index'] = index

    return render(request, 'home/index.html', {'message': message})

Template (home/templates/home/index.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Styled Page</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'home/style.css' %}">
</head>
<body>
    <div class="container">
        <h1>Hello World 👋</h1>
        <p>This page is styled using Django templates and CSS.</p>
        <form method="POST">
            {% csrf_token %}
            <button type="submit" class="press-button">Press Me</button>
        </form>
        {% if message %}
            <p class="message">{{ message }}</p>
        {% endif %}
    </div>
</body>
</html>

CSS (home/static/home/style.css)
body {
    font-family: Arial, sans-serif;
    background-color: #f4f6f8;
}

.container {
    max-width: 600px;
    margin: 100px auto;
    padding: 30px;
    background: white;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #2c3e50;
}

p {
    color: #555;
}

.press-button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 12px 25px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
}

.press-button:hover {
    background-color: #2980b9;
}

.message {
    margin-top: 20px;
    color: #e67e22;
    font-weight: bold;
    font-size: 18px;
    animation: fadein 0.5s;
}

@keyframes fadein {
    from { opacity: 0; }
    to { opacity: 1; }
}
"""
AI Prompt Journal
Prompt	AI Response Summary	Reflection
"Explain Django project vs app in simple terms"	Django projects are full websites; apps are modules/features inside projects.	Very clear explanation; helped structure my project correctly.
"Create a simple Django view and URL mapping"	Provided example home_view and URL configuration.	Worked perfectly for first “Hello World” view.
"How do I add CSS in a Django project?"	Explained static files, {% load static %}, and linking CSS in template.	Needed slight clarification on folder structure, but easy to fix.
"How to make a button trigger a server-side message?"	Suggested form with POST method and view logic to display messages.	Worked; helped implement dynamic behavior.
"How to cycle messages using Django sessions?"	Explained request.session usage to store index and cycle messages.	Very helpful; directly implemented in MWE.

Reflection:
Using AI accelerated learning, helped troubleshoot errors, and provided working examples. I iterated on prompts to get exact solutions for my project.

Common Issues & Fixes
Issue	Fix
Internal Server Error on button click	Run python manage.py migrate to create session table
CSS not loading	Ensure {% load static %} in template and correct static folder structure
Session index not updating	Check request.session['message_index'] = index is inside POST block
References

Django Official Documentation

Django Tutorials for Beginners

AI-assisted prompts and solutions
