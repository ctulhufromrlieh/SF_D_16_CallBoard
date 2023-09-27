# SF_D_16_CallBoard
# Skill factory D16 task. Project - "Call board".
## Requirements:
### packages:
celery<br>
django-allauth<br>
django-ckeditor<br>
django-filter<br>
eventlet<br>
redis

### If python version < 3.9 and SQLite is used
JSON1Extension is necessary:
https://code.djangoproject.com/wiki/JSON1Extension

### Redis server
Project use Redis server<br>
(configure "CallBoard\settings_celery.py")

### Email sending
Project use email sending<br>
(configure "CallBoard\settings_email.py" for non-console EMAIL_BACKEND)

### Celery (using in additional terminal windows)
1.a) Run "celery -A CallBoard worker -l INFO -P eventlet --pool=solo" command for email sending on reply create/accept using Windows
1.b) Run "celery -A CallBoard worker -l INFO --pool=solo" command for email sending on reply create/accept otherwise.
2. Run "celery -A CallBoard beat -l INFO" for mass email sending with latest posts.

### All installed packages (result of "pip list" command):
(venv) PS D:\Programing\Python\Learning\SF_D_16_CallBoard\CallBoard> pip list
Package            Version
------------------ ---------
amqp               5.1.1<br>
asgiref            3.7.2<br>
async-timeout      4.0.3<br>
backports.zoneinfo 0.2.1<br>
billiard           4.1.0<br>
celery             5.3.4<br>
certifi            2023.7.22<br>
cffi               1.15.1<br>
charset-normalizer 3.2.0<br>
click              8.1.7<br>
click-didyoumean   0.3.0<br>
click-plugins      1.1.1<br>
click-repl         0.3.0<br>
colorama           0.4.6<br>
cryptography       41.0.4<br>
defusedxml         0.7.1<br>
Django             4.2.5<br>
django-allauth     0.57.0<br>
django-ckeditor    6.7.0<br>
django-filter      23.3<br>
django-js-asset    2.1.0<br>
dnspython          2.4.2<br>
eventlet           0.33.3<br>
greenlet           2.0.2<br>
idna               3.4<br>
kombu              5.3.2<br>
oauthlib           3.2.2<br>
pip                23.2.1<br>
prompt-toolkit     3.0.39<br>
pycparser          2.21<br>
PyJWT              2.8.0<br>
python-dateutil    2.8.2<br>
python3-openid     3.2.0<br>
redis              4.6.0<br>
requests           2.31.0<br>
requests-oauthlib  1.3.1<br>
setuptools         65.5.1<br>
six                1.16.0<br>
sqlparse           0.4.4<br>
typing_extensions  4.7.1<br>
tzdata             2023.3<br>
urllib3            2.0.5<br>
vine               5.0.0<br>
wcwidth            0.2.6<br>
wheel              0.38.4<br>

Skill factory D16 task. Project - "Call board".

Install JSON1Extension:
https://code.djangoproject.com/wiki/JSON1Extension

## Shell commands (use for Category initialization)
from posts.models import Category<br>
<br>
Category.objects.create(name="Танки")<br>
Category.objects.create(name="Хилы")<br>
Category.objects.create(name="ДД")<br>
Category.objects.create(name="Торговцы")<br>
Category.objects.create(name="Гилдмастеры")<br>
Category.objects.create(name="Квестгиверы")<br>
Category.objects.create(name="Кузнецы")<br>
Category.objects.create(name="Кожевники")<br>
Category.objects.create(name="Зельевары")<br>
Category.objects.create(name="Мастера заклинаний")<br>

## Usage
### Entry points:
/posts/ - list of all posts (view only for unauthorized guests)<br>
/replies/ - list of all replies to user's posts (only for authorized guests)<br> 
