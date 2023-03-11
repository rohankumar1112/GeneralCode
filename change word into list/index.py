with open('listof_cybersecurity_data.txt', 'r') as f:

  # Read all the lines and split them into words
  words = f.read().split()

  # Print the list of words
  print(words)
  

# list =['Firewall', 'Antivirus', 'Malware', 'Virus', 'Phishing', 'Spam', 'Cybercrime', 'Cyberattack', 'Encryption', 'Decryption', 'Hacking', 'Identity', 'theft', 'Vulnerability', 'Authentication', 'Authorization', 'Intrusion', 'detection', 'Intrusion', 'prevention', 'Penetration', 'testing', 'Ransomware', 'Social', 'engineering', 'Two-factor', 'authentication', 'Virtual', 'private', 'network', '(VPN)', 'Zero-day', 'vulnerability', 'Botnet', 'Denial', 'of', 'service', '(DoS)', 'Distributed', 'denial', 'of', 'service', '(DDoS)', 'Access', 'control', 'Adware', 'Application', 'security', 'Backdoor', 'Biometric', 'authentication', 'Brute', 'force', 'attack', 'Buffer', 'overflow', 'Certificate', 'authority', '(CA)', 'Command', 'and', 'control', '(C&C)', 'Cryptography', 'Cyber', 'espionage', 'Data', 'breach', 'Exploit', 'Firewall', 'rule', 'Hash', 'function', 'Incident', 'response', 'Keylogger', 'Logic', 'bomb', 'Man-in-the-middle', '(MitM)', 'attack', 'Network', 'security', 'Password', 'cracking', 'Patch', 'Payload', 'Port', 'scanning', 'Rootkit', 'Security', 'audit', 'Social', 'media', 'security', 'Spoofing', 'Trojan', 'horse', 'Web', 'application', 'firewall', '(WAF)', 'Worm', 'Anomaly', 'detection', 'Bot', 'Cipher', 'Cross-site', 'scripting', '(XSS)', 'Cyber', 'espionage', 'Data', 'exfiltration', 'Digital', 'certificate', 'DNS', 'poisoning', 'Exploit', 'kit', 'Fileless', 'malware', 'Grayware', 'Honeypot', 'Injection', 'attack', 'Internet', 'of', 'Things', '(IoT)', 'security', 'Kerberos', 'Logic', 'bomb', 'Network', 'address', 'translation', '(NAT)', 'Obfuscation', 'Packet', 'sniffing', 'Phishing', 'kit', 'Port', 'knocking', 'Red', 'team', 'SQL', 'injection', 'Threat', 'intelligence', 'User', 'account', 'control', '(UAC)', 'Virtualization', 'Watering', 'hole', 'attack', 'XSS', 'payload', 'Zero', 'trust', 'Advanced', 'Persistent', 'Threat', '(APT)', 'Blacklist', 'Cloud', 'security', 'Cybersecurity', 'hygiene', 'Deep', 'Packet', 'Inspection', '(DPI)', 'Encryption', 'key', 'File', 'integrity', 'monitoring', '(FIM)', 'Grey', 'hat', 'hacker', 'HTTPS', 'Information', 'security', 'Jailbreaking', 'Key', 'exchange', 'Least', 'privilege', 'Malvertising', 'Network', 'segmentation', 'Open', 'Web', 'Application', 'Security', 'Project', '(OWASP)', 'Privileged', 'access', 'management', '(PAM)', 'Quantum', 'computing', 'Ransomware-as-a-Service', '(RaaS)', 'Session', 'hijacking', 'Threat', 'modeling', 'USB', 'security', 'Virtual', 'Private', 'Cloud', '(VPC)', 'Web', 'filtering', 'XML', 'external', 'entity', '(XXE)', 'attack', 'Yara', 'rules', 'Zombie', 'Authenticator', 'app', 'Behavior-based', 'detection', 'Computer', 'Emergency', 'Response', 'Team', '(CERT)', 'Data', 'loss', 'prevention', '(DLP)', 'Endpoint', 'security', 'Firewall', 'rule', 'set', 'Greyware', 'Hardening', 'Information', 'assurance', 'JavaScript', 'hijacking', 'Kernel', 'Least', 'privilege', 'principle', 'Multi-factor', 'authentication', '(MFA)', 'Network', 'Access', 'Control', '(NAC)', 'Online', 'Privacy', 'Protection', 'Act', '(OPPA)', 'Packet', 'filtering', 'Risk', 'assessment', 'Security', 'Operations', 'Center', '(SOC)', 'Tokenization', 'User', 'and', 'Entity', 'Behavior', 'Analytics', '(UEBA)', 'Vulnerability', 'scanner', 'Web', 'application', 'penetration', 'testing', 'XML', 'encryption', 'Zero-day', 'attack', 'Anti-virus', 'software', 'Bots', 'and', 'botnets', 'Certificate', 'revocation', 'list', '(CRL)', 'Cyberbullying', 'DDoS', 'attack', 'Advanced', 'Encryption', 'Standard', '(AES)', 'Business', 'Continuity', 'Planning', '(BCP)', 'Command', 'injection', 'Data', 'classification', 'Encryption', 'algorithm', 'Firewall', 'policy', 'Hashing', 'Information', 'security', 'management', 'system', '(ISMS)', 'Java', 'applet', 'Kerberos', 'authentication', 'protocol', 'Least', 'common', 'mechanism', 'Mobile', 'device', 'management', '(MDM)', 'Network', 'forensics', 'Online', 'fraud', 'Personal', 'Identifiable', 'Information', '(PII)', 'Quantum', 'key', 'distribution', 'Remote', 'access', 'Security', 'Information', 'and', 'Event', 'Management', '(SIEM)', 'Transport', 'Layer', 'Security', '(TLS)', 'Virtual', 'Private', 'Network', '(VPN)', 'tunneling', 'Web', 'application', 'firewall', '(WAF)', 'log', 'X.509', 'certificate', 'Zero-day', 'vulnerability', 'exploit', 'Botmaster', 'Cybersecurity', 'insurance', 'DNS', 'spoofing', 'Email', 'spoofing', 'Firewall', 'log', 'analysis', 'Access', 'control', 'Advanced', 'Encryption', 'Standard', '(AES)', 'Advanced', 'Persistent', 'Threat', '(APT)', 'Anomaly', 'detection', 'Anti-virus', 'software', 'Application', 'security', 'Authentication', 'Authenticator', 'app', 'Backdoor', 'Behavior-based', 'detection', 'Biometric', 'authentication', 'Blacklist', 'Bot', 'Botmaster', 'Botnet', 'Brute', 'force', 'attack', 'Buffer', 'overflow', 'Business', 'Continuity', 'Planning', '(BCP)', 'Certificate', 'authority', '(CA)', 'Certificate', 'revocation', 'list', '(CRL)', 'Cipher', 'Cloud', 'security', 'Command', 'and', 'control', '(C&C)', 'Command', 'injection', 'Computer', 'Emergency', 'Response', 'Team', '(CERT)', 'Cryptography', 'Cyber', 'espionage', 'Cyberbullying', 'Cybersecurity', 'hygiene', 'Cybersecurity', 'insurance', 'Data', 'breach', 'Data', 'classification', 'Data', 'exfiltration', 'Data', 'loss', 'prevention', '(DLP)', 'Deep', 'Packet', 'Inspection', '(DPI)', 'Digital', 'certificate', 'DNS', 'poisoning', 'DNS', 'spoofing', 'DDoS', 'attack', 'Email', 'spoofing', 'Encryption', 'algorithm', 'Encryption', 'key', 'Endpoint', 'security', 'Exploit', 'Exploit', 'kit', 'File', 'integrity', 'monitoring', '(FIM)', 'Fileless', 'malware', 'Firewall', 'log', 'analysis', 'Firewall', 'policy', 'Firewall', 'rule', 'Firewall', 'rule', 'set', 'Grayware', 'Grey', 'hat', 'hacker', 'Honeypot', 'HTTPS', 'Information', 'assurance', 'Information', 'security', 'Information', 'security', 'management', 'system', '(ISMS)', 'Injection', 'attack', 'Internet', 'of', 'Things', '(IoT)', 'security', 'Jailbreaking', 'Java', 'applet', 'JavaScript', 'hijacking', 'Kerberos', 'Kerberos', 'authentication', 'protocol', 'Kernel', 'Key', 'exchange', 'Keylogger', 'Least', 'common', 'mechanism', 'Least', 'privilege', 'Logic', 'bomb', 'Malvertising', 'Man-in-the-middle', '(MitM)', 'attack', 'Mobile', 'device', 'management', '(MDM)', 'Multi-factor', 'authentication', '(MFA)', 'NAT', 'Network', 'Access', 'Control', '(NAC)', 'Network', 'forensics', 'Network', 'security', 'Obfuscation', 'Online', 'fraud', 'Online', 'Privacy', 'Protection', 'Act', '(OPPA)', 'Packet', 'filtering', 'Packet', 'sniffing', 'Password', 'cracking', 'Patch', 'Payload', 'Personal', 'Identifiable', 'Information', '(PII)', 'Phishing', 'kit', 'Port', 'knocking', 'Port', 'scanning', 'Privileged', 'access', 'management', '(PAM)', 'Quantum', 'computing', 'Quantum', 'key', 'distribution', 'Ransomware-as-a-Service', '(RaaS)', 'Red', 'team', 'Remote', 'access', 'Risk', 'assessment', 'Rootkit', 'Security', 'audit', 'Security', 'Information', 'and', 'Event', 'Management', '(SIEM)', 'Session', 'hijacking', 'Social', 'media', 'security', 'SQL', 'injection', 'Threat', 'intelligence', 'Threat', 'modeling', 'Tokenization', 'Transport', 'Layer', 'Security', '(TLS)', 'Trojans', 'Trojan', 'horse', 'USB', 'security', 'User', 'account', 'control', '(UAC)', 'User', 'and', 'Entity', 'Behavior', 'Analytics', '(UEBA)', 'Virtual', 'Private', 'Cloud', '(VPC)', 'Virtual', 'Private', 'Network', '(VPN)', 'tunneling', 'Vulnerability', 'scanner', 'Watering', 'hole', 'attack', 'Web', 'application', 'firewall', '(WAF)', 'Web', 'application', 'firewall', '(WAF)', 'log', 'Web', 'application', 'penetration', 'testing', 'Web', 'filtering', 'Worm', 'X.509', 'certificate', 'XML', 'encryption', 'XML', 'external', 'entity', '(XXE)', 'attack', 'XSS', 'payload', 'Zero', 'trust', 'Zero-day', 'attack', 'Zero-day', 'vulnerability', 'exploit', 'Zombie', 'Yara', 'rules']  