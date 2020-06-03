FROM python:3.7

Add . /tmp/

WORKDIR /tmp/chatapplication/
RUN pip3 install -r requirements.txt

EXPOSE 8000
RUN chmod +x runserver.sh
CMD ["./runserver.sh"]
