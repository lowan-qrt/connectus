document.addEventListener("DOMContentLoaded", function() {
    var formulaire1 = document.getElementById("form");
    var formulaire2 = document.getElementById("form-2");
    var changerFormulaireBtn = document.getElementById("button1");
    var retourFormulaire1Btn = document.getElementById("retour");

    changerFormulaireBtn.addEventListener("click", function() {
        formulaire1.style.display = "none";
        formulaire2.style.display = "block";
        // Stocker l'état actuel dans le stockage local
        localStorage.setItem("formulaireCourant", "form-2");
    });

    retourFormulaire1Btn.addEventListener("click", function() {
        formulaire2.style.display = "none";
        formulaire1.style.display = "block";
        // Stocker l'état actuel dans le stockage local
        localStorage.setItem("formulaireCourant", "form");
    });

    // Récupérer l'état actuel depuis le stockage local
    var etatActuel = localStorage.getItem("formulaireCourant");

    // Afficher le formulaire correspondant à l'état actuel
    if (etatActuel === "form-2") {
        formulaire1.style.display = "none";
        formulaire2.style.display = "block";
    } else {
        formulaire2.style.display = "none";
        formulaire1.style.display = "block";
    }
});
