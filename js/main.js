// Load services dynamically
fetch('services.json')
  .then(res => res.json())
  .then(services => {
    const container = document.getElementById('services-container');
    services.forEach(service => {
      const accBtn = document.createElement('button');
      accBtn.className = 'accordion';
      accBtn.innerText = service.title;

      const panel = document.createElement('div');
      panel.className = 'panel';
      panel.innerHTML = `
        <p>${service.description}</p>
        <p>Price: ${service.price}</p>
        <a href="${service.paymentLink}" target="_blank">Pay via PhonePe</a>
      `;

      container.appendChild(accBtn);
      container.appendChild(panel);

      accBtn.onclick = function() {
        this.classList.toggle("active");
        panel.style.display = (panel.style.display === "block") ? "none" : "block";
      }
    });
  });

// Animate accordions on scroll
function animateAccordions() {
  document.querySelectorAll('.accordion').forEach(a => {
    if(a.getBoundingClientRect().top < window.innerHeight - 50) { a.classList.add('visible'); }
  });
}
window.addEventListener('scroll', animateAccordions);
window.addEventListener('load', animateAccordions);

// Animate review screenshots
function animateReviews() {
  document.querySelectorAll('.reviews-container img').forEach(img => {
    if(img.getBoundingClientRect().top < window.innerHeight - 50) { img.classList.add('visible'); }
  });
}
window.addEventListener('scroll', animateReviews);
window.addEventListener('load', animateReviews);
