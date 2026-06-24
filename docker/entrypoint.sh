#!/bin/sh
set -e

echo "Waiting for postgres..."

while ! nc -z postgres 5432; do
  sleep 1
done

echo "PostgreSQL started"

if [ "$RUN_MIGRATIONS" = "1" ]; then
  echo "Running migrations..."
  python manage.py makemigrations --settings=config.settings.production
  python manage.py migrate --settings=config.settings.production --noinput
  python manage.py collectstatic --settings=config.settings.production --noinput
fi

exec "$@"