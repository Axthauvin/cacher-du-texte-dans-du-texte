function int(str){
    return parseInt(str);
}

function str(l){
    return l.toString()
}

function base6(nombre){
    if (nombre >= 6**4) {
        return "Erreur";
    }
        
    var Base6 = [0, 0, 0, 0];
    while (nombre > 0) {
        Base6[3] = Base6[3] + 1;
        nombre -= 1;
        if (int(Base6[3]) >= 6) {
            Base6[3] = 0
            Base6[2] = Base6[2] + 1
        }
        if (int(Base6[2]) >= 6) {
            Base6[2] = 0
            Base6[1] = Base6[1] + 1
        }
        if (int(Base6[1]) >= 6) {
            Base6[1] = 0
            Base6[0] = Base6[0] + 1
        }
            
    }
        
    

    base6str = "";
    for (const el of Base6) {
        base6str += str(el);
    }
       

    return base6str
}
    
    

function destroy(id){
    var elem = document.getElementById(id);
    elem.parentNode.removeChild(elem);
}

var textacopier;

function dec2bin(dec){
    return (dec >>> 0).toString(2);
}


function copytoclipbard() {
    str = textacopier;
    const el = document.createElement('textarea');
    el.value = str;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    alert("Le texte a bien été copié !");

}

function coder(){
    document.getElementById("textresultat").style = "color : rgb(229, 57, 53);"

    original = document.getElementById("txtOri").value;
    acacher = document.getElementById("txtcacher").value;
    
    
    console.log("longeur de original " + original.length)
    console.log("longeur de acacher " +  acacher.length)
    
    
    if (original.length < acacher.length * 4) {
        err = "Erreur ! Le message original est trop court ! Il a besoin de " + (acacher.length * 4) + " caractères. <br> <strong> Soit " + (acacher.length * 4 - original.length) + " de plus.</strong><br> Ou, on peut aussi <strong>raccoucir le message caché de " + (acacher.length - Math.round((original.length / 4))) +  " lettres.</strong>";
        document.getElementById("textresultat").innerHTML  = err;
        return err;
    }

    
        
    listeBase2 = []
    for (const lettre of acacher) {
        console.log(lettre);
        binary = base6(lettre.charCodeAt(0)).toString()
        if (binary == "Erreur") {
            err = "Le caractère " + lettre + " est trop loin dans la table UTF-8";
            document.getElementById("textresultat").innerHTML  = err;
            return err;
        }
            
        listeBase2.push(binary);
    }

    console.log(listeBase2);
    
    var possibilites = ["", "\u200C", "\u200D", "\u200E", "\u200F", "\u034F"];
    

    var chaineFinale = "";
    var compteur = 0;
    for (const binaires of listeBase2) {
        for (const unbit of binaires) {
            chaineFinale += original[compteur];
            if (int(unbit) > 0) {
                chaineFinale += possibilites[int(unbit)]
            }
                
            compteur += 1
        }
    }

    
    
    
    chaineFinale += original.substring(compteur, original.length);
    document.getElementById("textresultat").innerHTML = "Le message a bien été généré !";
    document.getElementById("textresultat").style = "color : rgb(17, 80, 153);"

    document.getElementById("valider").innerHTML = "En générer un autre";
    document.getElementById("valider").style = "background-color : rgb(17, 80, 153);"
    document.getElementById("valider").setAttribute('onclick', "location.reload()");

    destroy("txtcacher");
    destroy("title2");

    document.getElementById("title1").innerText = "Le message modifié est :";

    copy = document.createElement("button");
    copy.innerText = "Copier dans le presse papier";
    copy.className = "valider espaces";

    

    textacopier = chaineFinale;


    copy.setAttribute('onclick','copytoclipbard()');
    document.getElementsByClassName("centered")[1].appendChild(copy);

    

    console.log(chaineFinale);
    return chaineFinale;

    
    
}


function decoder(){
    var message = document.getElementById("txtOri").value;

    var listebinaire = [];
    var binaire = "";
    var caractere = 1;
    var possibilites = ["", "\u200C", "\u200D", "\u200E", "\u200F", "\u034F"];
    while (caractere < message.length) {
        
        if (possibilites.includes(message[caractere])) {
            binaire += str(possibilites.indexOf(message[caractere]))
        } else {
            binaire += "0"
            caractere -= 1
        }
        
        caractere += 2
        
        

        if (binaire.length == 4 && binaire != "0000") {
            listebinaire.push(binaire)
            binaire = "";
        }
            
    }
        
        
        
        
    
    var strfinale = "";
    for (lettre of listebinaire) {
        strfinale += String.fromCharCode(parseInt(lettre, 6));
    }
    
        
    console.log(strfinale);

    destroy("txtOri");
    document.getElementById("title1").innerHTML = "Le message caché était :"
    document.getElementById("textresultat").innerHTML = strfinale;

    document.getElementById("valider").innerHTML = "En décoder un autre";
    document.getElementById("valider").style = "background-color : rgb(17, 80, 153);"
    document.getElementById("valider").setAttribute('onclick', "location.reload()");

    return strfinale;
}