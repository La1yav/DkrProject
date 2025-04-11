FROM python:3.10
WORKDIR /dkrproject
COPY code.py .
RUN pip install flask colorama
CMD ["python", "code.py"]