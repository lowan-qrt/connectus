const first_button = document.getElementById('submit'); // Button "CONTINUER"

// Display the next form part
first_button.addEventListener('click', function() {
    console.log('First button clicked')

    let form = document.getElementById('form');        // form
    let first_part = document.getElementById('first'); // part for updates
    let button = document.getElementById('submit')     // button
    // Updates
    form.style.margin = '10vh 0 6vh';
    form.style.height = '80vh';
    first.innerHTML += `
    <label for="fisrt_name">*Prénom</label>
    <input id="fisrt_name" class="input" type="text" name="new_user" placeholder="Obligatoire" required>
    <br>
    <label for="last_name">*Nom</label>
    <input id="last_name" class="input" type="text" name="new_user" placeholder="Obligatoire" required>
    <br>
    <label for="phone">Numéro de téléphone</label>
    <input id="phone" class="input" type="text" name="new_user" placeholder="Optionnel">
    `;
    button.value = 'S\'INSCRIRE'
});