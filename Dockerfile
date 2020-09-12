FROM python:3

WORKDIR /app

RUN apt update && apt install -y \
       default-jre \
    && rm -rf /var/lib/app/lists/*

RUN pip install nltk
RUN python -m nltk.downloader punkt

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

RUN chmod a+x *.py

ENTRYPOINT ["./gts.py"]

