import stardog

conn_details = {
  'endpoint': 'https://your_endpoint.stardog.cloud:5820',
  'username': 'user',
  'password': '***'
}
#
with stardog.Admin(**conn_details) as admin:

  with stardog.Connection('Lattes_KG', **conn_details) as conn:
    # conn.begin()
    # conn.commit()
    results = conn.select('''PREFIX : <file:Lattes_KG#>
SELECT ?orientacao
WHERE {
  ?pesquisador :Nome "Gisele da Silva Craveiro" .
  ?pesquisador :orienta ?orientacao .
}''')
    print(results)