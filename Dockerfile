FROM python:3.10-slim

WORKDIR  /farmwise

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . ./

CMD streamlit run --server.port=8501 --server.enableCORS false main.py

