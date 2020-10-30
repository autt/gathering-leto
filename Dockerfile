################################################
# BUILD

FROM python:3.6-slim AS BUILD
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

# Use virtualenv to get all deps into one single isolated directory which we then can copy to the release image
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/venv

# Install deps first to make use of docker layer caching for faster builds later on, then copy the app code
COPY requirements.txt .
RUN pip install -r requirements.txt
# Then copy the app code and build it
COPY . .

COPY /src/data /src/data
RUN pip install /src/data

ENTRYPOINT ["python"]


################################################
# TEST

# N/A



################################################
# RELEASE

FROM python:3.6-slim AS RELEASE

WORKDIR /app
COPY --from=BUILD /opt/venv /app

# Make sure we use the virtualenv:
ENV PATH="/app/bin:$PATH"

# Establish the runtime user (with no password and no sudo)
RUN useradd -m app
USER app

# Startup
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["app.py"]
