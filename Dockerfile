FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy project files
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# install library in editable mode
RUN pip install -e .

# default command
CMD ["python"]