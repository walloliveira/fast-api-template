FROM python:3.8.2 as build-stage
COPY ../ /app
WORKDIR /app
RUN apt update
RUN apt install nginx -y
RUN pip install pipenv
RUN pipenv install

FROM build-stage
COPY --from=build-stage /app/uvicorn.conf /etc/nginx/nginx.conf
ENTRYPOINT ["sh", "-c"]
CMD ["pipenv run alembic upgrade head | pipenv run uvicorn app:api --uds /tmp/uvicorn.sock | nginx -g 'daemon off;'"]
