FROM python:3
COPY ./main.py ./main.py
RUN pip install requests
CMD [ "python", "./main.py" ]