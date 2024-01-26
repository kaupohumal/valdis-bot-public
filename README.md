# valdis-bot

Valdisele andsid labidaga pähe Rauno Põlluäär ja Silver Spitsõn.

## Juhised
1. Kopeeri failid serverisse path-i `/opt` peale
2. Kui pole pip installitud, siis `sudo apt install python3-pip`
3. Mine `/opt/valdis-bot-public/`
4. Seejärel installi vajalik: `pip3 install -r requirements.txt`
5. Failis `valdis.service` asenda <USER> ja <SECRET> õigete väärtustega. USER on kasutaja, mis paneb teenuse tööle. SECRET on Discord bot token
6. Kopeeri valdis.service õigesse kausta `cp valdis.service /etc/systemd/system`
7. Käivita teenus: `systemctl start valdis`