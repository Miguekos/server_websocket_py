FROM python:3.6

WORKDIR /app

COPY ["./requeriments.txt" , "/app"]

RUN pip install -r requeriments.txt

EXPOSE 7667

COPY ["." , "/app"]

CMD [ "python" , "app.py" ]