import unicodedata


homoglyphs = {
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x', 'і': 'i',
    'Α': 'A', 'Β': 'B', 'Ε': 'E', 'Ο': 'O', 'Ρ': 'P', 'Τ': 'T', 'Χ': 'X'
}


def get_script(char):
    try:
        name = unicodedata.name(char)        
        return name.split()[0]               
    except:
        return 'UNKNOWN'


def detect_homograph(domain):
    detected_chars = []          
    scripts_used = set()         

    for char in domain:
        script = get_script(char)
        scripts_used.add(script)

        if char in homoglyphs:
            detected_chars.append((char, homoglyphs[char]))

    has_latin = 'LATIN' in scripts_used
    has_other = any(s not in ['LATIN', 'COMMON', 'DIGIT', 'UNKNOWN'] for s in scripts_used)

    
    is_suspicious = has_latin and has_other and len(detected_chars) > 0

    return is_suspicious, detected_chars, scripts_used

print("Homograph Detection Tool ")
domain = input("Enter the domain or URL to scan: ").strip()

suspicious, chars, scripts = detect_homograph(domain)

print("\nAnalysis Result:")
print("Domain:", domain)
print("Scripts used:", scripts)

if suspicious:
    print("\n WARNING: Potential Homograph Attack Detected!")
    print("Suspicious characters:")
    for fake, real in chars:
        print(f"  → '{fake}' looks like '{real}'")
else:
    print("\nDomain looks safe — no homograph found.")
