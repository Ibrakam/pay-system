FROM python:lates

WORKDIR /pay_system

COPY . /pay_system

RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--reload"]










