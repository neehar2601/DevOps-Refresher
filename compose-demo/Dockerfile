# Start with Python
FROM python:3.9-alpine

# Set working directory
WORKDIR /code

# Copy dependencies and install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Run the app
CMD ["python", "app.py"]
