#!/bin/sh

. ./scripts/migrate-upgrade.sh

pipenv run uvicorn app:api --reload --host "0.0.0.0" --port "5000"
