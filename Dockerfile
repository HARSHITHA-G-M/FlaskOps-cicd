FROM python:3.9

WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
