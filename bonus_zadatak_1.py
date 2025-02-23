ime1 = str(input("Unesi jedno ime: ")).strip()
ime2 = str(input("Unesi jos jedno ime: ")).strip()
ime3 = str(input("Unesi jos jedno ime: ")).strip()
len(ime1)
len(ime2)
len(ime3)
if len(ime1) > len(ime2) and len(ime3):
    print(f"Najduze ime je {ime1}, ima {len(ime1)} karaktera.")



elif len(ime2) < len(ime1) and len(ime3):
    print(f"Najduze ime je {ime2}, ima {len(ime2)} karaktera.")


elif ime3 > ime1 and ime2:
    print(f"Najduze ime je {ime3}, ima {len(ime3)} karaktera.")


elif len(ime1) == len(ime2) and  len(ime1) != len(ime3):
    print(f"Najduza imena su {ime1} i {ime2}, imaju {len(ime1)} karaktera.")
elif len(ime2) == len(ime3) and len(ime2) != len(ime1):
    print(f"Najduza imena su {ime2} i {ime3}, imaju {len(ime2)} karaktera.")
elif len(ime1) == len(ime3) and len(ime1) != len(ime2):
    print(f"Najduza imena su {ime1} i {ime3}, imaju {len(ime1)} karaktera.")

elif len(ime1) == len(ime2) and len(ime3):
    print(f"Najduza imena su {ime1},{ime3} i {ime2}, imaju {len(ime1)} karaktera.")
