## AgileDocs (TBA) - App for project management
This is an MVP for an application that uses version-control technology alongside new technologies (LLMs) in order to help with project management. The objective of this project is to provide everyone in the team a single environment in which they can have all the files they consider relevant to a project, and using the help of LLMs in order to facilitate the creation of documentation.

Documentation should never be something that is left undone, but the fast pace at which Agile development moves often leaves projects without any documentation. The objective of this project is to aid with that.

### 1. Requirements
------
- Python 3.12
- npm installed

### 2. How to run the environment:
------
1. Initialize a Python environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Prepare your PostgreSQL database with the Alembic scripts.
4. Prepare a .venv file with your database information.
5. Run the python script through `uvicorn src.backend.app.main:app --host 0.0.0.0 --port {{whatever port}}`
6. Deploy the frontend through `npm run dev` in the `src/frontend` folder.
