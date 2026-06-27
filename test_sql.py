import sqlite3

conn = sqlite3.connect('netflix.db')
cursor = conn.cursor()

with open('sql/netflix_retention_queries.sql', 'r') as f:
    content = f.read()

# Remove comment lines
lines = [l for l in content.splitlines() if not l.strip().startswith('--')]
clean_sql = '\n'.join(lines)

# Split by semicolon
queries = [q.strip() for q in clean_sql.split(';') if q.strip()]

print(f'Found {len(queries)} queries')

for i, q in enumerate(queries, 1):
    try:
        cursor.execute(q)
        print(f'Query {i}: OK')
    except Exception as e:
        print(f'Query {i}: ERROR - {e}')

conn.close()