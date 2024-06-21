# Resource Sharing and Management
## Overview
This is a Python package for easily applying **Role Based Access Control** for Resource Sharing and Management, implementing idiomatic Python practices.

Role-based access control (RBAC) refers to the idea of assigning permissions to users based on their role within an organization. It offers a simple, manageable approach to access management that is less prone to error than assigning permissions to users individually.

In many B2B and B2C apps, users can create resources and share them with other users giving them different levels of access.
The purpose of this project is to provide a framework for implementing resource sharing and management in a scalable and secure way.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- Scalability

Due to its modular architecture, the app can be easily scaled horizontally by adding more instances of the app. As the number 
of users increases, the app can be scaled to handle the increased load. The AWS load balancer can be used to distribute the load
across multiple instances of AWS Lambda functions.

- Serverless Deployment

The app is deployed on AWS Lambda, which is a serverless computing platform. This means that the app can scale automatically to handle
Authentication and Authorization
- SSO Integration
- User Management

- ### Role Hierarchies

    Supports role hierarchies where roles can inherit permissions from other roles. This simplifies management and make the system more **flexible**. 

- ### Dynamic and Static Permissions

    Supports both ststic (predefined) and dynamic (run-time) defined permissons

- ### Context-Aware Permissions

    Supports permission being evaluated in context at run-time based on access-time and access-location.

- ### Auditing and Logging

    Implements logging for access requests, permissions granted and changes to roles and permissions. This is crusial for security audits and usage tracking.

- ### Granular Control

    Allow for fine-grained control over permissions, down to specific actions on specific resources.

- ### APIs for Management

    Secure and fully documented API for managing users, roles, permissons and resources


## Installation

Step-by-step instructions to install the project.

## Run Locally

- Clone the project.

- Go to the project directory

- Create a virtual environemt and install dependencies using requirements.txt file and virtual environemt manager of your choice (You can use venv). Creating a virtual environment is not mandantory but it is best practice.

- Create a copy of .env.example file and fill it with proper environmaental variables.

- From the root of cloned repositry run:

    ```bash
    docker-compose up -d
    ```
    ```bash
    alembic upgrade head
    ```

    ```bash
    fastapi dev main.py
    ```


## Technologies Used

- FastAPI 
- SQLAlchemy
- Alembic
- Pulumi
- AWS Lambda
- AWS API Gateway
- Logfire

