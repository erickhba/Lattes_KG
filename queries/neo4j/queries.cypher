#Query 1
MATCH (pesquisador:Pesquisador { Nome: "Gisele da Silva Craveiro" })-[:orienta]->(orientacao:Orientacoes)
RETURN pesquisador,  orientacao


#Query 2
MATCH (pesquisador:Pesquisador)
WHERE pesquisador.Pais IS NOT NULL
WITH pesquisador.Pais AS pais, COUNT(pesquisador) AS totalPesquisadores
RETURN pais, totalPesquisadores
ORDER BY totalPesquisadores DESC

#Query 3
MATCH (p1:Pesquisador)-[:possui_formacao]->(f1:Formacoes)
MATCH (p2:Pesquisador)-[:possui_formacao]->(f2:Formacoes)
WHERE p1 <> p2 AND f1.Instituicao = f2.Instituicao
RETURN p1, p2, f1.Instituicao AS Instituicao