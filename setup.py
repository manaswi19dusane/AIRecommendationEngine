
from setuptools import setup, find_packages

setup(
    name="airecommendationengine",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "mysql-connector-python"
    ],
    author="Manaswi Dusane",
    description="Scalable AI Recommendation Engine with DB support",
)
