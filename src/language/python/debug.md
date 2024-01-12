# Debug Idea

## Flask debugging in PyCharm

![chalice.png](../../images/language/python/flask.png)

## Django debugging in PyCharm

![chalice.png](../../images/language/python/django.png)
Django Setting
![chalice.png](../../images/language/python/django_setting.png)

## Chalice debugging in PyCharm

- https://github.com/aws/chalice/issues/548
- https://github.com/aws/chalice/issues/873

```shell
local --no-autoreload --host 0.0.0.0 --port 8000
```

![chalice.png](../../images/language/python/chalice.png)

## Celery debugging in PyCharm

```shell
-A app.celery worker --scheduler redbeat.RedBeatScheduler -E -B -l info
```

![chalice.png](../../images/language/python/celery.png)

## AWS Serverless Application Model (AWS SAM) debugging in PyCharm

![chalice.png](../../images/language/python/sam_configuration.png)
![chalice.png](../../images/language/python/sam_cli.png)

> Fix PyCharm Fail on Debug SAM
> Can't open file /tmp/lambci_debug_files/pydevd.py: [Errno 13] Permission denied

Add path to `Resources » File sharing`
```shell
/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev
```
![chalice.png](../../images/language/python/docker.png)


