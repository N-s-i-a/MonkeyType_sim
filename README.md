# MonkeyType_sim
A lightweight typing test web application inspired by Monkeytype, built using Python, Flask, and HTML templates.
Project Structure
├── templates/
│   ├── firstpage.html      # Home/Typing interface
│   └── secondpage.html     # Result interface
├── .gitignore
├── LICENSE
├── aug.py                  # Main Flask app, routes, and entry point
├── base.py                 # Core Monkeytype simulation logic
└── requirements.txt        # Project dependencies
Prerequisites
Python Version: Python 3.12 is recommended.
Follow these steps to run the project locally.
Step 1: Clone the Repository
Open your terminal and run:
Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Step 2: Set Up a Virtual Environment (Recommended)
Creating a virtual environment isolates your project dependencies:
Bash
Create the virtual environment
python3 -m venv venv
Activate the virtual environment
On macOS / Linux:
source venv/bin/activate
On Windows (Command Prompt):
venv\Scripts\activate.bat
On Windows (PowerShell):
venv\Scripts\Activate.ps1
#Add your secret key by creating '.env' file in root directory
add the line FLASK_SECRET_KEY=your_custom_key_here
Step 3: Install Dependencies
Install your project requirements using pip:
Bash
pip3 install -r requirements.txt
Step 4: Run the Application
Start the Flask server by executing your routing file (aug.py)
Bash
python3 aug.py
Step 5: Open in Browser
Open your web browser and navigate to:
 http://127.0.0.1:8080
