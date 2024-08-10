# Define variables
PYTHON = python3
PIP = pip3
VENV = venv
PORT = 8080
OUTPUT_DIR = output
BROWSER = "Arc"
URL = http://localhost:8080
id ?= id
ip ?= 127.0.0.1
pem ?= main.pem
remote ?= /home/ubuntu
local ?= .
platform ?= ubuntu


# Define targets
.PHONY: all install clean run

# Default target to set up the environment and run the server
all: install run upload

# Install dependencies
install:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt

uninstall:
	rm -rf $(VENV)

# Clean the project
clean:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pid" -delete
	find . -type f -name "*.DS_Store" -delete
	find . -type f -name "*.log" -delete
	find . -type f -name "*.png" -delete
	find . -type f -name "log.html" -delete
	find . -type f -name "report.html" -delete
	find . -type f -name "output.xml" -delete
	find . -type d -name "__pycache__" -delete

# Run the server
run:
	mkdir -p $(OUTPUT_DIR)
	source $(VENV)/bin/activate && streamlit run main.py
	
server:
	mkdir -p $(OUTPUT_DIR)
	streamlit run main.py
	
automate:
	ansible-playbook -i ansible/inventory/main.ini ansible/main.yml

build:
	docker build -t chatty .

start:
	docker run -p 8081:8081 -d chatty 

clist:
	docker ps -a

imglist:
	docker images

clog:
	docker logs	$(id)

rm:
	docker rm	$(id)

stop:
	docker stop	$(id)

rmi:
	docker rmi	$(id)


# Upload files to remote server
upload:
	rsync -avz --exclude="*.pem" --exclude="venv" -e "ssh -i $(pem)" $(local) $(platform)@$(ip):$(remote)

# upload:
# 	rsync -avz --exclude="*.pem" --exclude="venv" -e "ssh -i  $(pem)" $(local) $(platform)@$(ip):$(remote)

# If you want to provide help or instructions
help:
	@echo "Usage: make [target] [VARIABLE=value]"
	@echo "Targets:"
	@echo "  all        - Install dependencies, run the server, and upload files"
	@echo "  install    - Set up the virtual environment and install dependencies"
	@echo "  clean      - Clean up the project"
	@echo "  run        - Run the server"
	@echo "  kill       - Kill any running twistd server"
	@echo "  server     - Run the server without virtual environment activation"
	@echo "  automate   - Run Ansible playbook"
	@echo "  build      - Build the Docker image"
	@echo "  start      - Start the Docker container"
	@echo "  clist      - List Docker containers"
	@echo "  imglist    - List Docker images"
	@echo "  clog       - View Docker container logs"
	@echo "  rm         - Remove Docker container"
	@echo "  stop       - Stop Docker container"
	@echo "  rmi        - Remove Docker image"
	@echo "  upload     - Upload files to remote server"
	@echo "  help       - Display this help message"
	@echo "Usage: make startapp APP_NAME=<app_name>"
	@echo "Example: make startapp APP_NAME=blog"

