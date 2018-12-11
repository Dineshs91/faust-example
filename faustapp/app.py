import os
import sys

import faust
import django

# make sure the gevent event loop is used as early as possible.
os.environ.setdefault('FAUST_LOOP', 'eventlet')

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
# set the default Django settings module for the 'faust' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faust_proj.settings')
django.setup()

app = faust.App('faust_proj', autodiscover=True, origin='faustapp')


@app.on_configured.connect
def configure_from_settings(app, conf, **kwargs):
    from django.conf import settings
    conf.broker = settings.FAUST_BROKER_URL
    conf.store = settings.FAUST_STORE_URL


if __name__ == '__main__':
    app.main()
