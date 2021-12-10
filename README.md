# Monxun-Code
# [Django Portfolio Site](http://monxun-code.herokuapp.com/)

Portfolio Django project highlighting my interests in finance applications, music, and ML using python.
All front end done with pure HTML5 and CSS/SCSS - Responsiveness of layout still a WIP... 


- DJANGO Backend / Django-Ninja API / Django-Rest-Framework
- HTMX and Hyperscript used for inline JS functionality / AJAX requests
- Results of ML Dashboard derived from Kaggle_Store_Timeseries repo: https://github.com/Monxun/Kaggle_Store_TimeSeries  
- VBT Backtester App utilizes VectorBT for backtesting, Finviz API and Gamestonk Terminal methods for gathering data.
- Memcached for Cacheing, Postgres / Mongo DB integration (Postgres in current version)
- Bootstrap 4-5
- Deployment scripts: Gunicorn / Nginx with Heroku

*Docker files coming soon*

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

# BIZ ML DASHBOARD
![Monxun-Code Biz](https://github.com/Monxun/monxun-code/blob/main/home/static/assets/images/brand/biz-card.PNG?raw=true)

# MUSIC API INTERFACE
![Monxun-Code Biz](https://github.com/Monxun/monxun-code/blob/main/home/static/assets/images/brand/mus-card.PNG?raw=true)

# VBT FINANCE BACK TESTER 
![Monxun-Code Biz](https://github.com/Monxun/monxun-code/blob/main/home/static/assets/images/brand/vbt-card.PNG?raw=true)
