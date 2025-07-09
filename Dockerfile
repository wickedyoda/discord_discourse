FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# If not using a requirements.txt:
# RUN pip install discord.py beautifulsoup4 requests

COPY . .

CMD ["python", "bot.py"]