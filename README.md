# monxun-code
# [Django Portfolio Site](http://monxun-code.herokuapp.com/)

Portfolio Django project highlighting my interests in finance applications, music, and ML using python.
All front end done by hand - Responsive layout still a WIP. 


- Up-to-date [dependencies](./requirements.txt): **Django 3.2.6 LTS**
- Session-Based Authentication, Forms validation
- Deployment scripts: Gunicorn / Nginx

<br />

![Monxun-Code Homepage](https://github.com/Monxun/monxun-code/blob/main/homepage.PNG?raw=true)


## File Structure
Within the download you'll find the following directories and files:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- home/
   |    |
   |    |-- models/                        # Directory for Models
   |    |    |-- biz_models.py             # Models for Biz ML Dashboard Module
   |    |    |-- mus_models.py             # Models for Mus Music Module
   |    |    |-- vbt_models.py             # Models for VBT Module
   |    |    |-- utils/                    # Simple DB Utils
   |    |
   |    |-- views/                         # Handles page rendering for apps
   |    |    |-- biz_view.py               # Views for Biz ML Dashboard Module
   |    |    |-- mus_view.py               # Views for Music Module
   |    |    |-- vbt_view.py               # Views for VBT Module
   |    |    |-- vbt_scripts/              # Directory conatining VBT helper scripts
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

