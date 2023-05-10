FROM python:3.10-slim

WORKDIR  /farmwise

COPY requirements.txt ./requirements.txt

RUN pip install -r requirments.txt

EXPOSE 8501

COPY . /farmwise

CMD streamlit run --server.port 8501 --server.enableCORS false main.py

#specifying ports are compulsory incase of deploying it will create port for our app to run 
