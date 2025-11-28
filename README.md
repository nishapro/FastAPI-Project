# FastAPI Blog

A simple RESTful API for managing blogs and users, built with **FastAPI**, **SQLAlchemy**, and **SQLite** (or any SQL database). Includes authentication via JWT and user management.


## Features

- User registration and login
- JWT-based authentication
- Create, read, update, and delete blog posts
- Database integration with SQLAlchemy
- Structured project with routers and schemas
- Dockerized for easy deployment
- Unit tests included

## API Endpoints

| Endpoint     | Method | Description             |
| ------------ | ------ | ----------------------- |
| `/user/`     | GET    | List all users          |
| `/user/`     | POST   | Register a new user     |
| `/login`     | POST   | Login and get JWT token |
| `/blog/`     | GET    | Get all blog posts      |
| `/blog/`     | POST   | Create a new blog post  |
| `/blog/{id}` | GET    | Get a blog post by ID   |
| `/blog/{id}` | PUT    | Update a blog post      |
| `/blog/{id}` | DELETE | Delete a blog post      |



