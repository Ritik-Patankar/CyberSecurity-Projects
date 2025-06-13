import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(3)  # wait for scan to complete
    results = iface.scan_results()

    print("{:<30} | Signal Strength".format("SSID"))
    print("-" * 50)

    for network in results:
        ssid = network.ssid
        signal = network.signal  # closer to 0 means better signal (e.g., -30 is good, -90 is bad)
        print("{:<30} | {} dBm".format(ssid, signal))

if __name__ == "__main__":
    print("Scanning for available Wi-Fi networks...\n")
    scan_wifi()
