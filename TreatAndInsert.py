import psycopg2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

con = psycopg2.connect(host='localhost', database='ml_fundamentus',
user='postgres', password='postgres')
cur = con.cursor()

sql = 'drop schema public cascade;create schema public'
cur.execute(sql)
con.commit()

sql = 'CREATE TABLE IF NOT EXISTS acao ('
sql = sql + 'id serial primary key,'
sql = sql + 'papel character varying(10),'
sql = sql + 'cotacao double precision,'
sql = sql + 'p_l double precision,'
sql = sql + 'p_vp double precision,'
sql = sql + 'psr double precision,'
sql = sql + 'div_yield double precision,'
sql = sql + 'p_ativo double precision,'
sql = sql + 'p_cap_giro double precision,'
sql = sql + 'p_ebit double precision,'
sql = sql + 'p_ativo_circulante double precision,'
sql = sql + 'ev_ebit double precision,'
sql = sql + 'ev_ebitda double precision,'
sql = sql + 'mrg_ebit double precision,'
sql = sql + 'mrg_liquida double precision,'
sql = sql + 'liq_corr double precision,'
sql = sql + 'roic double precision,'
sql = sql + 'roe double precision,'
sql = sql + 'liquides_2meses double precision,'
sql = sql + 'patrim_liquido double precision,'
sql = sql + 'div_bruto_patrimonio double precision,'
sql = sql + 'crescimento_recorente_5a double precision'
sql = sql + ')'
cur.execute(sql)
con.commit()

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("http://www.fundamentus.com.br/resultado.php")

tabela = driver.find_elements(By.TAG_NAME, "tbody")
linhas=tabela[0].find_elements(By.TAG_NAME, "tr")
for linha in linhas:
    colunas=linha.find_elements(By.TAG_NAME, "td")
    sql = "INSERT INTO acao VALUES (default,"
    tamanho = len(colunas)
    for i in range(tamanho):
        coluna=colunas[i].text
        coluna=coluna.replace(".","") 
        coluna=coluna.replace(",",".") 
        if coluna.find("%") != -1:
            coluna=coluna.replace("%","") 
            aux=float(coluna)
            coluna=str(aux/100)
        if i==0:
             sql=sql+"'"+coluna+"'"
        else:
            sql=sql+coluna
        if i!=tamanho-1:
            sql=sql+","
            
    sql=sql+")"
    cur.execute(sql)   

#Fechando conecxão banco
con.commit()
con.close()

#Fechando conecxão chromedriver
driver.quit()