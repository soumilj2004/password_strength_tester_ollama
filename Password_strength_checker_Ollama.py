import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import json
import re


class PasswordChecker:
    def __init__(self):
        # Create main window
        self.window = tk.Tk()
        self.window.title("🔐 Password Strength Checker")
        self.window.geometry("500x600")
        self.window.configure(bg="#f0f0f0")
        self.window.resizable(False, False)

        # Title
        title_frame = tk.Frame(self.window, bg="#2c3e50", height=80)
        title_frame.pack(fill="x", pady=(0, 20))
        title_frame.pack_propagate(False)

        title_label = tk.Label(title_frame, text="🔐 Password Strength Checker",
                               font=("Arial", 18, "bold"),
                               fg="white", bg="#2c3e50")
        title_label.pack(expand=True)

        # Main content frame
        main_frame = tk.Frame(self.window, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=30)

        # Password input section
        input_frame = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=1)
        input_frame.pack(fill="x", pady=(0, 20), padx=10)

        tk.Label(input_frame, text="Enter Your Password:",
                 font=("Arial", 12, "bold"), bg="#ffffff", fg="#2c3e50").pack(pady=(15, 5))

        self.password_entry = tk.Entry(input_frame, width=35, font=("Arial", 12),
                                       show="*", relief="solid", bd=1)
        self.password_entry.pack(pady=5)

        # Show/Hide password checkbox
        self.show_password = tk.BooleanVar()
        tk.Checkbutton(input_frame, text="👁️ Show Password",
                       variable=self.show_password,
                       command=self.toggle_password,
                       bg="#ffffff", font=("Arial", 10)).pack(pady=(5, 15))

        # Check button
        tk.Button(main_frame, text="🔍 Check Strength",
                  command=self.check_password,
                  font=("Arial", 12, "bold"),
                  bg="#3498db", fg="white",
                  relief="flat", pady=8, cursor="hand2").pack(pady=10)

        # Strength bar section
        strength_frame = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=1)
        strength_frame.pack(fill="x", pady=(0, 20), padx=10)

        # Strength bar header
        strength_header = tk.Frame(strength_frame, bg="#ffffff")
        strength_header.pack(fill="x", pady=(15, 5), padx=15)

        tk.Label(strength_header, text="💪 Password Strength:",
                 font=("Arial", 11, "bold"), bg="#ffffff", fg="#2c3e50").pack(side="left")

        self.strength_percent_label = tk.Label(strength_header, text="0%",
                                               font=("Arial", 11, "bold"),
                                               bg="#ffffff", fg="#2c3e50")
        self.strength_percent_label.pack(side="right")

        # Progress bar with custom style
        style = ttk.Style()
        style.configure("Custom.Horizontal.TProgressbar",
                        background='#e74c3c', troughcolor='#ecf0f1',
                        lightcolor='#e74c3c', darkcolor='#e74c3c')

        self.progress = ttk.Progressbar(strength_frame, length=400, mode='determinate',
                                        style="Custom.Horizontal.TProgressbar")
        self.progress.pack(pady=(5, 15), padx=15)

        # Password requirements checklist
        requirements_frame = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=1)
        requirements_frame.pack(fill="x", pady=(0, 20), padx=10)

        tk.Label(requirements_frame, text="📋 Password Requirements:",
                 font=("Arial", 12, "bold"), bg="#ffffff", fg="#2c3e50").pack(anchor="w",
                                                                              pady=(15, 10), padx=15)

        # Requirements list
        req_list_frame = tk.Frame(requirements_frame, bg="#ffffff")
        req_list_frame.pack(fill="x", padx=20, pady=(0, 15))

        self.req_uppercase = tk.Label(req_list_frame, text="❌ Has uppercase letters",
                                      font=("Arial", 10), fg="#e74c3c", bg="#ffffff")
        self.req_uppercase.pack(anchor="w", pady=2)

        self.req_lowercase = tk.Label(req_list_frame, text="❌ Has lowercase letters",
                                      font=("Arial", 10), fg="#e74c3c", bg="#ffffff")
        self.req_lowercase.pack(anchor="w", pady=2)

        self.req_numbers = tk.Label(req_list_frame, text="❌ Has numbers",
                                    font=("Arial", 10), fg="#e74c3c", bg="#ffffff")
        self.req_numbers.pack(anchor="w", pady=2)

        self.req_special = tk.Label(req_list_frame, text="❌ Has special characters",
                                    font=("Arial", 10), fg="#e74c3c", bg="#ffffff")
        self.req_special.pack(anchor="w", pady=2)

        self.req_length = tk.Label(req_list_frame, text="❌ At least 8 characters",
                                   font=("Arial", 10), fg="#e74c3c", bg="#ffffff")
        self.req_length.pack(anchor="w", pady=2)

        # Result display
        result_frame = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=1)
        result_frame.pack(fill="x", pady=(0, 20), padx=10)

        tk.Label(result_frame, text="🤖 AI Analysis:",
                 font=("Arial", 12, "bold"), bg="#ffffff", fg="#2c3e50").pack(anchor="w",
                                                                              pady=(15, 5), padx=15)

        self.result_label = tk.Label(result_frame, text="Click 'Check Strength' to analyze your password",
                                     font=("Arial", 10),
                                     wraplength=400,
                                     justify="left", bg="#ffffff", fg="#7f8c8d")
        self.result_label.pack(pady=(5, 15), padx=15, anchor="w")

        # Buttons frame
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(fill="x", pady=10)

        tk.Button(button_frame, text="🗑️ Clear All",
                  command=self.clear_all,
                  font=("Arial", 10), bg="#e67e22", fg="white",
                  relief="flat", cursor="hand2").pack(side="right", padx=5)

    def update_progress_bar_color(self, percentage):
        """Update progress bar color based on strength percentage"""
        style = ttk.Style()

        if percentage < 33:
            # Red for weak
            style.configure("Custom.Horizontal.TProgressbar",
                            background='#e74c3c', troughcolor='#ecf0f1',
                            lightcolor='#e74c3c', darkcolor='#c0392b')
        elif percentage < 66:
            # Yellow/Orange for medium
            style.configure("Custom.Horizontal.TProgressbar",
                            background='#f39c12', troughcolor='#ecf0f1',
                            lightcolor='#f39c12', darkcolor='#e67e22')
        else:
            # Green for strong
            style.configure("Custom.Horizontal.TProgressbar",
                            background='#27ae60', troughcolor='#ecf0f1',
                            lightcolor='#27ae60', darkcolor='#229954')

    def check_password_requirements(self, password):
        """Check and update password requirements display"""
        # Check uppercase
        has_upper = bool(re.search(r'[A-Z]', password))
        self.req_uppercase.config(
            text="✅ Has uppercase letters" if has_upper else "❌ Has uppercase letters",
            fg="#27ae60" if has_upper else "#e74c3c"
        )

        # Check lowercase
        has_lower = bool(re.search(r'[a-z]', password))
        self.req_lowercase.config(
            text="✅ Has lowercase letters" if has_lower else "❌ Has lowercase letters",
            fg="#27ae60" if has_lower else "#e74c3c"
        )

        # Check numbers
        has_numbers = bool(re.search(r'[0-9]', password))
        self.req_numbers.config(
            text="✅ Has numbers" if has_numbers else "❌ Has numbers",
            fg="#27ae60" if has_numbers else "#e74c3c"
        )

        # Check special characters
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        self.req_special.config(
            text="✅ Has special characters" if has_special else "❌ Has special characters",
            fg="#27ae60" if has_special else "#e74c3c"
        )

        # Check length
        has_length = len(password) >= 8
        self.req_length.config(
            text="✅ At least 8 characters" if has_length else "❌ At least 8 characters",
            fg="#27ae60" if has_length else "#e74c3c"
        )

        # Calculate strength percentage
        score = sum([has_upper, has_lower, has_numbers, has_special, has_length])
        strength_percent = (score / 5) * 100

        # Update progress bar
        self.progress['value'] = strength_percent
        self.strength_percent_label.config(text=f"{strength_percent:.0f}%")

        # Update progress bar color
        self.update_progress_bar_color(strength_percent)

        return score

    def toggle_password(self):
        """Show or hide password"""
        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def check_password(self):
        """Check password strength using Ollama"""
        password = self.password_entry.get()

        if not password:
            messagebox.showwarning("Warning", "Please enter a password!")
            return

        # Update requirements checklist immediately
        score = self.check_password_requirements(password)

        # Show loading message
        self.result_label.config(text="🔄 Analyzing password strength...", fg="#3498db")
        self.window.update()

        try:
            # Call Ollama API
            strength = self.get_password_strength(password)

            # Display result with color
            if "weak" in strength.lower():
                color = "#e74c3c"
                emoji = "🔴"
            elif "medium" in strength.lower() or "moderate" in strength.lower():
                color = "#f39c12"
                emoji = "🟡"
            elif "strong" in strength.lower():
                color = "#27ae60"
                emoji = "🟢"
            else:
                color = "#2c3e50"
                emoji = "🔍"

            self.result_label.config(text=f"{emoji} {strength}", fg=color)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to check password: {str(e)}")
            self.result_label.config(text="❌ Error checking password", fg="#e74c3c")

    def get_password_strength(self, password):
        """Call Ollama to check password strength"""
        prompt = f"""Analyze this password strength: {password}

Rate it as:
- WEAK (too short, common, predictable)
- MEDIUM (decent but could be better)  
- STRONG (excellent security)

Provide a brief explanation and 1-2 tips to improve it.
Keep response under 100 words."""

        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama2",  # Change to your preferred model
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                return result["response"].strip()
            else:
                return f"Error: Ollama returned status {response.status_code}"

        except requests.exceptions.ConnectionError:
            return "Error: Cannot connect to Ollama. Make sure it's running (ollama serve)"
        except requests.exceptions.Timeout:
            return "Error: Request timed out. Try again."
        except Exception as e:
            return f"Error: {str(e)}"

    def clear_all(self):
        """Clear password and result"""
        self.password_entry.delete(0, tk.END)
        self.result_label.config(text="Click 'Check Strength' to analyze your password", fg="#7f8c8d")
        self.progress['value'] = 0
        self.strength_percent_label.config(text="0%")

        # Reset progress bar color to red
        self.update_progress_bar_color(0)

        # Reset all requirement labels
        requirements = [self.req_uppercase, self.req_lowercase, self.req_numbers,
                        self.req_special, self.req_length]
        texts = ["❌ Has uppercase letters", "❌ Has lowercase letters", "❌ Has numbers",
                 "❌ Has special characters", "❌ At least 8 characters"]

        for req_label, text in zip(requirements, texts):
            req_label.config(text=text, fg="#e74c3c")

    def run(self):
        """Start the GUI"""
        self.window.mainloop()


# Run the application
if __name__ == "__main__":
    # Check if Ollama is available
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code != 200:
            print("Warning: Ollama might not be running properly")
    except:
        print("Error: Cannot connect to Ollama!")
        print("Please make sure Ollama is running:")
        print("1. Install Ollama")
        print("2. Run: ollama serve")
        print("3. Run: ollama pull llama2")

    app = PasswordChecker()
    app.run()