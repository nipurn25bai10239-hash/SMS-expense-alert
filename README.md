# SMS Expense Alert (Voice Budget Notifier)

A simple Python-based tool that simulates SMS transaction monitoring and alerts you with a **Hindi voice message** when your monthly spending crosses a predefined limit.

It uses:
- **Regular expressions (`re`)** to extract amounts from text  
- **gTTS (Google Text-to-Speech)** to generate a voice alert  
- **Pygame** to play the alert audio  

---

## Features

- Accepts transaction-like input such as:  
  - `Rs 300 to Swiggy`  
  - `INR 450 paid to Zomato`  
  - `₹500 recharge`
- Automatically extracts the **amount** from the text.
- Keeps track of **total spending** for the month.
- When spending exceeds the **monthly limit** (default: ₹5000):
  - Plays a **Hindi voice alert**:  
    > "सावधान! आप बहुत ज्यादा खर्च कर रहे हैं। कृपया अपने खर्चे कम करें।"
- Simple **command-line interface**.
- Beginner-friendly Python project demonstrating:
  - String handling  
  - Regular expressions  
  - Using external libraries (gTTS, pygame)  
  - Basic logic & condition checking  

---

## Tech Stack

- **Language**: Python 3
- **Libraries**:
  - `re` (built-in)
  - `gTTS`
  - `pygame`
  - `time` (built-in)

---

## Requirements

Make sure you have:

- Python 3.x installed
- Internet connection (required by gTTS to generate audio)

Install the required Python packages:

```bash
pip install gTTS pygame
