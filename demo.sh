#!/bin/bash

read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then


if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "-- creating python .venv environment"
    python -m venv .venv && source .venv/bin/activate
    python -m pip install --upgrade pip wheel
    python -m pip install -r requirements.txt
fi

echo "-- deleting database"
python manage.py reset_db  --noinput --close-sessions

echo "-- migrating"
python manage.py migrate

echo "-- creating admin user "
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='admin', email='admin@local', password='demo')"
python manage.py add_tika

fi

python manage.py runserver 0.0.0.0:8000

