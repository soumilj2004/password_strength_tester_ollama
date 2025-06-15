# 🔐 Password Strength Checker with AI Analysis

A robust and intuitive desktop application built with Python and Tkinter, designed to help users assess the strength of their passwords. Beyond standard requirement checks, this tool uniquely leverages a locally hosted Large Language Model (LLM) via Ollama to provide advanced, AI-powered insights and actionable improvement tips for enhanced security.

## ✨ Features

* **Interactive GUI:** A user-friendly graphical interface built with Tkinter.
* **Real-time Requirement Check:** Instantly verifies password compliance with common security rules (length, uppercase, lowercase, numbers, special characters).
* **Dynamic Strength Bar:** A visual progress bar that updates in real-time, changing color based on the calculated strength.
* **Show/Hide Password:** Toggles visibility for convenient input.
* **AI-Powered Analysis (Ollama Integration):** Sends the entered password to a locally running Ollama LLM (e.g., Llama 2) for a nuanced strength assessment, complete with brief explanations and personalized improvement suggestions.
* **Offline Inference for Privacy:** The AI analysis runs entirely on your local machine, ensuring user privacy and eliminating cloud dependencies or associated costs.
* **Clear All Functionality:** Resets the input field and analysis results for a fresh start.

## ⚙️ Prerequisites

Before you run this application, ensure you have the following set up on your system:

1.  **Python 3.x:** Download and install from [python.org](https://www.python.org/downloads/).
2.  **Ollama:**
    * **Download & Install Ollama:** Get the installer for your operating system from the official website: [https://ollama.com/download](https://ollama.com/download)
    * **Run Ollama Server:** Open your terminal or command prompt and start the Ollama server by typing:
        ```bash
        ollama serve
        ```
    * **Pull a Model:** Download a model that the application can use (e.g., `llama2`). In your terminal, run:
        ```bash
        ollama pull llama2
        ```
        *(Note: You can use other models compatible with Ollama, just ensure the `model` variable in `get_password_strength` function in `Password_strength_checker_Ollama.py` matches the model you pull.)*

## 🚀 Installation & Setup

Follow these steps to get the project running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/soumilj2004/password_strength_tester_ollama.git](https://github.com/soumilj2004/password_strength_tester_ollama.git)
    cd password_strength_tester_ollama
    ```

2.  **Create a virtual environment (highly recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ How to Run the Application

1.  **Start the Ollama server** in a separate terminal window (if it's not already running):
    ```bash
    ollama serve
    ```
2.  **Ensure you have the required LLM pulled** (e.g., `llama2`) as mentioned in the Prerequisites.
3.  With your virtual environment activated in your project's terminal, run the main script:
    ```bash
    python Password_strength_checker_Ollama.py
    ```
    The GUI window for the Password Strength Checker should appear.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please feel free to:

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed by [Soumil Jain](https://github.com/soumilj2004)
