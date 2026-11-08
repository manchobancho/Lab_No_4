from pathlib import Path
from utils.statistics import find_max, find_min, calculate_evarage
from utils.reader import read_numbers
file_location = Path("data") / "measurement.txt"
a = read_numbers(file_location)

def main():
    mx = find_max(a)
    mn = find_min(a)
    evarage = calculate_evarage(a)
    print(mx, mn, evarage)
    print(a)

if __name__ == "__main__":
    main()

print("input file location: ", Path.cwd())
print("file is exist? True/False: ", file_location.exists())
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)