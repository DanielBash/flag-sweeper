![placeholder](https://github.com/DanielBash/flag-sweeper/blob/main/.github/github-banner.png?raw=true)
[![flask tests](https://github.com/DanielBash/flag-sweeper/actions/workflows/python-tests.yaml/badge.svg)](https://github.com/DanielBash/flag-sweeper/actions/workflows/python-tests.yaml)
[![update docker image](https://github.com/DanielBash/flag-sweeper/actions/workflows/docker-deploy.yaml/badge.svg)](https://github.com/DanielBash/flag-sweeper/actions/workflows/docker-deploy.yaml)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Stars](https://img.shields.io/github/stars/DanielBash/flag-sweeper)

# Flag Sweeper

> Web resource for finding red flags in your opponents machine.

Flag Sweeper - internet resource, that can be self-hosted, for attack-defense CTF(capture the flag) competitions.
It is currently accessible on [this](https://flag-sweeper.ibashlhr.beget.tech) address.

## Local setup
### Option 1: Python virtual environment
1) Download repository
```bash
git clone https://github.com/ThreeBodyProblems/flag-sweeper.git
cd flag-sweeper
```

2) Install required packages
```bash
pip install -r requirements.txt
```

3) Run script <br/>
**Option 1.1**: Run script for debug
```bash
python main.py
```

**Option 1.2**: Run production script
```bash
gunicorn --config gunicorn_config.py main:app
```

### Option 2: Docker-container
1) Pull relevant container from docker hub:
```bash
docker pull danielbashl/flagsweeper:latest
```

2) Launch container:
```bash
docker run -d -p 8000:5000 danielbashl/flagsweeper:latest
```
