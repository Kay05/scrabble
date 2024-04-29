# Scrabble Setup Guide

This guide will help you set up the Scrabble application on your machine, which consists of a Django backend and a Vue.js frontend.

## Pre-requisites

Before you start, ensure that Python and Node.js are installed on your system:

1. **Python**: Download and install from [Python's official website](https://www.python.org/downloads/).
2. **Node.js**: Download and install from [Node.js's official website](https://nodejs.org/).

## Part 1: Setting Up the Django Backend

### Step 1: Download and Setup the Django Project

1. **Open a Terminal or Command Prompt**.
2. **Clone the project from GitHub** (replace `https://github.com/Kay05/scrabble.git` with the actual URL):
   ```bash
   git clone https://github.com/Kay05/scrabble.git scrabble
   cd scrabble

3. **Create and activate a virtual environment:** 
    Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
    macOS or Linux:
        ```bash
            python -m venv venv
            source venv/bin/activate

4. **Install Django and other required packages:** 
    ```bash
    cd scrabble_backend
    pip install -r requirements.txt

5. **Run the script to prepare the word dictionary:** 
    ```bash
    cd scrabble_backend
    python word_list.py

6. **Migrate the database:** 
    ```bash
    cd scrabble_backend
    python manage.py migrate

7. **Run the Django server:** 
    ```bash
    cd scrabble_backend
    python manage.py runserver

### Step 2: Verify Backend Setup

**Open a web browser and visit http://127.0.0.1:8000/convert/ to ensure the Django project is running.**.

## Part 2: Setting Up the Vue.js Frontend

### Step 1: Install and Setup the Vue Project

1. **Ensure you are in the root directory of the Django project:**.
    ```bash
    cd vue_frontend
    npm install
    npm run serve

2. **Open a web browser and go to http://localhost:8080/ to see the Vue application.**.


This Markdown file provides a step-by-step guide for your client to follow, ensuring that they can successfully set up and verify each part of the Scrabble application.








