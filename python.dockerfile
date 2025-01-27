FROM python:3.9

RUN useradd --user-group -r app

WORKDIR /home/app

COPY . .

RUN chown -R app:app /home/app

USER app

RUN pip3 install -r requirements.txt --no-cache-dir

ENTRYPOINT [ "python", "main.py" ]

CMD [ "run" ]