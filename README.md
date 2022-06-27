# capstoneProject

# To Run
~PREPARE DATABASE
https://drive.google.com/file/d/1KH9bSOfrgK56V_AUsW9Exb9lXp_Hjzrw/view?usp=sharing

1. Create virtual environment
    - `python -m venv venv`
    - `venv\scripts\activate`
2. Install dependencies
    - `pip install -r requirements.txt`
3. Run server
    - `uvicorn main:app --reload`

# Create "Equipment Manager" user type
1. Go to http://127.0.0.1:8000/docs#/
    - Find register
    - Fill the details except for user_type
    - go to http://127.0.0.1:8000/login/ to login
    - 
# Create "Employee" user type
1. Go to http://127.0.0.1:8000/docs#/
    - Find register
    - Fill the details and put "Employee" on user_type
    - go to http://127.0.0.1:8000/login/ to login
