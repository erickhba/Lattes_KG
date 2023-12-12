from owlready2 import get_ontology, DataProperty, ObjectProperty, Thing
import pandas as pd
import datetime 

#path on linux
#owl_path = "file:///home/erick_albuquerque/Documents/TCC/Lattes_KG/OWL/ontology.owl"

#path on windows
owl_path = "file://C:\\Users\\User\\Documents\\Faculdade\\Lattes_KG\\OWL\\ontology.owl"

onto = get_ontology(owl_path).load()


#PREFIX Linux = '/home/erick_albuquerque/Documents/TCC/dados'
PREFIX = 'C:\\Users\\User\\Documents\\Faculdade\\TCC\\dados'


# all entities classes, object properties/relations, and data properties are defined within same namespace,
# so these objects of knowledge graph can be managed within same scope.
with onto:
    
    # classes
    class Pesquisador(Thing):
        pass

    class AreasAtuacao(Thing):
        pass

    class Atuacoes(Thing):
        pass
    
    class Orientacoes(Thing):
        pass
 
    class Formacoes(Thing):
        pass

    # Data properties
    class LattesId(DataProperty):
        domain = [Pesquisador, AreasAtuacao, Atuacoes, Orientacoes]
        range = [str]

    class Nome(DataProperty):
        domain = [Pesquisador, Orientacoes]
        range = [str]

    class Cidade(DataProperty):
        domain = [Pesquisador]
        range = [str]

    class Estado(DataProperty):
        domain = [Pesquisador]
        range = [str]

    class Pais(DataProperty):
        domain = [Pesquisador]
        range = [str]

    class Nacionalidade(DataProperty):
        domain = [Pesquisador]
        range = [str]

    class GrandeArea(DataProperty):
        domain = [Pesquisador]
        range = [str]

    class Area(DataProperty):
        domain = [Pesquisador]
        range = [str]

    class SubArea(DataProperty):
        domain = [Pesquisador]
        range = [str]

    class Especialidade(DataProperty):
        domain = [Pesquisador]
        range = [str]
    

    class Instituicao(DataProperty):
        domain = [Atuacoes, Orientacoes, Formacoes]
        range = [str]
    
    class Titulo(DataProperty):
        domain = [Pesquisador]
        range = [str]

    class TipoTrabalho(DataProperty):
        domain = [Orientacoes]
        range = [str]

    class StatusOrientacao(DataProperty):
        domain = [Orientacoes]
        range = [str]
    
    class Ano(DataProperty):
        domain = [Orientacoes]
        range = [datetime.datetime]

    class AnoInicio(DataProperty):
        domain = [Formacoes]
        range = [datetime.datetime]

    class AnoFim(DataProperty):
        domain = [Formacoes]
        range = [datetime.datetime]
    

# Object properties
    class areas_relacionadas(ObjectProperty):
        domain = [Pesquisador]
        range = [AreasAtuacao]

    class atua_em(ObjectProperty):
        domain = [Pesquisador]
        range = [Atuacoes]

    class orienta(ObjectProperty):
        domain = [Pesquisador]
        range = [Orientacoes]
    
    class possui_formacao(ObjectProperty):
        domain = [Pesquisador]
        range = [Formacoes]




# Generating individuals
    def gera_curriculo():
        df = pd.read_csv(f'{PREFIX}/gerais1.txt', sep="\t", header=None, encoding='ISO-8859-1')
        df.columns = ['id', 'nome', 'doc1', 'doc2', 'Cidade', 'Estado', 'Pais','Nacionalidade', 'unknow']
        df.id = df.id.astype('string')
       
        for ind in df.index:
            obj = Pesquisador(name=df['nome'][ind])
            obj.LattesId.append(df['id'][ind])
            obj.Nome.append(df['nome'][ind])
            obj.Cidade.append(df['Cidade'][ind])
            obj.Pais.append(df['Pais'][ind])
            obj.Nacionalidade.append(df['Nacionalidade'][ind])
            if df['Nacionalidade'][ind] != 'E':
                obj.Estado.append(df['Estado'][ind])
            else:
                obj.Estado.append('Estrangeiro')

    def gera_areas_atuacao():
        df = pd.read_csv(f'{PREFIX}/areas1.txt', sep="\t", header=None, encoding='ISO-8859-1')
        df.columns = ['id', 'number', 'grande_area', 'area', 'sub_area', 'especialidade']
        df.id = df.id.astype('string')
       
        for ind in df.index:
            obj = AreasAtuacao()
            obj.LattesId.append(df['id'][ind])
            obj.GrandeArea.append(df['grande_area'][ind])

            if (not pd.isna(df.at[ind, 'area'])):
                obj.Area.append(df['area'][ind])

            if (not pd.isna(df.at[ind, 'sub_area'])):
                obj.SubArea.append(df['sub_area'][ind])

            if (not pd.isna(df.at[ind, 'especialidade'])):
                 obj.Especialidade.append(df['especialidade'][ind])
                 

    def gera_atuacoes():
        df = pd.read_csv(f'{PREFIX}/atuacoes1.txt', sep="\t", header=None, encoding='ISO-8859-1')
        df.columns = ['id', 'unknow', 'nome_instituicao', 'unknow2', 'unknow3', 'unknow4', 'unknow5', 'unknow6', 'unknow7', 'unknow8']
        df.id = df.id.astype('string')
       
        for ind in df.index:
            obj = Atuacoes()
            obj.LattesId.append(df['id'][ind])
            
            if (not pd.isna(df.at[ind, 'nome_instituicao'])):
                obj.Instituicao.append(df['nome_instituicao'][ind])

    def gera_orientacoes():
        df = pd.read_csv(f'{PREFIX}/orientacoes1.txt', sep="\t", header=None, encoding='ISO-8859-1')
        df.columns = ['id', 'tipo_trabalho', 'status', 'ano', 'nome_orientando', 'codigo_instituicao', 'nome_instituicao', 'unknow1', 'unknow2', 'unknow3', 'unknow4', 'unknow5', 'unknow6', 'unknow7', 'unknow8', 'unknow9', 'unknow10', 'unknow11', 'unknow12']
        df.id = df.id.astype('string')

        df.ano = df.ano.astype('string')

        #df.ano = pd.to_datetime(df.ano, infer_datetime_format= True)
        #df.ano = df.ano.astype('datetime64[Y]')

        for ind in df.index:
            obj = Orientacoes()
            obj.LattesId.append(df['id'][ind])
            
            obj.Instituicao.append(df['nome_instituicao'][ind])
            obj.TipoTrabalho.append(df['tipo_trabalho'][ind])
            obj.StatusOrientacao.append(df['status'][ind])
            obj.Ano.append(df['ano'][ind])
            obj.Nome.append(df['nome_orientando'][ind])
            
            if (not pd.isna(df.at[ind, 'nome_instituicao'])):
                obj.Instituicao.append(df['nome_instituicao'][ind])

    def gera_formacoes():
        df = pd.read_csv(f'{PREFIX}/formacoes1.txt', sep="\t", header=None, encoding='ISO-8859-1')
        df.columns = ['id','unknow1','titulo','unknow2','inicio','fim','status', 'curso','nome_instituicao','unknow3']
        
        df.id = df.id.astype('string')
        df.inicio = df.inicio.astype('string', errors='ignore')
        df.fim = df.fim.astype('string')

        for ind in df.index:
          
            obj = Formacoes()
            obj.LattesId.append(df['id'][ind])
            if (not pd.isna(df.at[ind, 'nome_instituicao'])):
                obj.Instituicao.append(df['nome_instituicao'][ind])
            obj.Titulo.append(df['titulo'][ind])
            if df['titulo'][ind] == 'LIVRE-DOCENCIA':
                obj.AnoInicio.append('null')
                obj.AnoFim.append('null')
            elif df['status'][ind] == 'EM_ANDAMENTO':
                obj.AnoFim.append('null')
            else:
                obj.AnoInicio.append(df['inicio'][ind])
                obj.AnoFim.append(df['fim'][ind])


#Função genérica para vincular automaticamente todas as relações por LattesID para todos os Pesquisadores
    def vincular_todos_por_lattesid(tipo_entidade):
        for entidade_pesquisador in onto[tipo_entidade].instances():
            Pesquisador_lattes_id = entidade_pesquisador.LattesId[0]  # Supondo que há apenas um LattesID por Pesquisador
            print(Pesquisador_lattes_id)
            # Gera as relações Pesquisador atua_em Atuacoes
            for atuacoes in onto["Atuacoes"].instances():
                atuacoes_lattes_id = atuacoes.LattesId[0]
                if Pesquisador_lattes_id == atuacoes_lattes_id:
                    #cria relação
                    entidade_pesquisador.atua_em.append(atuacoes)

            # Gera as relações Pesquisador areas_relacionadas AreasAtuacao
            for AreasAtuacao in onto["AreasAtuacao"].instances():
                AreasAtuacao_lattes_id = AreasAtuacao.LattesId[0]
                if Pesquisador_lattes_id == AreasAtuacao_lattes_id:
                    #cria relação
                    entidade_pesquisador.areas_relacionadas.append(AreasAtuacao)


            # Gera as relações Pesquisador orienta Orientacoes
            for Orientacoes in onto["Orientacoes"].instances():
                Orientacoes_lattes_id = Orientacoes.LattesId[0]
                if Pesquisador_lattes_id == Orientacoes_lattes_id:
                    #cria relação
                    entidade_pesquisador.orienta.append(Orientacoes)

            # Gera as relações Pesquisador orienta Formacoes
            for Formacoes in onto["Formacoes"].instances():
                Formacoes_lattes_id = Formacoes.LattesId[0]
                if Pesquisador_lattes_id == Formacoes_lattes_id:
                    #cria relação
                    entidade_pesquisador.possui_formacao.append(Formacoes)                   




    gera_curriculo()
    gera_areas_atuacao()
    gera_atuacoes()
    gera_orientacoes()
    gera_formacoes()
    

    # Chamando a função para vincular automaticamente todas as relações para todos os Pesquisadores
    vincular_todos_por_lattesid("Pesquisador")

    onto.save()


