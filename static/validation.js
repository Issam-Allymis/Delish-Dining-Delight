function validateContent(Event) {
    var allowedWords = ['super pepperoni pizza', 'coke', 'fanta', 'water', 
                        'bavette spaghetti with tomato basil sause', 'pepperoni pizza', 
                        'chicken', 'Chicken Curry Stew', 'Lamb Kebab with yogurt', 
                        'Lamb Kebab', 'chicken kebab', 'Chicken Fried Rice Recipe', 
                        'Chicken Curry', 'Chicken Fried Rice', 'Fried Rice', 
                        'Well Done Steak', 'Mighty Medium Rare', 'Guacamole and Steak Chops', 
                        'Guacamole', 'Steak Chops', 'apple juice', 'orange juice', 'cranberry juice', 'rice']; // List of allowed words
    var content = document.getElementById('id_content').value.toLowerCase(); // Get the value of the content field, change all character to lowercase to increase case insensitivity
    var isValid = allowedWords.some(function(word) { // Check if any of the allowed words match the content
        return content.includes(word);//.toLowerCase()
    });
    if (!isValid) {
        var invalidWord = content.split(' ').find(function(word) {
            return !allowedWords.includes(word);
        });
        // Display custom error message modal
        var modal = document.getElementById('errorModal');
        var errorMessage = document.getElementById('errorMessage');
        errorMessage.textContent = 'We\'re sorry, "' + invalidWord + '" is currently not available.';
        modal.style.display = 'block';
        // Hide the modal after 5 seconds
        setTimeout(function() {
            closeModal();
        }, 5000);
        // Prevent form submission
        Event.preventDefault();
    }
}

function closeModal() {
    var modal = document.getElementById('errorModal');
    modal.style.display = 'none';
}