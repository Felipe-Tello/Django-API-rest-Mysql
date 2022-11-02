# Django-API-rest-Mysql

## Technologies used

* Python 3.9.10
* Django 4.1.2
* Django Rest Framework 3.14.0
* PyMySQL 1.0.2
* django-cors-headers 3.13.0

## Overview

|   Methods   |       URL        |       Actions      |
| ----------- |------------------|--------------------|
| POST        | api/pets/        | create new Pet     |
| GET         | api/pets/        | read all Pets      |
| GET         | api/pets/:id     | read Pets by `id`  |
| PUT         | api/pets/:id     | update Pet by `id` |
| DELETE      | api/pets/:id     | delete Pet by `id` |
| DELETE      | api/pets/        | delete all Pets    |