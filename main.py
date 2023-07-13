import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd
import os


cols = ["Cod","Operação" , "Seire", "Numero", 'D H Emisão' , "D H Saída", 'CNPJ Emissor' , 'Nome Emissor', 'Nome Comercial' , 'logradouro Emissor', 'Bairro emissor', 'Municipio emissor', 'CEP emissor' , 'cpf destino' , 'nome destino' , 'logradouro destino', 'bairro destino' , 'municipio destino' , 'cep destino',
           "vIPI","vICMS","vBC","vFN","modFrete" , "vPa" , 'cod prod', 'cean' , 'descricao produto' , 'ncm' ,'CFOP' ,'qcom' , 'ucom' , 'vucom' , 'vprod' ,]

dirs = os.listdir('xml/')
# xprod = cprod = cean = ncm = cfpo = ucom = qcom = vucom = vprod = ceantib = ""
print(dirs)
row = []

for dir in dirs:
        xprod = cprod = cean = ncm = cfpo = ucom = qcom = vucom = vprod = ceantib = ""

        xml = open('xml/'+dir)
        nfe = minidom.parse(xml)
        cod = nfe.getElementsByTagName('cUF')[0].firstChild.data
        nat = nfe.getElementsByTagName('natOp')[0].firstChild.data
        serie = nfe.getElementsByTagName('serie')[0].firstChild.data
        num = nfe.getElementsByTagName('nNF')[0].firstChild.data
        try:
                dhemi = nfe.getElementsByTagName('dhEmi')[0].firstChild.data
        except IndexError:
                dhemi = nfe.getElementsByTagName('dEmi')[0].firstChild.data

        try:
                dhSaiEnt= nfe.getElementsByTagName('dhSaiEnt')[0].firstChild.data
        except IndexError:
                dhSaiEnt= nfe.getElementsByTagName('dSaiEnt')[0].firstChild.data
                
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
        vipi = nfe.getElementsByTagName('vIPI')[0].firstChild.data      
        vicms = nfe.getElementsByTagName('vICMS')[0].firstChild.data      
        vbc = nfe.getElementsByTagName('vBC')[0].firstChild.data      
        vfn = nfe.getElementsByTagName('vNF')[0].firstChild.data      
        modfrete = nfe.getElementsByTagName('modFrete')[0].firstChild.data      
        vpag = nfe.getElementsByTagName('vProd')[0].firstChild.data      

        for i in range(nfe.getElementsByTagName('xProd').length):      
                xprod += f"{nfe.getElementsByTagName('xProd')[i].firstChild.data};"
                cprod += f"{nfe.getElementsByTagName('cProd')[i].firstChild.data};"
                try:
                        cean += f"{nfe.getElementsByTagName('cEAN')[i].firstChild.data};"
                except AttributeError: 
                        cean += ";"
                        ceantib += ";"

                try:
                        ncm += f"{nfe.getElementsByTagName('NCM')[i].firstChild.data};"
                except IndexError:
                        ncm += ";"
                        
                try:
                        ceantib += f"{nfe.getElementsByTagName('cEANTrib')[i].firstChild.data};"
                except AttributeError: 
                        
                        ceantib += ";"

                cfpo += f"{nfe.getElementsByTagName('CFOP')[i].firstChild.data};"
                ucom += f"{nfe.getElementsByTagName('uCom')[i].firstChild.data};"
                qcom += f"{nfe.getElementsByTagName('qCom')[i].firstChild.data};"
                vucom += f"{nfe.getElementsByTagName('vUnCom')[i].firstChild.data};"
                vprod += f"{nfe.getElementsByTagName('vProd')[i].firstChild.data};"
 
      
        

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