// ===== APPOINTMENT BOOKING FUNCTION =====
function bookAppointment(doctorName) {
    alert(`Заявка на запись к врачу: ${doctorName}\n\nСпасибо за обращение! В ближайшее время с вами свяжется администратор для подтверждения времени приема.\n\nТелефон: +7 (495) 123-45-67`);
}

// ===== SMOOTH SCROLLING FOR NAVIGATION =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===== NAVBAR STYLING ON SCROLL =====
window.addEventListener('scroll', function() {
    const nav = document.querySelector('.nav');
    if (window.scrollY > 50) {
        nav.style.background = 'rgba(255, 255, 255, 0.98)';
        nav.style.boxShadow = '0 2px 15px rgba(0, 0, 0, 0.15)';
    } else {