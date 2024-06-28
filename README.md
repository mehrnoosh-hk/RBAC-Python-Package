# Idiomic Python Role-Based Access Control Package

[![codecov](https://codecov.io/gh/mehrnoosh-hk/RBAC-Python-Package/graph/badge.svg?token=9W1GJHROZQ)](https://codecov.io/gh/mehrnoosh-hk/RBAC-Python-Package)


Overview

This Python package facilitates the implementation of Role-Based Access Control (RBAC) for resource sharing and management, following idiomatic Python practices.

Role-Based Access Control (RBAC) assigns permissions to users based on their roles within an organization. This approach simplifies access management and reduces the risk of errors compared to assigning permissions to users individually.

In numerous B2B (Business-to-Business) and B2C (Business-to-Consumer) applications, users often need the capability to create and manage resources, such as documents, projects, or datasets, and share them with others while specifying varying levels of access. For example, in a project management tool, users might create projects and assign different roles to team members with specific access levels. Typical roles might include:

- Viewer: Can only view project details and progress without making any changes.
- Editor: Can view and edit project details, add or update tasks, and collaborate with other team members.
- Administrator: Has full control over the project, including the ability to assign roles, manage team members, and configure project settings.

This project aims to provide a robust, scalable, and secure framework to implement such resource sharing and access management, ensuring that each user has the appropriate permissions based on their role. By using this framework, developers can easily integrate role-based access control into their applications, enhancing both security and usability.



Key Features

- Idiomatic Python: Leverages Python's best practices for clean and maintainable code.
- Scalable Design: Suitable for applications of all sizes, from small startups to large enterprises.
- Secure: Implements robust security measures to protect your resources and data.
- Flexible Role Management: Easily define and manage roles and permissions to suit your organizational needs.
- Easy Integration: Seamlessly integrate with existing Python applications and frameworks.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- ### Scalability

    Due to its modular architecture, the app can be easily scaled horizontally by adding more instances of the app. As the number 
    of users increases, the app can be scaled to handle the increased load. The AWS load balancer can be used to distribute the load
    across multiple instances of AWS Lambda functions.

- ### Serverless Deployment

    The app is deployed on AWS Lambda, which is a serverless computing platform. This means that the app can scale automatically to handle
    Authentication and Authorization
- ### SSO Integration
- ### User Management

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

## Run Locally for Development

- Clone the project.

- Go to the project directory

- Create a virtual environemt and install dependencies using requirements.txt file and virtual environemt manager of your choice (You can use venv). Creating a virtual environment is not mandantory but it is best practice.

- Create a copy of .env.example file and fill it with proper environmaental variables.

- From the root of cloned repositry run:

    ```bash
    docker-compose up -d
    alembic upgrade head
    fastapi dev main.py
    ```

## How to Use

The main idea of this package is to make RBAC as simple as possible. To control resources access based on the role it is enough to decorate your function with Python decorator.

A resource can be anything from a shared file, a password or an AWS Lambda instance.

```python
from rbac_package import has_role


@has_role['lambda_user', 'lambda_admin']
def run_aws_lambda(instance_id: str) -> None:
    # code to run lambda instance


@has_role['lambda_admin']
def delete_aws_lambda(instance_id: str) -> None:
    # code to delete lamabda instance

```



## Technologies Used

- FastAPI 
- SQLAlchemy
- Alembic
- Pulumi
- AWS Lambda
- AWS API Gateway
- Logfire

