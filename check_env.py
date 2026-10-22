import sys
import importlib.util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

print("=" * 45)
print("SUSPICIOUS ACTIVITY DETECTION")
print("ENVIRONMENT CHECK")
print("=" * 45)

print("\nPython version:", sys.version)
print("Python executable:", sys.executable)
print("Project root:", PROJECT_ROOT)

packages = [
    "numpy",
    "pandas",
    "cv2",
    "torch",
    "torchvision",
    "sklearn",
    "matplotlib",
]

print("\nPackage availability:")

for package in packages:
    installed = importlib.util.find_spec(package) is not None
    status = "AVAILABLE" if installed else "MISSING"
    print(f"{package:15} : {status}")

print("\nEnvironment check completed.")