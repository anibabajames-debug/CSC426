document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');
    const formResponse = document.getElementById('formResponseMessage');

    // Reset UI states completely before validation
    usernameError.textContent = "";
    passwordError.textContent = "";
    formResponse.textContent = "";
    formResponse.className = "form-message"; 
    formResponse.style.display = "none";

    let isValid = true;

    // Client-side validation
    if (!usernameInput.value.trim()) {
        usernameError.textContent = "Username is required.";
        isValid = false;
    }
    if (!passwordInput.value.trim()) {
        passwordError.textContent = "Password is required.";
        isValid = false;
    }

    if (!isValid) return;

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                username: usernameInput.value.trim(),
                password: passwordInput.value
            })
        });

        const data = await response.json();

        formResponse.style.display = "block";
        formResponse.textContent = data.message;

        if (response.ok) { 
            formResponse.classList.add('success');
            
            // DELAYED REDIRECTION: Wait 1.5 seconds so the user can see the green success message
            setTimeout(() => {
                window.location.href = data.redirect_url;
            }, 1500);
            
        } else { 
            formResponse.classList.add('error');
        }
    } catch (error) {
        formResponse.style.display = "block";
        formResponse.textContent = "Unable to connect to server.";
        formResponse.classList.add('error');
    }
});

// Reset Button Handler
document.getElementById('resetBtn').addEventListener('click', function() {
    document.getElementById('loginForm').reset();
    document.getElementById('usernameError').textContent = "";
    document.getElementById('passwordError').textContent = "";
    
    const formResponse = document.getElementById('formResponseMessage');
    formResponse.textContent = "";
    formResponse.className = "form-message";
    formResponse.style.display = "none";
});