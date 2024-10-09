# Clipboard Manager

The Clipboard Manager is a Python application that stores and manages clipboard history. It allows you to easily access and paste previously copied items from a history list.

---

## Features

- Capture and store clipboard history.
- Select an item from the history to copy and paste it.
- Simple UI built with Tkinter.

---

## Installation and Setup

### Prerequisites

Make sure you have Python 3.x installed on your system. You can check this by running the following command in your terminal:

```bash
python3 --version
```

---


### Clone the repository 

```bash
git clone https://github.com/your-username/clipboard-manager.git
cd clipboard-manager
```

---

### Step 2: Create and Activate Virtual Environment

#### macOS/Linux:

1. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate
    ```

#### Windows:

1. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment:**

    ```bash
    venv\Scripts\activate
    ```

---

### Step 3: Install Dependencies

After activating the virtual environment, install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### Step 4: Run the Application 

To start the clipboard manager, run the following command:

```bash
python3 main.py
```
This will launch the clipboard window

---

## Adding or Updateing Dependencies

To add new packages or update existing ones:

1.**Install a new package:**
```bash
pip install <package-name>
```
2.**Update the requirements.txt file:**
```bash
pip freeze > requirements.txt
```

---

## Troubleshooting 

- **Clipboard access:** If you experience issues with clipboard access on macOS, you may need to grant permission to the application.
- **Tkinter not installed:** If the Tkinter library is not installed, you can install it with your package manager (e.g., ```bash brew install python-tk``` on macOS).


