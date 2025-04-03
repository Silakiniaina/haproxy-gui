# HAProxy GUI Management

## Overview
The **HAProxy GUI Management** is a web application designed to simplify the management of HAProxy configurations through a user-friendly graphical interface. It provides a robust set of endpoints, routes, and services to handle HAProxy configuration data, including global and default sections, as well as dynamic generation of frontend and backend configurations. The system includes models for backend, server, and frontend entities, enabling seamless management of HAProxy load balancing setups.

This project aims to streamline HAProxy configuration management by offering a centralized solution for creating, editing, deleting, and validating configurations, with support for both RESTful API endpoints and a web interface. It is ideal for system administrators and developers looking to manage HAProxy setups efficiently.

## Features
- **HAProxy Configuration Management**:
  - Generate and manage HAProxy configurations with global and default sections.
  - Create, display, and validate HAProxy configurations via dedicated endpoints.
  - Dynamically generate frontend and backend configurations for HAProxy using a config generator service.
  - Store and manage configuration data with a dedicated storage service.
- **Backend Management**:
  - Create, edit, and delete HAProxy backend entities (e.g., backend pools for load balancing).
  - Add and manage servers within a backend, including health and status checks.
  - RESTful endpoints for backend operations (e.g., `/backend/add`, `/backend/<name>/edit`, `/backend/<name>/delete`).
- **Server Management**:
  - Add, edit, delete, and monitor the status of servers within an HAProxy backend.
  - Endpoints for server operations (e.g., `/backend/<backend_name>/server/add`, `/backend/<backend_name>/server/<server_name>/status`).
- **Frontend Management**:
  - Create, edit, and delete HAProxy frontend configurations (e.g., listeners for incoming traffic).
  - Form-based interface for adding and editing frontend entities.
  - Endpoints for frontend operations (e.g., `/frontend/add`, `/frontend/<name>/edit`, `/frontend/<name>/delete`).
- **Routing and Endpoints**:
  - Comprehensive routing for managing HAProxy backend, server, frontend, and configuration data.
  - Endpoints for configuration display and validation (e.g., `/config`, `/config/validate`, `/config/back`).
- **Web Interface**:
  - A page to list all HAProxy backend, server, and frontend configurations.
  - A page to display the current HAProxy configuration.

## Installation
Follow these steps to set up the HAProxy GUI Management project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Silakiniaina/haproxy-gui.git
   cd haproxy-gui
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: If a `requirements.txt` file is not present, you may need to install dependencies like Flask (or the framework used in `app.py`) manually:
   ```bash
   pip install flask
   ```

4. **Ensure HAProxy is Installed**:
   The application interacts with HAProxy configurations, so ensure HAProxy is installed on your system:
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install haproxy
     ```
   - On CentOS/RHEL:
     ```bash
     sudo yum install haproxy
     ```

5. **Run the Application**:
   Start the application using the main entry point (`app.py`):
   ```bash
   python app.py
   ```
   The application should now be running on `http://localhost:5000` (or the configured port).

## Usage
1. **Access the Web Interface**:
   - Open your browser and navigate to `http://localhost:5000/` to access the root endpoint.
   - Visit `/config` to view the current HAProxy configuration.
   - Use `/backend` and `/frontend` endpoints to manage HAProxy backends and frontends.

2. **Interact via API**:
   - Use tools like `curl` or Postman to interact with the API endpoints:
     - **List Configurations**: `GET /config`
     - **Validate Configuration**: `POST /config/validate`
     - **Add a Backend**: `POST /backend/add`
     - **Add a Frontend**: `POST /frontend/add`
     - **Check Server Status**: `GET /backend/<backend_name>/server/<server_name>/status`

3. **Manage HAProxy Configurations**:
   - Use the configuration generator to create HAProxy frontend and backend configs dynamically.
   - Access the listing page to view all HAProxy backend, server, and frontend configurations.
   - After making changes, apply the updated configuration to HAProxy by restarting the service:
     ```bash
     sudo systemctl restart haproxy
     ```

## Contributing
We welcome contributions to improve the HAProxy GUI Management project! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them with descriptive messages:
   ```bash
   git commit -m "feat: add new feature description"
   ```
4. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request against the `main` branch of this repository.

Please ensure your code follows the project's coding style and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Notes on the Modified README
- The project name and descriptions have been updated to reflect its purpose as an **HAProxy GUI Management** tool, focusing on HAProxy-specific terminology (e.g., backends as load balancing pools, frontends as listeners).
- The "Installation" section now includes a step to ensure HAProxy is installed, as the application likely interacts with HAProxy configurations.
- The "Usage" section includes a step to restart the HAProxy service after making configuration changes, which is a common practice when managing HAProxy setups.
- The repository URL remains a placeholder (`https://github.com/Silakiniaina/haproxy-gui.git`) and should be updated with the actual URL if available.
- The tech stack assumption (Python/Flask) remains based on the `app.py` reference in the commits. If a different stack is used, further adjustments may be needed.