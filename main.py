import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd
import os

root = ET.parse('xml/NFe-43230289982268002980550020002336701002634178.xml').getroot()
nsNFE = {'ns': "http://www.portalfiscal.inf.br/nfe" }
numero_nfe = root.find('ns:NFe/ns:infNFe/ns:ide/ns:nNF' , nsNFE) 


cols = ["Cod","Operação" , "Seire", "Numero", 'D H Emisão' , "D H Saída", 'CNPJ Emissor' , 'Nome Emissor', 'Nome Comercial' , 'logradouro Emissor', 'Bairro emissor', 'Municipio emissor', 'CEP emissor' , 'cpf destino' , 'nome destino' , 'logradouro destino', 'bairro destino' , 'municipio destino' , 'cep destino',
         'cod prod', 'cean' , 'descricao produto' , 'ncm' ,'CFOP' ,'qcom' , 'ucom' , 'vucom' , 'vprod' ,  "vIPI","vICMS","vBC","vFN","modFrete" , "vPa"]

dirs = os.listdir('xml/')
print(dirs)
row = []

for dir in dirs:
        xml = open('xml/'+dir)
        nfe = minidom.parse(xml)
        cod = nfe.getElementsByTagName('cUF')[0].firstChild.data
        nat = nfe.getElementsByTagName('natOp')[0].firstChild.data
        serie = nfe.getElementsByTagName('serie')[0].firstChild.data
        num = nfe.getElementsByTagName('nNF')[0].firstChild.data
        dhemi = nfe.getElementsByTagName('dhEmi')[0].firstChild.data
        dhSaiEnt= nfe.getElementsByTagName('dhSaiEnt')[0].firstChild.data

        cnpj = nfe.getElementsByTagName('CNPJ')[0].firstChild.data
        copNome = nfe.getElementsByTagName('xNome')[0].firstChild.data
        copNomeC = nfe.getElementsByTagName('xFant')[0].firstChild.data
        logC = nfe.getElementsByTagName('xLgr')[0].firstChild.data
        bairroC = nfe.getElementsByTagName('xBairro')[0].firstChild.data
        munc = nfe.getElementsByTagName('xMun')[0].firstChild.data
        cepc = nfe.getElementsByTagName('CEP')[0].firstChild.data

        cpf = nfe.getElementsByTagName('CPF')[0].firstChild.data
        nomed = nfe.getElementsByTagName('xNome')[1].firstChild.data
        logd = nfe.getElementsByTagName('xLgr')[1].firstChild.data
        bairrod = nfe.getElementsByTagName('xBairro')[1].firstChild.data
        cepd = nfe.getElementsByTagName('CEP')[1].firstChild.data
        mund = nfe.getElementsByTagName('xMun')[1].firstChild.data
        cprod = nfe.getElementsByTagName('cProd')[0].firstChild.data
        cean = nfe.getElementsByTagName('cEAN')[0].firstChild.data      
        xprod = nfe.getElementsByTagName('xProd')[0].firstChild.data      
        ncm = nfe.getElementsByTagName('NCM')[0].firstChild.data      
        cfpo = nfe.getElementsByTagName('CFOP')[0].firstChild.data      
        ucom = nfe.getElementsByTagName('uCom')[0].firstChild.data      
        qcom= nfe.getElementsByTagName('qCom')[0].firstChild.data      
        vucom = nfe.getElementsByTagName('vUnCom')[0].firstChild.data      
        vprod = nfe.getElementsByTagName('vProd')[0].firstChild.data      
        ceantib = nfe.getElementsByTagName('cEANTrib')[0].firstChild.data      
        vipi = nfe.getElementsByTagName('vIPI')[0].firstChild.data      
        vicms = nfe.getElementsByTagName('vICMS')[0].firstChild.data      
        vbc = nfe.getElementsByTagName('vBC')[0].firstChild.data      
        vfn = nfe.getElementsByTagName('vNF')[0].firstChild.data      
        modfrete = nfe.getElementsByTagName('modFrete')[0].firstChild.data      
        vpag = nfe.getElementsByTagName('vPag')[0].firstChild.data      


        row.append({
                "Cod":cod,
                "Operação":nat , 
                "Seire":serie, 
                "Numero":num, 
                'D.H. Emisão':dhemi , 
                "D.H Saída":dhSaiEnt, 
                'CNPJ Emissor':cnpj , 
                'Nome Emissor':copNome, 
                'Nome Comercial':copNomeC , 
                'logradouro Emissor':logC, 
                'Bairro emissor':bairroC, 
                'Municipio emissor':munc, 
                'CEP emissor':cepc ,  
                'cpf destino': cpf, 
                'nome destino' :nomed, 
                'logradouro destino':logd, 
                'bairro destino' :bairrod, 
                'municipio destino':mund , 
                'cep destino':cepd,
                'cod prod':cprod,
                'cean':cean,
                'descricao produto':xprod,
                'ncm':ncm,
                'CFOP':cfpo,
                'qcom':qcom,
                'ucom':ucom, 
                'vucom':vucom,
                'vprod':vprod,  
                "vIPI":vipi,
                "vICMS":vicms,
                "vBC":vbc,
                "vFN":vfn,
                "modFrete":modfrete,
                "vPa":vpag,        
        })


df = pd.DataFrame(row, columns=cols)
  
# Writing dataframe to csv
df.to_csv('output.csv' , encoding='UTF-8')