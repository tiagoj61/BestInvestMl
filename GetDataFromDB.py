import psycopg2
import pandas as pd

param_dic = {
    "host"      : "localhost",
    "database"  : "ml_fundamentus",
    "user"      : "postgres",
    "password"  : "postgres"
}
def connect(params_dic):
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query, column_names):
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df
 

conn = connect(param_dic)
column_names = ['id','papel','cotacao','p_l','p_vp','psr','div_yield','p_ativo','p_cap_giro','p_ebit','p_ativo_circulante','ev_ebit','ev_ebitda','mrg_ebit','mrg_liquida','liq_corr','roic','roe','liquides_2meses','patrim_liquido','div_bruto_patrimonio','crescimento_recorente_5a']
# Execute the "SELECT *" query
df = postgresql_to_dataframe(conn, "select * from acao", column_names)
print(df.head())