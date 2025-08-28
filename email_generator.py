import tkinter as tk
import requests
import json

API_URL = "http://localhost:11434/api/generate"

def generate_email():
    user_prompt = prompt_entry.get().strip()
    if not user_prompt:
        return

    full_prompt = f"""
    You are an assistant that writes professional emails.
    Based on the following request, generate ONLY a subject and body.

    Request: {user_prompt}

    Format your answer strictly as:
    Subject: <your subject line here>
    Body: <your body content here>
    """

    payload = {
        "model": "llama3.2",  
        "prompt": full_prompt, 
        "stream": False
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            data = response.json()
            bot_reply = data.get("response", "").strip()

            subject = ""
            body = bot_reply
            if "Subject:" in bot_reply:
                parts = bot_reply.split("Body:")
                subject = parts[0].replace("Subject:", "").strip()
                if len(parts) > 1:
                    body = parts[1].strip()

            subject_text.delete("1.0", tk.END)
            subject_text.insert(tk.END, subject)

            body_text.delete("1.0", tk.END)
            body_text.insert(tk.END, body)

        else:
            subject_text.insert(tk.END, f"Error {response.status_code}")
            body_text.insert(tk.END, response.text)

    except Exception as e:
        subject_text.insert(tk.END, "Error")
        body_text.insert(tk.END, str(e))

root = tk.Tk()
root.title("AI Email Generator")
root.geometry("450x500")

tk.Label(root, text="Enter your request:").pack()
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=5)

tk.Button(root, text="Generate Email", command=generate_email).pack(pady=5)

tk.Label(root, text="Subject:").pack()
subject_text = tk.Text(root, height=2, width=55, wrap="word")
subject_text.pack(pady=5)

tk.Label(root, text="Body:").pack()
body_text = tk.Text(root, height=15, width=55, wrap="word")
body_text.pack(pady=5)


root.mainloop()
