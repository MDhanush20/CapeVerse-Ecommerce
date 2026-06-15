
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

<img width="1463" height="731" alt="image" src="https://github.com/user-attachments/assets/c972c14b-581b-4baa-b6ca-ceb4cdbd0a84" />


<img width="1462" height="733" alt="image" src="https://github.com/user-attachments/assets/4e2b7a02-6c25-45c5-8f1e-3a7ca5471a91" />


<img width="1455" height="722" alt="image" src="https://github.com/user-attachments/assets/ad2d7456-a758-4b8d-956a-356624639813" />

<img width="1463" height="726" alt="image" src="https://github.com/user-attachments/assets/8e8f465e-cc0f-4bac-b35f-543532a91425" />

<img width="1467" height="725" alt="image" src="https://github.com/user-attachments/assets/d8cb4e87-d336-4e97-a83c-8a77a51f807a" />


### Home Page

<img width="1467" height="729" alt="image" src="https://github.com/user-attachments/assets/9ae6b9f9-26d2-419f-a8bf-110bf5a77693" />



### Product Page

<img width="1469" height="732" alt="image" src="https://github.com/user-attachments/assets/e3f4902c-94f4-4406-a414-b1f18d3b246c" />


### User Authentication

<img width="1477" height="721" alt="image" src="https://github.com/user-attachments/assets/d96a2d6d-c4f5-4d7c-9b78-9f19705b82a0" />

<img width="1485" height="719" alt="image" src="https://github.com/user-attachments/assets/f76ffb62-2ed6-4761-a1fb-fb6b42d8c402" />

### Footer
<img width="1450" height="735" alt="image" src="https://github.com/user-attachments/assets/d3ee7faa-1a23-44cb-9c4b-622414128d17" />


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

# CapeVerse-Ecommerce
CapeVerse is a Django-based eCommerce web app featuring product listings, user authentication, shopping cart, and admin management. Built with Python, Django, Bootstrap, and SQLite, it showcases full-stack development and UI/UX design skills for scalable online shopping.
