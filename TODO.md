## AgileDocs (TBA) - App for project management
TODO list for the project.

### Todo 
-------

- [ ] Implement LLM agents to ask questions about the workspace.
  - [ ] Global questions.
  - [ ] Ask about specific folders, information retrieval.
  - [ ] Generate documentation from files (code, documents, etc.)
  - [ ] ...
- [ ] Dockerize application, prepare migrations scripts, etc.

### In Progress
-------

- [ ] Prepare a basic front-end for the application.
  - [X] Login screen.
  - [X] Prepare vue.js templates, design application flow.
  - [ ] Integrate backend with the frontend (JWT authentication, etc.).
  - [ ] Page with user's repositories.
  - [ ] Visualize the documents in the repository, allow for uploads, etc.
  - [ ] Implementation of version-control operations with the backend.

### Done (✓)
-------

- [X] Create the repository.
- [X] Work on the repository's structrure.
- [X] Prepare the backend code for the application.
  - [X] Prepare an API with basic auth.
  - [X] Prepare models for the DB (minimal, for prototyping).
  - [X] Repository creation, basic adding and committing.
  - [X] Initialize Alembic for migration scripts and generating the DB.
  - [X] CRUD operations with the database.
  - [X] Move from local fake db to PostgreSQL.
