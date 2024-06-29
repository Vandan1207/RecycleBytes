# RecycleBytes

---

# E-Waste Collection and Recycling Platform

## Project Overview
This project is a web application for e-waste collection and recycling. Users can exchange their e-waste for money through this platform. The project is built using HTML, CSS,Bootstrap, JavaScript, and Django.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Database Configuration](#database-configuration)
4. [Running the Project](#running-the-project)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Requirements
- Python 3.12
- XAMPP (to manage MySQL and Apache)
- Django
- Django Cart
- MySQL

## Installation

### Step 1: Set up a virtual environment
Create a virtual environment for your project to manage dependencies:

bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`


### Step 2: Install XAMPP
Download and install XAMPP from [apachefriends.org](https://www.apachefriends.org/index.html). This will help you manage MySQL and Apache.

### Step 3: Install required Python packages
Use pip to install the necessary packages:

bash
pip install cart \n
pip install mysqlclient \n
pip install django


## Database Configuration

### Step 4: Configure the database
Edit the settings.py file in your Django project to configure the MySQL database. Add the following lines:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oddo',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


### Step 5: Start MySQL and Apache in XAMPP
Open XAMPP and start the MySQL and Apache services.

## Running the Project

### Step 6: Run the Django server
Navigate to your project directory and run the following command to start the Django development server:

bash
python manage.py runserver


The server should now be running at http://127.0.0.1:8000/.

## Usage
1. Open a web browser and go to http://127.0.0.1:8000/.
2. Register or log in to your account.
3. Use the platform to exchange your e-waste for money.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README file should provide clear instructions for setting up and running your project. Make sure to replace any placeholder text with specific information relevant to your project as needed.
