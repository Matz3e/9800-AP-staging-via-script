import pandas as pd
import paramiko
import getpass

# Funktion zum SSH-Verbindungsaufbau
def establish_ssh_connection(hostname, username, password):
    print(f'Verbinde mit {hostname}...')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    return client

# Funktion zum Ausführen eines Befehls auf dem Cisco-Gerät
def execute_command(ssh_client, command):
    print(f'Führe Befehl aus: {command}')
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode()
    print('Befehlsausgabe:')
    print(output)
    return output

# Lese die Excel-Datei
excel_file = 'staging.xlsx'  # Bitte den Pfad zur Excel-Datei angeben
print(f'Lese Excel-Datei: {excel_file}')
df = pd.read_excel(excel_file)

# Benutzername und Passwort abfragen
cisco_host = input('Cisco Host (IP-Adresse oder Hostname): ')
cisco_username = input('Cisco SSH-Benutzername: ')
cisco_password = getpass.getpass('Cisco SSH-Passwort: ')

# Führe show ap summary aus und suche nach AP-Namen
ssh_client = establish_ssh_connection(cisco_host, cisco_username, cisco_password)
ap_summary_output = execute_command(ssh_client, 'sh ap summary')
ap_names = [line.split()[0] for line in ap_summary_output.split('\n') if line.strip().startswith("AP")]
print('Gefundene AP-Namen:')
for ap_name in ap_names:
    print(ap_name)

# Iteriere über die Zeilen der Excel-Tabelle und zeige den Konfigurationsbefehl an
for index, row in df.iterrows():
    hostname2 = row['Hostname2']
    command = row['Command']

    if hostname2 in ap_names:
        print(f'Gefundenen AP: {hostname2}')
        print(f'Konfigurationsbefehl: {command}')
        confirmation = input('Möchten Sie diese Konfiguration durchführen? (J/N): ')
        if confirmation.lower() == 'j':
            ssh_client = establish_ssh_connection(cisco_host, cisco_username, cisco_password)  # Neue SSH-Verbindung herstellen
            result = execute_command(ssh_client, command)
            ssh_client.close()  # SSH-Verbindung schließen
            print(f'Ausführung für Hostname2: {hostname2} abgeschlossen.')
        else:
            print(f'Konfiguration für {hostname2} abgebrochen.')

# Trenne die SSH-Verbindung
ssh_client.close()
print(f'SSH-Verbindung zu {cisco_host} getrennt.')
