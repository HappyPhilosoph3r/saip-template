FROM python:3.11.4-bullseye

WORKDIR /student-attrition-model

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["hypercorn", "--bind=0.0.0.0", "main:create_app()"]

EXPOSE 8000
