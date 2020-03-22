#!/bin/sh

pipenv run alembic revision --autogenerate -m "$1"
