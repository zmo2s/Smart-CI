# Use official Python 3.12 image
FROM python:3.12-slim

# Install git and other required utilities
RUN apt-get update && apt-get install -y git

# Set working directory inside the container
WORKDIR /app



# Copy your script into the container
COPY . .

# (Optional) Install any dependencies if you have a requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Default command to run your script
# Replace 'your_script.py' with your actual script name
ENTRYPOINT ["python", "choose_test.py"]
CMD ["--diff", "origin/main...HEAD"]