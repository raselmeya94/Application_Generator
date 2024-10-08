# Project Deployment (Application Generator)

## Prerequisites

### Python 3.10 or Above:
This guide assumes you have Python 3.10 or a later version installed. If not, refer to the official documentation for your operating system (OS) on how to install Python. Package manager commands like `sudo apt` (Ubuntu), `curl` (generic), or `brew` (macOS) might be used.

### Package Manager (Pip):
Verify that you have either `pip` (the default package manager for Python) or `con installed. If not, installation instructions are usually available online for your specific OS.



## Creating a Project Directory and Virtual Environment


### Create a Project Directory:

1. Open your terminal or command prompt.
2. Use the `mkdir` command to create a directory for your project. For example:

    ```bash
   mkdir my_django_project
    ```
3. Navigate into the project directory:
    ```bash
   cd my_django_project
    ```

### Clone Git repository:

```bash
    git clone https://github.com/raselmeya94/Application_Generator.git
```



### Create a Virtual Environment:

1. Use the `python -m venv` command to create a virtual environment named `application_env` (replace with your desired name):

    ```bash
   python -m venv application_env
    ```
Directory Structure:
- my_django_project (local directory)
    - application_env
    - Application_Generator (git repository)
      - nothi_application_generator 
      - nothi_app_gen
      - manage.py
      - README.md
      - requirements.txt
### Activating the Virtual Environment:

#### macOS/Linux:
source llm_environment/bin/activate
Inside the project directory where located `application_env` and run the following command
    
```bash
source application_env/bin/activate
```   


Your terminal prompt will change to indicate that you're working within the virtual environment.


### Dependencies Installation:
Change directory and go to `Application Generator` Navigate into the project directory:

```bash
   cd Application Generator
```
 and run requirements.txt for installation dependencies.
```bash
    pip install -r requirements.txt
```

### Run Application Generator:
Run the following commands
```bash
python manage.py runserver 0.0.0.0:8000
```

The server will typically listen on the default port 8000. You can access your application by opening http://localhost:8000/ in your web browser.


