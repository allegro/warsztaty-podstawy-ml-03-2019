Aby praca na warsztatach szła sprawnie, prosimy Was o wcześniejsze przygotowanie
środowiska na swoich komputerach.

1. Zainstalujcie system zarządzania zależnościami Pythona Anaconda:
https://www.anaconda.com/download/

2. W załączniku do niniejszego maila powinien znajdować się plik
alleml.yml z specyfikacją środowiska

3. W wierszu poleceń uruchomcie komendę:

    conda env create -f <sciezka do pliku>/alleml.yml

4. Po instalacji wszystkich pakietów aktywujcie środowisko poleceniem:

    source activate alleml

(deaktywację środowiska można wykonać komendą: source deactivate)

5. Mając aktywne środowisko alleml, sprawdźcie czy wszystko działa,
uruchamiając jupytera poleceniem:

    jupyter notebook

    lub

    jupyter-notebook

Jupyter powinien się uruchomić i automatycznie otworzyć w przeglądarce.

Będąc w konsoli z aktywnym środowiskiem alleml w sytuacji gdy
zabraknie jakiegoś pakietu będziecie mogli go doinstalować
standardowymi poleceniami
np. pip install httplib2

Uwagi dodatkowe (głównie dla użytkowników Windows)

W specyfikacji środowiska musicie zmienic nazwę pakietu xgboost, dla
windows nazywa się on nieco inaczej bodajże: py-xgboost.

Może zainstnieć też potrzeba instalacji dodatkowych operacji aby
uruchomić graphviza z którego korzystamy do wizualizacji drzew
decyzyjnych.
- Dla macowców: brew install graphviz
- Dla windowsa instrukcja jest tu:
https://stackoverflow.com/questions/18438997/why-is-pydot-unable-to-find-graphvizs-executables-in-windows-8
- Linuxowcy sobie pewnie poradzą ;-)

W przypadku Windowsa, może też pojawić się konieczność zainstalowania
Visual Studio (a dokładniej analoga Linuxowego build-essentials i
xcode)

