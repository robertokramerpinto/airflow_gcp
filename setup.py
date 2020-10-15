from setuptools import setup, find_packages

setup(
    name='airflow_gcp',
    version='0.1',
    description='Airflow GCP Porject',
    long_description='Airflow GCP Porject',

    # Author details
    author='roberto kramer',
    author_email='robertokramerpinto@gmail.com',

    packages=find_packages(exclude=['contrib', 'docs'])
)