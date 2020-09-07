
# This makes the subsequent variables available to child shells
.EXPORT_ALL_VARIABLES:

include ./reflask-env.txt

# For mounting Source
REFLASK_SRC := $(PWD)/../app

##
## Usage:
##   make
##

help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build:		## Build React Flask Containers
	docker-compose -f reflask-build.yml build

network:	## Create Network, if not present
	docker network create --attachable --driver overlay reflask || true

volumes:	## Create Volumes required, if not present
	docker volume create reflask_data || true

down:		## Stop React Flask Containers
	docker-compose -f reflask-run.yml down

up:			## Bring up Flask, Service and React
up:
	TAG_NO=1 docker-compose -f reflask-run.yml up

all:		# Build and bring up
all: build network volumes up

lint:
	pylint --load-plugins pylint_flask_sqlalchemy **/*.py
