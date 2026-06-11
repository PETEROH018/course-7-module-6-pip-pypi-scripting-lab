import os
import sys

# This forces CodeGrade to see your lib folder before it runs its hidden test_file.py
student_path = "/home/codegrade/student"
lib_path = os.path.join(student_path, "lib")

if student_path not in sys.path:
    sys.path.insert(0, student_path)

if lib_path not in sys.path:
    sys.path.insert(0, lib_path)
