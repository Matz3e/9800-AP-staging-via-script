# 9800-AP-staging-via-script

# Cisco Access Point Konfigurations-Skript

## Beschreibung
Dieses Python-Skript ermöglicht die Konfiguration von Cisco Access Points (APs) über SSH, basierend auf einer Excel-Datei mit Konfigurationsbefehlen.

## Voraussetzungen
- Python 3
- Die Python-Module `pandas` und `paramiko`. Sie können diese Module mit `pip` installieren:


## Verwendung
1. Legen Sie Ihre Konfigurationsbefehle in einer Excel-Datei ab. Die Excel-Datei sollte mindestens die folgenden Spalten enthalten:
 - Spalte A: Hostname des APs
 - Spalte B: MAC-Adresse des APs
 - Spalte C: Hostname2 des APs
 - Spalte D: Konfigurationsbefehl, der auf den AP angewendet werden soll


3. Das Skript wird Sie nach den folgenden Informationen fragen:
- Den Dateinamen der Excel-Datei mit den Konfigurationsbefehlen.
- Die IP-Adresse oder den Hostnamen des Cisco-Geräts.
- Ihren SSH-Benutzernamen für das Cisco-Gerät.
- Ihr SSH-Passwort für das Cisco-Gerät.

4. Das Skript wird dann eine SSH-Verbindung zum Cisco-Gerät herstellen und eine Liste der gefundenen APs ausgeben.

5. Anschließend werden die Konfigurationsbefehle für die gefundenen APs angezeigt. Sie haben die Möglichkeit, "J" (Ja), "N" (Nein) oder "Alle" auszuwählen:
- "J": Der Konfigurationsbefehl wird für den ausgewählten AP ausgeführt.
- "N": Der Konfigurationsbefehl wird nicht ausgeführt.
- "Alle": Der Konfigurationsbefehl wird für alle gefundenen APs ausgeführt.

6. Das Skript führt die ausgewählten Konfigurationsbefehle aus und zeigt die Ausgabe an.

7. Das Skript trennt die SSH-Verbindung und beendet die Ausführung.

## Beispiel
Angenommen, Sie haben eine Excel-Datei "staging.xlsx" mit den Konfigurationsbefehlen und möchten diese auf einem Cisco-Gerät mit der IP-Adresse "10.0.0.1" ausführen:

1. Führen Sie das Skript aus: python staging.py
2. Geben Sie den Dateinamen "staging.xlsx" ein.
3. Geben Sie die IP-Adresse "10.0.0.1" des Cisco-Geräts ein.
4. Geben Sie Ihren SSH-Benutzernamen und Ihr Passwort ein.
5. Wählen Sie die auszuführenden Konfigurationsbefehle aus.

Das Skript wird die ausgewählten Befehle auf den gefundenen APs ausführen.


