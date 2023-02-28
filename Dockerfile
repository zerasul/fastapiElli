FROM python:slim
RUN pip install pipenv
RUN mkdir elliapi
WORKDIR elliapi/
EXPOSE 8000
COPY . /elliapi
VOLUME [ "/images" ]
RUN ln -s /images images
RUN pipenv install
CMD [ "pipenv", "run", "startapi" ]
