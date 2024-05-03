import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql

# Connectar a la base de dades MySQL
sqlConnection = mysql.connect(

	host = "localhost",
	user = "root",
	password = "root",
	database = "sergioAlumnesDB"
)

def guardar_inscripcio():

	# dades alumne
	dni = entry_dni.get()
	nom = entry_nom.get()
	edat = entry_edat.get()

	# adreça alumne
	localitat = entry_localitat.get()
	cp = entry_cp.get() # codi postal
	carrer = entry_carrer.get()
	vivenda = entry_vivenda.get() # numero de la vivenda
	

	# dades cicle a inscriure
	cicle = entry_cicle.get()
	curs = entry_curs.get()

	# Validació de camps
	if (not nom or not edat or not dni) or (not localitat or not cp or not carrer or not vivenda) or (not cicle or not curs):

		messagebox.showerror("Error", "Per favor completa tots el camps.")
		return

	# Insertar informació a la base de dades
	cursor = sqlConnection.cursor()

	consultAlu = "INSERT INTO alumnes (dni, nom, edat) VALUES (%s, %s, %s)"
	consultAdreçes = "INSERT INTO adreçes (cp, localitat, carrer, vivenda, propietari) VALUES (%s, %s, %s, %s, %s)"
	consultaCicles = "INSERT INTO cicles (cicle, curs, alumne) VALUES (%s, %s, %s)"

	dadesAlu = (dni, nom, edat)
	cursor.execute(consultAlu, dadesAlu)

	dadesAdr = (cp, localitat, carrer, vivenda, dni)
	cursor.execute(consultAdreçes, dadesAdr)

	dadesCicles = (cicle, curs, dni)
	cursor.execute(consultaCicles, dadesCicles)

	sqlConnection.commit()
	cursor.close()

	messagebox.showinfo("Inscripció correcta", f"¡{nom} ha sigut inscrit correctament!")


# Finestra principal
finestra = tk.Tk()
finestra.title("Inscripció d'Alumnes")

# Crear i posicionar elements en la app
dades_personals = tk.Label(finestra, text="DADES PERSONALS")
dades_personals.grid(row=0, column= 0, columnspan=2)

dades_personals = tk.Label(finestra, text="VIVENDA")
dades_personals.grid(row=0, column=2, columnspan=2)

dades_personals = tk.Label(finestra, text="CICLE A INSCRIURE")
dades_personals.grid(row=0, column= 4, columnspan=2)

label_dni = tk.Label(finestra, text="*NIF/NIE:")
label_dni.grid(row=1, column=0)
entry_dni = tk.Entry(finestra)
entry_dni.grid(row=1, column=1)

label_nom = tk.Label(finestra, text="*Nom:")
label_nom.grid(row=2, column=0)
entry_nom = tk.Entry(finestra)
entry_nom.grid(row=2, column=1)

label_edat = tk.Label(finestra, text="*Edat:")
label_edat.grid(row=3, column=0)
entry_edat = tk.Entry(finestra)
entry_edat.grid(row=3, column=1)

# --------------------------------------------------------- ADREÇES

label_cp = tk.Label(finestra, text="*Codi Postal:")
label_cp.grid(row=1, column=2)
entry_cp = tk.Entry(finestra)
entry_cp.grid(row=1, column=3)

label_localitat = tk.Label(finestra, text="*Localitat:")
label_localitat.grid(row=2, column=2)
entry_localitat = tk.Entry(finestra)
entry_localitat.grid(row=2, column=3)

label_carrer = tk.Label(finestra, text="*Carrer:")
label_carrer.grid(row=3, column=2)
entry_carrer = tk.Entry(finestra)
entry_carrer.grid(row=3, column=3)

label_vivenda = tk.Label(finestra, text="*Nº Vivenda:")
label_vivenda.grid(row=4, column=2)
entry_vivenda = tk.Entry(finestra)
entry_vivenda.grid(row=4, column=3)


# --------------------------------------------------------- CICLES

label_cicle = tk.Label(finestra, text="*Cicle:")
label_cicle.grid(row=1, column=4)
entry_cicle = tk.Entry(finestra)
entry_cicle.grid(row=1, column=5)

label_curs = tk.Label(finestra, text="*Curs:")
label_curs.grid(row=2, column=4)
entry_curs = tk.Entry(finestra)
entry_curs.grid(row=2, column=5)

# --------------------------------------------------------- ALTRES ELEMENTS

button_inscriure = tk.Button(finestra, text="Inscriure", command=guardar_inscripcio)
button_inscriure.grid(row=998, columnspan=2)

# Execució
finestra.mainloop()