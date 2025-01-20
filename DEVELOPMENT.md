## DevContainer Development
Copilot assisted DevContainer setup

### Prompt
_How do I setup my machine to do local Python development? I want to use Visual Studio Code as my editor. I want to use dev containers instead of installing Python locally._

### Answer
Step 1: Install Docker
First, you'll need to install Docker on your machine. Docker is essential for running dev containers2. You can download it from the official Docker website.

Step 2: Install the Docker Extension for VS Code
Next, install the Docker extension for VS Code. Open VS Code, go to the Extensions view (Ctrl+Shift+X), search for "Docker," and install the extension authored by Microsoft1.

Step 3: Create a Python Project
If you don't have a Python project already, you can create one. For example, you can start with a simple "Hello, World!" script1.

Step 4: Add Docker Files to Your Project
Open your project folder in VS Code. Open the Command Palette (Ctrl+Shift+P) and choose Docker: Add Docker Files to Workspace. Select the appropriate app type (e.g., Python: General)1. This will create a Dockerfile and a .dockerignore file in your project.

Step 5: Create a Dev Container
To create a dev container, open the Command Palette again and select Dev Containers: Open Folder in Container. This will create a .devcontainer folder with a devcontainer.json file. You can customize this file to define the container's configuration, such as the Docker image to use and any environment variables2.

Step 6: Build and Run the Container
Once the dev container is set up, you can build and run it. Open the Command Palette and select Dev Containers: Rebuild and Run. This will build the Docker image and start the container3.

Step 7: Develop Inside the Container
With the container running, you can now develop your Python project inside it. VS Code will mount your project files into the container, and you can use all of VS Code's features, including IntelliSense, debugging, and extensions2.

1. https://code.visualstudio.com/docs/containers/quickstart-python?form=MG0AV3
2. https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&form=MG0AV3
3. https://dev.to/jajera/python-development-in-vscode-using-devcontainer-2ao1?form=MG0AV3