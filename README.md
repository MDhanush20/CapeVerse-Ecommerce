# CapeVerse Ecommerce

CapeVerse is a Django-based eCommerce web application that provides product browsing, user account management, and an organized online shopping experience.

## Features

* User Registration and Login
* Product Management
* Product Listing Pages
* Product Detail Pages
* Django Admin Panel
* Media File Support
* Responsive Frontend Design
* SQLite Database

## Built With

* Python
* Django
* HTML5
* CSS3
* JavaScript
* SQLite

## Project Structure

CapeVerse/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── products/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── capeverse/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── ecom/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
├── manage.py
├── .gitignore
├── readme.md
└── db.sqlite3

## Installation

### Clone the repository

bash
git clone https://github.com/MDhanush20/CapeVerse-Ecommerce.git
cd CapeVerse-Ecommerce


### Create a virtual environment

bash
python -m venv .env


### Activate the virtual environment

Windows:

bash
.env\Scripts\activate


Linux/macOS:

bash
source .env/bin/activate


### Install dependencies

bash
pip install -r requirements.txt

### Apply migrations

bash
python manage.py migrate


### Run the development server

bash
python manage.py runserver


Visit:

text
http://127.0.0.1:8000/


## Screenshots

<img width="1456" height="727" alt="image" src="https://github.com/user-attachments/assets/58037bbd-0499-4690-9325-9d06f610bbc1" />

<img width="1468" height="723" alt="image" src="https://github.com/user-attachments/assets/9d9c0441-13e2-41a4-acce-5417a3bd8997" />

<img width="1466" height="725" alt="image" src="https://github.com/user-attachments/assets/be70c328-108b-4059-9687-9541ff5bcaeb" />


### Home Page

<img width="1456" height="727" alt="image" src="https://github.com/user-attachments/assets/dfcfae01-e0d6-4913-8381-0eaff607aa7f" />


### Product Page

<img width="1471" height="698" alt="image" src="https://github.com/user-attachments/assets/5ae3c6bb-24c8-4aac-a1cf-95a74d73879b" />


### User Authentication

<img width="1480" height="733" alt="image" src="https://github.com/user-attachments/assets/6dc352e3-996c-455d-8650-72af6b10012f" />

<img width="1478" height="735" alt="image" src="https://github.com/user-attachments/assets/404814de-c3e1-470e-9d96-e443e129155e" />

### Footer
<img width="1449" height="720" alt="image" src="https://github.com/user-attachments/assets/fb0648bf-0bd1-4e1e-9471-b91f3dc37ce0" />


## Future Improvements

* Shopping Cart
* Wishlist
* Order Management
* Payment Gateway Integration
* Product Reviews and Ratings
* Email Notifications
* Search and Filtering

## Author

Dhanush

## License

This project is created for learning, practice, and portfolio purposes.
