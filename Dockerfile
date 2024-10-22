
#      Standard version
# FROM python:3.10

#      Slim version
FROM python:3.10-slim

#      Tensorflow version
# FROM tensorflow/tensorflow:2.13.0

#      Or tensorflow to run on Apple Silicon (M1 / M2)
# FROM armswdev/tensorflow-arm-neoverse:r23.08-tf-2.13.0-eigen


# Copy everything we need into the image
COPY songsentiment songsentiment
COPY model_small model_small
COPY raw_data raw_data
COPY api api
COPY requirements.txt requirements_docker.txt
COPY setup.py setup.py

# COPY scripts scripts
# COPY credentials.json credentials.json

# Install everything
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements_docker.txt
RUN pip install .
RUN python -m nltk.downloader punkt stopwords wordnet

# Make directories that we need, but that are not included in the COPY
RUN mkdir /models

# TODO: to speed up, you can load your model from MLFlow or Google Cloud Storage at startup using
# RUN python -c 'replace_this_with_the_commands_you_need_to_run_to_load_the_model'

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
