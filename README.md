![Logo](https://raw.githubusercontent.com/C0DE-SLAYER/AutoMax/master/github_assets/logo.png)

> Developed a marketplace for car for buying and selling using django

## About django
* Django's high-level Pythonic API promotes rapid development and clean, pragmatic design.
* It handles small to large-scale projects with ease, offering flexibility and performance.
* Includes robust ORM, URL routing, template engine, authentication, and more, saving development time.

## Installation

```python
git clone https://github.com/C0DE-SLAYER/AutoMax
cd AutoMax

pip install -r requirement.txt

# Change the .env.example file to .env and fill the field accordingly. If using the s3 bucket uncomment the storages section in settings.py file and fill the field accordingly

python manage.py migrate # Database migrations
python manage.py createsuperuser # Create a superuser (Optional)
python manage.py runserver # Head to 127.0.0.1:8000 to view the website
```

## For deployment instructions
- please visit the [deployment branch](https://github.com/C0DE-SLAYER/AutoMax/tree/deployment).

## Demo

![demo_1](https://raw.githubusercontent.com/C0DE-SLAYER/AutoMax/master/github_assets/demo_1.png)
![demo_2](https://raw.githubusercontent.com/C0DE-SLAYER/AutoMax/master/github_assets/demo_2.png)
![demo_3](https://raw.githubusercontent.com/C0DE-SLAYER/AutoMax/master/github_assets/demo_3.png)
![demo_4](https://raw.githubusercontent.com/C0DE-SLAYER/AutoMax/master/github_assets/demo_4.png)
![demo_5](https://raw.githubusercontent.com/C0DE-SLAYER/AutoMax/master/github_assets/demo_5.png)

## License

[MIT](https://github.com/C0DE-SLAYER/AutoMax/blob/master/LICENSE.txt)