import schedule
import time
from send_signal import send_signal
from save_signal import save_signal
from strategies import run_all_strategies

def job():
    print("Running analysis...")
    signals = run_all_strategies()
    for signal in signals:
        save_signal(signal)
        send_signal(signal)

schedule.every(5).minutes.do(job)

if __name__ == "__main__":
    print("Bot started. Scanning every 5 minutes...")
    job()
    while True:
        schedule.run_pending()
        time.sleep(1)
