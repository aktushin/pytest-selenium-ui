FROM python:3.10-slim as base

# Add new user
RUN useradd -ms /bin/bash jenkins

ENV WORKDIR_PATH="/ui-tests" \
    DISPLAY=":99"

WORKDIR $WORKDIR_PATH

# Install packages
RUN apt-get update \
    && apt-get install -y wget

# Install python libs from requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chown -R jenkins $WORKDIR_PATH/

ENTRYPOINT ["python3", "-m", "pytest"]


FROM base as chrome_last
# Install google chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb
USER jenkins


FROM base as firefox_last
# Install firefox
RUN apt-get install -y firefox-esr
USER jenkins