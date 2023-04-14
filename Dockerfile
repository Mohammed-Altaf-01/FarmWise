FROM python:3.10-alpine

WORKDIR  /farmwise

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /farmwise

ENTRYPOINT ["streamlit","run"]

CMD  ["main.py"]

# CMD streamlit run main.py will also work the same 

