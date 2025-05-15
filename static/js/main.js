// Greeting based on time of day
function showGreeting() {
    // Check if user has just logged in
    const justLoggedIn = sessionStorage.getItem('justLoggedIn');
    
    // Only show greeting if user just logged in
    if (justLoggedIn === 'true') {
        const hour = new Date().getHours();
        let message = "";
        if (hour < 12) {
            message = "Good morning! Welcome to Cognifyz Technologies.";
        } else if (hour < 18) {
            message = "Good afternoon! Welcome to Cognifyz Technologies.";
        } else {
            message = "Good evening! Welcome to Cognifyz Technologies.";
        }

        // Use custom alert instead of default alert
        showCustomAlert(message);
        
        // Reset the login flag so alert doesn't show on subsequent page loads
        sessionStorage.removeItem('justLoggedIn');
    }
}

// Custom Alert Functions
function showCustomAlert(message) {
    const alertBox = document.getElementById("custom-alert");
    const alertMessage = document.getElementById("custom-alert-message");
    alertMessage.textContent = message;
    alertBox.style.display = "flex";
}

function closeCustomAlert() {
    document.getElementById("custom-alert").style.display = "none";
}

// Button color change function
function changeColor() {
    const button = document.getElementById("colorBtn");
    const colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c"];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    button.style.backgroundColor = randomColor;
}

// Enhanced calculator function using the API
function calculateViaApi() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    
    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById("result").textContent = "Please enter valid numbers";
        return;
    }
    
    // Call the API endpoint
    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            num1: num1,
            num2: num2,
            operation: 'add'  // Default to addition
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById("result").textContent = `Result: ${data.result}`;
        } else {
            document.getElementById("result").textContent = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("result").textContent = "An error occurred during calculation";
    });
}

// Mobile menu toggle
function toggleMenu() {
    const mainNav = document.querySelector('.main-nav');
    mainNav.classList.toggle('active');
}

// Image Modal
function openModal(img) {
    const modal = document.getElementById("imageModal");
    const enlargedImg = document.getElementById("enlargedImage");

    modal.style.display = "flex";
    enlargedImg.src = img.src;
}

function closeModal() {
    document.getElementById("imageModal").style.display = "none";
}

// Image Slideshow
let slideIndex = 0;

function showSlides() {
    const slides = document.getElementsByClassName("slideshow-slide");

    if (slides.length === 0) return;

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slideIndex++;

    if (slideIndex > slides.length) {
        slideIndex = 1;
    }

    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 3000); // Change image every 3 seconds
}

// You might want to add event listeners for calculator buttons:
document.addEventListener('DOMContentLoaded', function() {
    const calcButton = document.getElementById('calculate-button');
    if (calcButton) {
        calcButton.addEventListener('click', calculateViaApi);
    }
});

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners for custom alert close buttons
    const closeBtn = document.querySelector('.custom-alert-close');
    const okButton = document.querySelector('.custom-alert-button');
    
    if (closeBtn) {
        closeBtn.addEventListener('click', closeCustomAlert);
    }
    
    if (okButton) {
        okButton.addEventListener('click', closeCustomAlert);
    }
    
    // Existing code...
    // Check if we're on a page with slideshow
    if (document.querySelector('.slideshow-slide')) {
        showSlides();
    }

    // Show greeting if appropriate
    showGreeting();
});