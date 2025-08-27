# AI Email Generator (with Ollama + Tkinter)
This project is a simple desktop application that uses **Llama 3.2 (via Ollama)** to generate professional emails.  
You provide a short request (e.g., "Write an email requesting a meeting with HR"), and the app generates both a **subject line** and a **body** for your email in a structured format.

The interface is built with **Tkinter** for a lightweight GUI, and it communicates with Ollama’s local API using **Python requests**.

---

## Features
- Simple GUI for entering prompts
- Uses Llama 3.2 model locally (via Ollama)
- Automatically formats the output into:
  - **Subject line**
  - **Email body**

---

## Installation

### 1. Install Ollama
Download and install Ollama from [https://ollama.com/](https://ollama.com/).  
Make sure it’s running locally.

### 2. Pull Llama 3.2 Model
In your terminal, run:
```bash
ollama run llama3.2
```
This will download the **Llama 3.2** model and start it for the first time.

### 3. Clone this Repository
```bash
git clone https://github.com/sarthakmasta/EmailGenerator.git
cd EmailGenerator
```

### 4. Install Python Dependencies
Make sure you have Python 3.8+ installed. Then install required libraries:
```bash
pip install requests
```
> **Note:**  
> - `tkinter` comes preinstalled with Python on most systems.  
> - `json` is part of Python’s standard library, so no installation is required.

---

## Usage
Run the app with:
```bash
python email_generator.py
```

A window will appear where you can:
1. Enter your request (e.g., "Write an email requesting a refund").
2. Click **Generate Email**.
3. View the generated subject and body in the GUI.

---

## Preview
- Input: `Request a meeting with the design team for project updates`
- Output:  
  - **Subject:** Meeting Request with Design Team – Project Updates  
  - **Body:** Dear Team, ...  

---

## Notes
- Make sure Ollama is running in the background.
- You can change the model by pulling a different model and editing `"model": "llama3.2"` in the code if you want to experiment with other models supported by Ollama.

---

## License
MIT License
