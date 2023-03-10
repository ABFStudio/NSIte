const moyenneFinale = document.getElementById("moyenne");
const calculBtn = document.getElementById("calculer-moyenne");

function calculerMoyenne(value1, value2, value3) {
    return (value1 + value2 + value3) / 3;
}

function updateMoyenne() {
    let maths = Number(document.getElementById("maths").value);
    let physique = Number(document.getElementById("physique").value);
    let snt = Number(document.getElementById("snt").value);

    if (maths > 20 || physique > 20 || snt > 20 || maths < 0 || physique < 0 || snt < 0 || maths === "" || physique === "" || maths === "") {
        moyenneFinale.setAttribute("red", true);
        moyenneFinale.removeAttribute("orange");
        moyenneFinale.removeAttribute("green");
        moyenneFinale.innerHTML = "Valeurs incorrectes !";
    }
    else {
        const moyenne = calculerMoyenne(maths, physique, snt);
        if (moyenne < 10) {
            moyenneFinale.setAttribute("red", true);
            moyenneFinale.removeAttribute("orange");
            moyenneFinale.removeAttribute("green");
            moyenneFinale.innerHTML = "La spécialité NSI vous est vivement déconseillée !";
        }
        else if (moyenne >= 10 && moyenne < 14) {
            moyenneFinale.setAttribute("orange", true);
            moyenneFinale.removeAttribute("red");
            moyenneFinale.removeAttribute("green");
            moyenneFinale.innerHTML = "Vous devrez vous accrocher, mais vous pouvez y arriver !";
        }
        else if (moyenne >= 14 && moyenne <= 20) {
            moyenneFinale.setAttribute("green", true);
            moyenneFinale.removeAttribute("orange");
            moyenneFinale.removeAttribute("red");
            moyenneFinale.innerHTML = "Vous pouvez y aller les yeux fermés !";
        }
        else {
            moyenneFinale.setAttribute("red", true);
            moyenneFinale.removeAttribute("orange");
            moyenneFinale.removeAttribute("green");
            moyenneFinale.innerHTML = "Valeurs incorrectes !";
        }
    }
}

calculBtn.addEventListener("click", updateMoyenne);