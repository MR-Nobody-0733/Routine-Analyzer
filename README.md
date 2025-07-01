# Routine-Analyzer
Goal: Build a Python program that takes your sleep, study, work, and free time input, and tells you:      If your routine is balanced      If you're overworking or under-sleeping      If you're wasting too much time
Got it! You want a real-life challenge — not a boring homework — using only the basics of Python (variables, reserved words, sequence, conditionals, operators, user input, comments, data types, conversions).
⚔️ Challenge: Personal Daily Routine Analyzer

Goal: Build a Python program that takes your sleep, study, work, and free time input, and tells you:

    If your routine is balanced

    If you're overworking or under-sleeping

    If you're wasting too much time

🧠 Rules:

    Use only:

        Variables

        User input

        if / else / elif

        Comments

        Basic operators (+, -, >, <)

        Data types and conversions

    You must not use: lists, loops, functions, classes, imports

🧪 Input to Collect:

# Ask for number of hours spent on activities
sleep = float(input("How many hours did you sleep today? "))
study = float(input("How many hours did you study today? "))
work = float(input("How many hours did you work today? "))
free = float(input("How many hours did you spend on phone/TV/etc? "))

🧮 What You Have to Do:

    Calculate total hours used.

    Check if total is over 24 hours — if yes, warn the user.

    Check if:

        sleep < 6 → warn: “You didn’t sleep enough.”

        study >= 3 → good job

        free > 4 → too much screen time

        total <= 24 → print a message saying: "Good time balance" or "Needs improvement"

🧾 Sample Output:

You used 26 hours today. Time error!
You didn’t sleep enough.
You studied well. Keep it up!
You spent too much time on phone/TV.

🏁 Your Mission:

Write the code, test different values, and try to make the messages match your own real day. This will help you reflect on your habits while learning Python.
