
<br>



<br />
<p align="center">
  <a href="https://github.com/mrpourhoseini/DjangoBlog">
    <img src="static/images/png/logo-no-background.png" alt="Logo" width="400">
  </a>

  <h3 align="center">A simple blog with Django framework</h3>

  <h3 align="center">

  ![python](https://img.shields.io/badge/python-v3.11.5-asd?logo=python&logoColor=%232b5b84&label=python&labelColor=%23ffd343&color=%232b5b84)
  ![django](https://img.shields.io/badge/django-v4.2.5-a?logo=django&logoColor=%23092E20&label=django&labelColor=%23fff&color=%23092E20)
  ![tailwind](https://img.shields.io/badge/tailwindcss-v3.3.3-a?logo=tailwindcss&logoColor=%2306B6D4&label=tailwindcss&labelColor=%23fff&color=%2306B6D4)
  
  </h3>
</p>


<!-- ABOUT THE PROJECT -->

## About The Project

![Django Blog](static/images/png/screenshot.jpg)

Django Blog is a simple and basic practice project. In this blog, we have the possibility to create articles, categories, tags and commenting system. This project is written with the popular Django framework as a full stack, and the Tailwindcss framework is used for the user interface part. In more detail, [Flowbite](https://flowbite.com/) website components have been used for the front-end section.

Features:
* Function base view
* Extending User Model Using a One-To-One Link
* Categories and subcategories
* Content tagging system
* Comments system

In this project, the management panel of users and authors is the same as Django's default admin panel, and the main focus has been on the basic concepts of MVT architecture.


### Built With

As mentioned, this project is written as a full stack and the following tools were used to build it:


* [Django](https://www.djangoproject.com/)
* [SQLite(default DB)](https://www.sqlite.org/index.html)
* [Tailwindcss](https://tailwindcss.com/)
* [Flowbite](https://flowbite.com/)



<!-- GETTING STARTED -->

## Getting Started

In this section, we present the installation and implementation of the project for those interested.

### Prerequisites

Before doing anything, you need to install two prerequisites, Python and NodeJS.
1. [Python](https://www.python.org/)
2. [NodeJS](https://nodejs.org/en)

### Installation
1. Creating and activating the virtual environment(depends on OS)

2. Clone the repo
   ```sh
   git clone https://github.com/mrpourhoseini/DjangoBlog.git
   ```
3. Install requirements packages
    ```sh
    pip install -r requirements.txt
    ```
4. Install NPM packages
   ```sh
   npm install
   ```


<!-- USAGE EXAMPLES -->

## Usage

To implement the project, we follow the following order:

1. Start a new database
   ```sh
    python manage.py makemigrations
    python manage.py migrate
   ```
2. Creating a superuser
   ```sh
    python manage.py createsuperuser
   ```
3. Running the server
    ```sh
    python manage.py runserver
    ```
4. Start the Tailwind CLI build process
   ```sh
   npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch
   ```

<!-- CONTACT -->

## Contact

Mohammadreza Pourhoseini - mohammadreza.pour.computer@gmail.com

