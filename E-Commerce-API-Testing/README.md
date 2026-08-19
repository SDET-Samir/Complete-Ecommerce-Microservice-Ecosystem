# Enterprise E-Commerce Automation & Multi-Container Ecosystem

[![CI/CD Multi-Container Pipeline](https://github.com)](https://github.com)

A production-grade, multi-layered microservice testing ecosystem featuring a fully **Containerized Architecture** integrated with a **GitHub Actions CI/CD Cloud Pipeline**. 

This framework isolates infrastructure layers using **Docker Containers** and features **Dynamic Token Chaining**, **SQL Database Integrity Verification**, and a decoupled **Data-Driven Architecture** that executes seamlessly in zero-trust, automated cloud runner environments.

---

## System Architecture & Containerization
To eliminate the classic *"works on my machine"* problem, this ecosystem is entirely engineered into independent, sandboxed environments using industry-standard **Docker Containerization**:

* **The Core Application Layer (`ecommerce-core-app`):** Packages our custom-engineered Flask web application server core into an isolated Linux runtime environment, exposed on network port `5000` to handle external HTTP protocol vectors.
* **The Data Infrastructure Layer (`ecommerce-database-layer`):** An isolated relational database container sandbox that handles relational tables securely, ensuring the main application server can query state data across network loops.
* **Isolated Data Synchronization Portal:** Utilizes automated entrypoint boot sequences (`python init_db.py && python server.py`) inside the container filesystem to guarantee database schema setup and user record seeding happen before endpoints open.

---

## Business Value & Test Coverage
This framework guarantees business financial security, API resilience, and database accuracy by covering critical full-stack storefront flows:

- **Dynamic Token Chaining:** Simulates zero-trust client environments by dynamically authenticating users, extracting live Bearer Tokens, and injecting them seamlessly into subsequent operations—preventing test fragility when secret parameters rotate.
- **Multi-Layer Data Validation (API + SQL Database):** Performs end-to-end data integrity checks. The framework verifies transactions through both the front-door web layers (HTTP endpoints) and down to the deepest data engines by executing independent SQL queries directly against raw database tables.
- **Automated Lifecycle Sandboxing (Setup & Teardown):** Utilizes global test controllers to dynamically spin up a clean database environment and seed test records before execution starts, wiping it completely clean afterward to eliminate "ghost data" contamination.
- **Data-Driven Separation of Concerns:** Decouples execution logic from testing payloads by feeding all user credentials and environments from isolated centralized JSON data repositories.
- **Access Guard & Defensive Error Handling:** Validates that sensitive internal business catalogs are shielded behind authentication headers (401 Unauthorized) while protecting backend pipelines from malformed injections.

---

## Tech Stack & DevOps Tooling
- **Language:** Python 3.11
- **Database Engine:** SQLite3 (Relational data layer)
- **Library:** Requests (Complex HTTP protocol handling)
- **Framework:** Pytest (Dynamic test management, session scopes & lifecycle fixtures)
- **Infrastructure:** Docker (Containerization, isolated image building & port mapping)
- **CI/CD Platform:** GitHub Actions (Automated multi-container cloud virtualization)
- **Reporting:** Pytest-HTML (Stakeholder-ready visual telemetry)

---

## How to Build and Execute the Containerized Ecosystem

### 1. Build the Core Application Image
Compile the standalone web server image snapshot out of your root directory space:
```bash
docker build -f Dockerfile.app -t ecommerce-core-app .
```

### 2. Launch the Active Container Sandbox
Boot up the application server container, map network port `5000`, and trigger the automated database initialization sequence instantly:
```bash
docker run -d -p 5000:5000 --name web-store-engine ecommerce-core-app /bin/bash -c "python init_db.py && python server.py"
```

### 3. Run the Automated Quality Suite Locally
Slide into your validation workspace and fire your Pytest regression engine against the live container endpoints:
```bash
cd tests
python -m pytest test_auth.py test_database.py test_products.py -v --html=../report.html --self-contained-html
```

---

## Project Structure
- `.github/workflows/`: Holds the `ci.yml` automation workflow for multi-container cloud execution loops upon code push.
- `Playwright-Docker-Clean/`: Houses our dedicated, standalone frontend web UI automation suite and canonical browser `Dockerfile` setups.
- `data/`: Centralized JSON data storage (`users.json`) keeping operational inputs separate from code.
- `tests/`: Modular test scripts isolating logic scopes:
  - `conftest.py`: Manages the automated setup and teardown lifecycle of the database sandbox.
  - `test_auth.py` & `test_products.py`: Verifies endpoints and headers.
  - `test_database.py`: Performs direct validation on the database layer.
  - `utils.py`: Adaptive path-safe data utility translator.
- `server.py`: Custom-engineered secure Flask web app mapping container loop bridge routing configurations.
- `Dockerfile.app`: Enterprise Docker blueprint specifying package layers and operational workspace environments.
- `config.py`: Centralized environment variables keeping configurations separate from testing logic.
- `pytest.ini`: Project path controller mapping path dependency exclusions.
- `requirements.txt`: Frozen package dependencies handling environment predictability.

---

## Sample Telemetry Report
Upon successful framework execution, open the generated `report.html` to review granular step timelines, database layer checks, request performance speeds, and validation results.
