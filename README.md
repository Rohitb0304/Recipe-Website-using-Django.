# Django Project Setup

This repository contains the code for a Django project named `core` with an app named `vege`. Follow the instructions below to set up the project on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- Python 3.x
- pip (Python package installer)
- virtualenv

## Installation

### Windows

1. **Install Python**

   Download and install Python from [python.org](https://www.python.org/downloads/).

   ```bash
   python --version
   ```

2. **Install Django**

   ```bash
   pip install django
   ```

3. **Create a Virtual Environment**

   ```bash
   python -m venv env
   ```

4. **Activate the Virtual Environment**

   ```bash
   .\env\Scripts\activate
   ```

### macOS

1. **Install Python**

   ```bash
   brew install python
   ```

2. **Install Django**

   ```bash
   pip3 install django
   ```

3. **Create a Virtual Environment**

   ```bash
   python3 -m venv env
   ```

4. **Activate the Virtual Environment**

   ```bash
   source env/bin/activate
   ```

### Linux

1. **Install Python**

   ```bash
   sudo apt-get update
   sudo apt-get install python3
   ```

2. **Install Django**

   ```bash
   sudo apt-get install python3-pip
   pip3 install django
   ```

3. **Create a Virtual Environment**

   ```bash
   python3 -m venv env
   ```

4. **Activate the Virtual Environment**

   ```bash
   source env/bin/activate
   ```

## Create Django Project and App

1. **Create Django Project**

   ```bash
   django-admin startproject core
   ```

2. **Create Django App**

   ```bash
   cd core
   django-admin startapp vege
   ```

## Replace Project Files

Replace the following files in the `core` directory with the ones provided:

- `settings.py`
- `urls.py`

Replace the following files in the `vege` directory with the ones provided:

- `views.py`
- `models.py`
- `admin.py`

Add the `templates` folder as provided.

## Apply Migrations

1. **Make Migrations**

   ```bash
   python manage.py makemigrations
   ```

2. **Migrate**

   ```bash
   python manage.py migrate
   ```

## Create Superuser

Create a superuser to access the Django admin interface.

```bash
python manage.py createsuperuser
```

## Run the Server

Start the Django development server.

```bash
python manage.py runserver
```

Open your web browser and go to `http://127.0.0.1:8000/` to see the project in action.

## Contributing

If you would like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
