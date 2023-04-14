FROM python:3.10

WORKDIR  /farmwise

COPY requirements.txt ./requirments.txt

RUN pip install -r requirments.txt

EXPOSE 8080

COPY . /farmwise

CMD streamlit run --server.port 8080 --server.enableCORS false main.py

#specifying ports are compulsory incase of deploying it will create port for our app to run 

