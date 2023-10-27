from data import stock_data, greeting
import subprocess

greeting()
stock_data()

subprocess.call(['notepad.exe', 'analysis_results.txt'])

