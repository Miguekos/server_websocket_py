FROM python:3.6

WORKDIR /app

COPY ["./requeriments.txt" , "/app"]

RUN pip install -r requeriments.txt

COPY ["." , "/app"]

EXPOSE 7667

CMD [ "python" , "main.py" ]