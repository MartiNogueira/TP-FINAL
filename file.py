from collections import Counter

# Lee el archivo de logs
with open("log.txt", "r") as file:
    logs = file.readlines()

# Contadores
ip_counter = Counter()
page_counter = Counter()
successful_accesses = 0
total_accesses = 0

# Procesa cada línea del log
for log in logs:
    parts = log.split()
    
    ip = parts[0]
    page = parts[6]
    status_code = int(parts[8])
    
    # Cuenta las visitas por IP y página
    ip_counter[ip] += 1
    page_counter[page] += 1
    
    # Cuenta accesos exitosos
    total_accesses += 1
    if status_code == 200:
        successful_accesses += 1

# Imprime resultados por consola
print("Visitas por IP:")
for ip, count in ip_counter.items():
    print(f"{ip}: {count} veces")

top_3_pages = page_counter.most_common(3)
print("\nLas 3 páginas más visitadas:")
for page, count in top_3_pages:
    print(f"{page}: {count} visitas")

success_percentage = (successful_accesses / total_accesses) * 100
print(f"\nPorcentaje de accesos exitosos (código 200): {success_percentage:.2f}%")
