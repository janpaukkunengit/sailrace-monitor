
from notifier import notify_telegram
from datetime import datetime
from zoneinfo import ZoneInfo

def main():
    now = datetime.now(ZoneInfo("Europe/Helsinki"))
    notify_telegram(
        f"✅ TESTI: SailRace-agentti käynnistyi\n"
        f"Aika: {now.strftime('%d.%m.%Y %H:%M')}"
    )

if __name__ == "__main__":
    main()

