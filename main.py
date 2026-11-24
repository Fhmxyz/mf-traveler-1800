import os

LINE = "Imagine every library, post office, and market stall in the world joined by a single road, so any letter you write arrives before the ink dries, and any book you seek opens in your hands."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
