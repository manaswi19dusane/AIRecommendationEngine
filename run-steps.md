
# Running AIRecommendationEngine v2 with Docker

This guide explains how to run the **AIRecommendationEngine v2** locally using **Docker**.  
Using Docker ensures the project runs in a consistent environment without installing Python or dependencies on your host machine.

---

# 1. Prerequisites

Install the following:

- Docker Desktop (Mac / Windows)
- Docker Engine (Linux)

Verify installation:

```bash
docker --version
```

Expected output example:

```
Docker version 24.x.x
```

---

# 2. Project Structure

Your project directory should look like this:

```
AIRecommendationEngine_v2
│
├── airec
│   ├── algorithms
│   ├── application
│   ├── data_sources
│   ├── domain
│   ├── infrastructure
│   └── utils
│
├── examples
│   ├── train_from_csv.py
│   └── train_from_mysql.py
│
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

# 3. Create Dockerfile

Create a file named:

```
Dockerfile
```

Add the following:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install -e .

CMD ["python"]
```

---

# 4. Build Docker Image

Navigate to the project root directory and run:

```bash
docker build -t airec-engine .
```

Docker will:

1. Pull Python image
2. Copy project files
3. Install dependencies
4. Install the recommendation library

---

# 5. Run Docker Container

Start a container:

```bash
docker run -it airec-engine
```

You will enter the container shell.

---

# 6. Train Recommendation Model

Inside the container run:

```bash
python examples/train_from_csv.py
```

This will:

- Load the dataset
- Train the recommendation model
- Generate a model file

Output:

```
book_model.pkl
```

---

# 7. Run Recommendation Script

Example test script:

```
test_recommend.py
```

```python
from airec import Recommender
from airec.algorithms.content_based import ContentBased

recommender = Recommender(ContentBased())

recommender.load_model("book_model.pkl")

print(recommender.recommend(item_id=1))
```

Run:

```bash
python test_recommend.py
```

---

# 8. Mount Local Folder (Recommended)

To access local files inside Docker:

```bash
docker run -it -v $(pwd):/app airec-engine
```

This mounts your project directory into the container.

---

# 9. Run Training Directly

You can run scripts without entering the container:

```bash
docker run -it airec-engine python examples/train_from_csv.py
```

---

# 10. Optional: Docker Compose (Recommended for MySQL)

Create:

```
docker-compose.yml
```

```yaml
version: "3.9"

services:

  recommender:
    build: .
    container_name: airec-engine
    volumes:
      - .:/app
    command: python examples/train_from_csv.py

  mysql:
    image: mysql:8
    container_name: airec-mysql
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: recommendation
    ports:
      - "3306:3306"
```

Run:

```bash
docker compose up
```

---

# 11. Stopping Containers

Stop running containers:

```bash
docker compose down
```

---

# 12. Useful Docker Commands

List containers:

```bash
docker ps
```

List images:

```bash
docker images
```

Remove image:

```bash
docker rmi airec-engine
```

---

# 13. Troubleshooting

### Docker not found

Install Docker Desktop.

### Permission issues

Run:

```bash
sudo docker build -t airec-engine .
```

### Dataset not found

Make sure files are mounted using:

```
-v $(pwd):/app
```

---

# 14. Summary

Recommended workflow:

```
docker build -t airec-engine .
docker run -it -v $(pwd):/app airec-engine
python examples/train_from_csv.py
```

---

# Author
Manasvi Dusane
