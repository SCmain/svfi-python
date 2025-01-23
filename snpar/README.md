# Français
## Fonctionnalités readsnpar.py :

    Lecture binaire :
        Le fichier est ouvert en mode binaire avec open(file_path, "rb").
        struct.unpack("<l", ...) est utilisé pour lire un entier long en format little-endian (32 bits).

    Affichage des valeurs :
        glSN est affiché comme un entier.
        gucAddr est affiché :
            En hexadécimal : chaque octet est converti au format hexadécimal.
            En ASCII : les caractères imprimables sont affichés tels quels ; les caractères non imprimables sont remplacés par un ..

    Validation :
        Vérifie que le fichier existe.
        Vérifie que les données lues ont la longueur attendue (4 octets pour glSN, 10 octets pour gucAddr).

### Prérequis et commandes pour OpenSUSE Tumbleweed i386 :
Installer Python3 :

Python3 est généralement préinstallé sur OpenSUSE Tumbleweed. Si ce n'est pas le cas :

sudo zypper install python3

Installer les modules nécessaires :

Le code utilise uniquement les modules standard de Python, donc aucune bibliothèque externe n'est nécessaire.
Exemple d'utilisation :

    Sauvegardez le programme dans un fichier, par exemple readsnpar.py.
    Rendez le script exécutable :

chmod +x readsnpar.py

Exécutez le script :

    ./readsnpar.py /root/controller/scmain/snpar.par

### Exemple de sortie :

Si le fichier contient :

    glSN = 12345
    gucAddr = "ABCDEFGHIJ"

La sortie sera :

glSN: 12345
gucAddr (hex): 41 42 43 44 45 46 47 48 49 4a
gucAddr (ASCII): ABCDEFGHIJ

Si gucAddr contient des caractères non imprimables :

glSN: 12345
gucAddr (hex): 41 42 43 00 45 46 47 48 49 1a
gucAddr (ASCII): ABC.EFGHI.

### Avantages du code Python :

    Facilité de lecture et maintenance.
    Compatibilité multi-plateforme.
    Aucune dépendance externe requise.

## fonctionalités writesnpar.py

### Exemple d'utilisation

    Sauvegardez le code dans un fichier nommé writesnpar.py.

    Rendez-le exécutable :

chmod +x writesnpar.py

### Commande pour écrire les données :

./writesnpar.py file.snpar 12345 4142434445464748494a

    file.snpar : Chemin du fichier binaire à créer.
    12345 : Valeur pour glSN.
    4142434445464748494a : Chaîne hexadécimale représentant 10 octets (par exemple, "ABCDEFGHIJ").

### Exemple de sortie :

    Data was written to file 'file.snpar' successfully.
    Contents of file 'file.snpar':
    glSN: 12345
    gucAddr (hex): 41 42 43 44 45 46 47 48 49 4a
    gucAddr (ASCII): ABCDEFGHIJ

### Points forts :

    Écrit et vérifie les données en un seul script.
    Affiche les données en formats lisibles : hexadécimal et ASCII.
    Robuste face aux erreurs d'entrée et de fichier.

# English

## Featuresreadsnpar.py :

Binary reading:
The file is opened in binary mode with open(file_path, "rb").
struct.unpack("<l", ...) is used to read a long integer in little-endian (32-bit) format.

Displaying values:
glSN is displayed as an integer.
gucAddr is displayed:
In hexadecimal: each byte is converted to hexadecimal format.
In ASCII: printable characters are displayed as is; non-printable characters are replaced by a ..

Validation:
Checks that the file exists.
Checks that the data read has the expected length (4 bytes for glSN, 10 bytes for gucAddr).

### Prerequisites and commands for OpenSUSE Tumbleweed i386:
Installing Python3:

Python3 is usually preinstalled on OpenSUSE Tumbleweed. If not:

sudo zypper install python3

Install the necessary modules:

The code uses only standard Python modules, so no external libraries are needed.
Example of use:

Save the program in a file, for example readsnpar.py.
Make the script executable:

chmod +x readsnpar.py

Run the script:

./readsnpar.py /root/controller/scmain/snpar.par

### Example output:

If the file contains:

glSN = 12345
gucAddr = "ABCDEFGHIJ"

The output will be:

glSN: 12345
gucAddr (hex): 41 42 43 44 45 46 47 48 49 4a
gucAddr (ASCII): ABCDEFGHIJ

If gucAddr contains non-printable characters:

glSN: 12345
gucAddr (hex): 41 42 43 00 45 46 47 48 49 1a
gucAddr (ASCII): ABC.EFGHI.

### Advantages of Python code:

Ease of reading and maintenance.
Multi-platform compatibility.
No external dependencies required.

## writesnpar.py features

### Example usage

Save the code in a file named writesnpar.py.

Make it executable:

chmod +x writesnpar.py

### Command to write data:

./writesnpar.py file.snpar 12345 4142434445464748494a

file.snpar : Path to the binary file to create.
12345 : Value for glSN.
4142434445464748494a : Hexadecimal string representing 10 bytes (e.g., "ABCDEFGHIJ").

### Example output:

Data was written to file 'file.snpar' successfully.
Contents of file 'file.snpar':
glSN: 12345
gucAddr (hex): 41 42 43 44 45 46 47 48 49 4a
gucAddr (ASCII): ABCDEFGHIJ

### Highlights:

Writes and verifies data in a single script.
Displays data in human-readable formats: hexadecimal and ASCII.
Robust against input and file errors.