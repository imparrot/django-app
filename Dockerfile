# use base python image with python 2.7
FROM python:3.10

ENV PYTHONUNBUFFERED true

RUN mkdir /root/.pip
COPY pip.conf /root/.pip/
# set working directory to /app/
WORKDIR /app/

# copy requirements.txt to the image
COPY requirements.txt requirements.txt

# install python dependencies
RUN pip install -r requirements.txt

# copy code base to the image
COPY . .
RUN chmod +x run_web.sh
CMD ["./run_web.sh"]
