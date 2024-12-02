import psycopg2

#Dettagli di connessione
host = "localhost"
port = "5432"
dbname = "Accademia"
user = "postgres"
password = "postgres"

#Connessionee ad database

try:
    connection = psycopg2.connect(

        host = host,
        port = port,
        dbname = dbname,
        user = user,
        password = password
    )

    print("Connesione al database avvenuta con successo")
except Exception as e:
    print(f"Errore durante la connessione al database: {e}")



cursor = connection.cursor()

#Esegui la query
cursor.execute("SELECT * FROM Persona")

#Recupere i risutati
rows = cursor.fetchall()
for row in rows:
    print(row)

scelta: int



risposta: str = "si"
lista_scelte: list[int] = [1,2,3,4] #lista che serve a contenere le scelte valide, in modo da non stampare la stessa strinda per 2 volte.
                                    #guarda da riga a 68 a 72

while(risposta.lower() == "si"):

    print()

    scelta = int(input("Inserisci il numero della QUERY vuoi eseguire?\n"
          "1 - Seleziona il tipo di assenze di tutti gli strutturati\n"
          "2 - Seleziona le date in ordine cresecente delle attività non progettuale\n"
          "3 - Seleziona il nome, data inizio e data fine del WP del progetto di nome PEGASUS\n"
          "4 - Query con tabella a scelta\n"
          "5 - Se non vuoi eseguire nessuna operazione\n"))
        

    if scelta == 1:
        cursor.execute("SELECT DISTINCT ass.tipo FROM Assenza ass")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif scelta == 2:
        cursor.execute("SELECT DISTINCT annop.giorno FROM AttivitaNonProgettuale annop WHERE annop.tipo = 'Didattica' ORDER BY annop.giorno ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif scelta == 3:
        cursor.execute("SELECT wp.nome, wp.inizio, wp.fine FROM Wp wp JOIN Progetto pr ON pr.id = wp.progetto WHERE pr.nome = 'Pegasus'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif scelta == 4:
        
        nometabella: str = input("Inserisci il nome della tabella\n")
        cursor.execute("SELECT * FROM "+nometabella)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif scelta == 5:
        exit()


    else:
        print("Inserimento non valido.\nVuoi eseguire un'altra operazione? Si/No ")
        
    if scelta not in lista_scelte:
        risposta = input("Vuoi eseguire un'altra operazione? Si/No ")