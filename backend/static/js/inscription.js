function calculateDateMin() {
    var today = new Date();
    var minDate = new Date(today);
    
    // Adjust the age
    minDate.setFullYear(today.getFullYear() - 18);
    
    // Plus one day
    minDate.setDate(minDate.getDate() + 1);

    var inputDate = document.getElementById('birthday');
    inputDate.setAttribute('max', minDate.toISOString().split('T')[0]);
}

function nextPart() {
    console.log('Bouton suivant cliqué');

    // Elements
    let form = document.getElementById('form');       // form
    let firstPart = document.getElementById('first'); // the part to update
    let button = document.getElementById('submit');   // button

    // Updates
    if (button.value === 'CONTINUER') {
        form.style.margin = '10vh 0 6vh';
        form.style.height = '100vh';
        firstPart.insertAdjacentHTML('beforeend', `
        <label for="first_name">*Prénom</label>
        <input name="first_name" id="first_name" class="input" type="text" placeholder="Obligatoire" required>
        <br>
        <label for="last_name">*Nom</label>
        <input name="last_name" id="last_name" class="input" type="text" placeholder="Obligatoire" required>
        <br>
        <label for="birthday">*Date de naissance</label>
        <input name="birthday" id="birthday" class="input" type="date" placeholder="Sélectionnez une date" required>
        <br>
        <label for="phone">Numéro de téléphone</label>
        <input name="phone" id="phone" class="input" type="text" placeholder="Optionnel">
        <p>{{ errorPseudo }}</p>
        `);

        calculateDateMin(); // adjust the min date

        button.value = 'S\'INSCRIRE';
    }
}

let button = document.getElementById('submit'); // button "CONTINUER"

// Call function when button clicked
button.addEventListener('click', function(event) {
    let form = document.getElementById('form');

    if (button.value === 'CONTINUER') {
        event.preventDefault(); // don't load the page
        nextPart();
    } else {
        form.submit(); // load the page
    }
});