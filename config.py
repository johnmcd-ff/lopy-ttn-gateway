""" LoPy LoRaWAN Nano Gateway configuration options """

# replace with with your id i.e. 11aa334455bb7788

GATEWAY_ID = 'YOUR_GATEWAY_ID'

SERVER = 'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'YOUR_SSID_HERE'
WIFI_PASS = 'YOUR_PASSWORD_HERE'

LORA_FREQUENCY = 868100000
LORA_DR = "SF7BW125"   # DR_5
