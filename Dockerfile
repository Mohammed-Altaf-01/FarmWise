FROM python:3.10-slim

WORKDIR  /farmwise

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

RUN pipwin install PyAudio==0.2.11

EXPOSE 8501

COPY . /farmwise

CMD streamlit run --server.port 8501 --server.enableCORS false main.py

