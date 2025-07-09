# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install required libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot source code
COPY . .

# Run the bot
CMD ["python", "bot.py"]