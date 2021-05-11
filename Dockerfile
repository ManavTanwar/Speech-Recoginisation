# FROM python:3

# USER root

# ENV PYTHONUNBUFFERED 1

# # ENV PORT 8080

# RUN mkdir /code

# WORKDIR /app

# ADD . /app

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

# RUN apt-get update \
#         && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev -y \
#         && pip3 install pyaudio

# COPY . /appdo

# CMD [ "python","./capstone2_main.py" ]

FROM python:3.7

ADD capstone2_main.py /

ADD capstone.py /

RUN pip install googlesearch-python

RUN pip install pyttsx3

RUN pip install speechrecognition

RUN pip install wikipedia

RUN pip install pytest-shutil

RUN pip install subprocess32

RUN pip install pywin32 == 222

RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev -y \
        && pip3 install pyaudio

CMD [ "python","./capstone2_main.py" ]