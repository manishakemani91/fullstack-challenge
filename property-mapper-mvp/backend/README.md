<h1 align="center"> 
Property Mapper Backend
</h1>

---

# ⚒️ Techologies Used

- Alembic: For Database Migrations.
- SQLAlchemy: For ORM.
- Pydantic: For Typing or Serialization.
- Pytests: For TDD or Unit Testing.
- Docker & docker-compose : For Virtualization.
- postgresSQL: Database.
- PgAdmin: To interact with the Postgres database sessions.

# 🚀 Up and run in 5 mins 🕙
Make sure you have docker and docker-compose installed [docker installation guide](https://docs.docker.com/compose/install/)
## Step 1
create **.env** file in root folder .env
```
DATABASE_URL=postgresql+psycopg://username:password@db:5432/db
DB_USER=
DB_PASSWORD=
DB_NAME= 
PGADMIN_EMAIL=
PGADMIN_PASSWORD=
```

## Step 2
Create docker-compose.yml with containers defined(take reference of docker-compose on root level of directory) and run containers using command
```
docker-compose up
```

# 🎉 Your Production Ready FastAPI CRUD backend app is up and running on `localhost:8000`

- Swagger docs on `localhost:8000/docs`
- PgAdmin on `localhost:5050`

