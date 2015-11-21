Dipendenze
-

Il progetto necessita soltanto di due dipendenze:
* bottle - libreria per creare il webservice
* pyserial - libreria per sfruttare la comunicazione seriale

Per installare le dipendenze necessarie al progetto con il packet manager **APT** basta digitare
```
sudo apt-get install python3 python3-bottle python3-serial
```

Coding Style
-

Brevissimo inciso sullo stile della nomenclatura adottata nel codice.
I nomi utilizzati faranno riferimento alla famosa convenzione [PEP-8](http://legacy.python.org/dev/peps/pep-0008/#naming-conventions).

Si raccomanda di attenersi a queste poche e semplici regole di scrittura del codice per favorire una collaborazione più efficace e produttiva:

* Nome di modulo (file .py): nomedimodulopython
* Nomi di variabili: nome_lungo_di_variabile
* Nomi di classi: NomeLungoDiClasse
* Nomi di variabili private: _nome_di_variabile_privata
* Nomi di metodi di classe: nome_di_metodo_di_classe


Unit testing
-

Unittest è un modulo python per eseguire un insieme di regole che vanno a verificare in modo totalmente automatizzato il corretto funzionamento del codice che sviluppato.

Tutti i file denominati come **test_*nome_modulo*** non sono altro che una raccolta di *testcase* per validare il codice del rispettivo modulo.

Per eseguire i test basta spostarsi nella cartella che li contiene e lanciare il comando seguente
```
python3 -m unittest
```
