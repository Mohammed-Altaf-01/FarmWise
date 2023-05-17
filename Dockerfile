FROM python:3.10-slim

WORKDIR  /app

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT [ "streamlit", "run" ]

CMD ["main.py"]


