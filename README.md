# SI Gathering Challenge: Template


## Table of contents

- [Technologies](#technologies)
- [Components](#components)
- [Security](#security)
- [Development](#development)
- [Additional documentation](#additional-docs)

## Technologies

- [dash](https://plotly.com/dash/)  
  Dash empowers teams to build data science and ML apps that put the power of Python, R, and Julia in the hands of business users. Full-stack apps that would typically require a front end, back end, and DevOps team can now be built and deployed in hours by data scientists with Dash

- [Docker](https://www.docker.com/)  
  For hosting the web app anywhere and to run local development environments
  To quickly get up to speed with docker then run through the [Learn Docker & Containers using Interactive Browser-Based Scenarios](https://www.katacoda.com/courses/docker) at katacoda  

- [Omnia Radix](https://www.radix.equinor.com/)  
  CICD and hosting of apps in docker containers


### CICD

- [Docker](https://www.docker.com/)  
  We use multistage dockerfiles to build the images.
  `docker-compose` is used for development purposes only.

- [Omnia Radix](https://www.radix.equinor.com/)  
  CICD and hosting in the [playground](https://console.playground.radix.equinor.com/applications/gathering-leto) environment.
  Radix configuration is mainly handled in [`radixconfiguration.yaml`](../radixconfiguration.yaml)


## Components

### server 

- [**presentation**](./docs)  
  A web app produced by Dash.


## Security

- **Network**
  - _What:_ https
  - _Where:_
    - Internet facing app use TLS cert managed by Radix
    - Local dev app has no certs (http)

- **CICD**
  - _What:_ Radix Playground
  - _Where:_ https://console.playground.radix.equinor.com/applications/gathering-leto
  - _Who:_ AZ AD group [`Radix Playground Users (`4b8ec60e-714c-4a9d-8e0a-3e4cfb3c3d31`)](https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupDetailsMenuBlade/Overview/groupId/4b8ec60e-714c-4a9d-8e0a-3e4cfb3c3d31/adminUnitObjectId/)

- **Hosting**
  - _What:_ Radix Playground
  - _Where:_
    - [Production](https://gathering-leto.app.playground.radix.equinor.com/), (git branch `release`)
    - [Development](https://server-gathering-leto-development.playground.radix.equinor.com/), (git branch `master`)
  - _Who:_ See "CICD/Who"

- **Docker**
  - _What:_  Release image does not have root privilieges
  - _Where:_ 
    - [Dockerfile](./Dockerfile) , release image


## Development

### How we work

Trunk based development and a [Kanban board](https://github.com/equinor/gathering-leto/projects/2)
1. Pick an issue/feature
1. Create a feature branch and start hacking
1. When done hacking, run pull request and code review
1. If review ok then merge into master, this will kick off CICD for development in Radix



## Build and run release image

The [`./Dockerfile`](./Dockerfile) is a multistage build that will produce a minimal release image.


```sh
docker build -t gathering-leto-release .
docker run -it --rm -p 8000:8000 --name gathering-leto-release gathering-leto-release

# You should now be able to access the web app from the host computer at http://localhost:8000/
# Note that https is not available as there is no tls cert. Cert termination will be handled automatically by the host loadbalancer, in our case Radix.

# Inspect contents
docker exec -it gathering-leto-release sh
```