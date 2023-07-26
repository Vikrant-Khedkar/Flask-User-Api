
# Dockerized-Flask User API


https://github.com/Vikrant-Khedkar/Flask-User-Api/assets/64966091/5aea4824-50c2-4983-86ba-1d582369a3f2


Simple Flask App to perform CRUD on User API


## API Reference

#### Get all users

```http
  GET /users
```


#### Get user by id

```http
  GET /users/id
```
#### Create a user

```http
  POST /users/
```
#### Update a user

```http
  PUT /users/id
```
#### Delete a user

```http
  DELETE /users/id
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `userid`      | `string` | **Required**. Id of user |
| `name`      | `string` | **Required**. name of user |
| `email`      | `string` | **Required**. email of user |
| `password`      | `string` | **Required**. password of user |





## Run Locally

Clone the project

```bash
  git clone https://github.com/Vikrant-Khedkar/Flask-User-Api
```

Go to the project directory

```bash
  cd my-project
```

Build Docker image for app.py

```bash
  docker build -t user-api .
```
Build Docker image for Mongo

```bash
  cd MongoDocker
  docker build -t my-mongo .
```


Run the Mongo container
```bash
  docker run -d --name my-mongo-container -p 27017:27017 my-mongo
```
Run the user-api container

```bash
docker run -p 5000:5000 --link my-mongo-container:db user-api
```
Done now app will be running on 
```bash
http://localhost:5000
```

## Screenshots

### Get all users
![image](https://github.com/Vikrant-Khedkar/Flask-User-Api/assets/64966091/8ae9a9ab-8ae7-44c1-ba84-23240be3bdad)
### Get a user by id
![image](https://github.com/Vikrant-Khedkar/Flask-User-Api/assets/64966091/4bed2728-cf4e-42cb-abfe-17ef6b2d7041)
### Post a user
![image](https://github.com/Vikrant-Khedkar/Flask-User-Api/assets/64966091/1134ac5b-e268-48a8-964f-f657a96dc4ad)
### PUT a user(update)
![image](https://github.com/Vikrant-Khedkar/Flask-User-Api/assets/64966091/0f4dcbef-109c-4b16-92b0-b79637756c9e)

![image](https://github.com/Vikrant-Khedkar/Flask-User-Api/assets/64966091/3abf0cff-2210-49d1-801f-0f1b5e5dc092)
### Delete a user
![image](https://github.com/Vikrant-Khedkar/Flask-User-Api/assets/64966091/03ce3591-e793-48c8-bc5e-3f39f6b075fd)








