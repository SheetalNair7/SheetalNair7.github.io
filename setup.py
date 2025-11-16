import os

# Folder structure
folders = [
    "css",
    "js",
    "data",
    "images/reviews"
]

for f in folders:
    os.makedirs(f, exist_ok=True)

print("Folders created!")

# ---------- index.html ----------
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sheetal’s Transformational Services</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<section class="hero">
  <h1>Step Into Your Transformation</h1>
  <p>Curated energy healing and soul guidance sessions designed to align, awaken, and empower.</p>
</section>

<div id="services-container" style="max-width:900px; margin:40px auto; padding:0 20px;"></div>

<section id="reviews">
  <h2>What Clients Say</h2>
  <div id="reviews-list" class="reviews-container"></div>
</section>

<script src="js/main.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("index.html created!")

# ---------- style.css ----------
style_css = """
body, html { margin: 0; padding: 0; font-family: sans-serif; background: #faf5f0; }
.hero { background: linear-gradient(135deg, #ffecd2, #fcb69f); height: 60vh; display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center; }
.accordion { background:#fff; padding:18px; width:100%; border-radius:10px; cursor:pointer; margin-bottom:10px; box-shadow:0 5px 15px rgba(0,0,0,0.1); }
.panel { display:none; background:#fff; padding:15px 20px; border-radius:10px; margin-bottom:20px; }
.reviews-container { background:#fff; padding:20px; border-radius:10px; }
"""

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(style_css)

print("style.css created!")

# ---------- main.js ----------
main_js = """
// Load Services
fetch('data/services.json')
  .then(res => res.json())
  .then(services => {
    let container = document.getElementById("services-container");
    container.innerHTML = "";
    services.forEach(s => {
      container.innerHTML += `
        <button class="accordion">${s.title}</button>
        <div class="panel">
          <p>${s.description}</p>
          <p>Price: ${s.price}</p>
          <a href="${s.upi}" target="_blank">Pay via UPI</a>
        </div>
      `;
    });
    activateAccordions();
  });

// Load Reviews
fetch('data/reviews.json')
  .then(res => res.json())
  .then(reviews => {
    let list = document.getElementById("reviews-list");
    list.innerHTML = "";
    reviews.forEach(r => list.innerHTML += `<blockquote>${r}</blockquote>`);
  });

function activateAccordions() {
  var acc = document.getElementsByClassName("accordion");
  for (let i = 0; i < acc.length; i++) {
    acc[i].onclick = function () {
      this.classList.toggle("active");
      let panel = this.nextElementSibling;
      panel.style.display = panel.style.display === "block" ? "none" : "block";
    };
  }
}
"""

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(main_js)

print("main.js created!")

# ---------- services.json ----------
services_json = """
[
  {
    "title": "Energy Healing Session",
    "description": "60-minute personalized session to realign your energy, release blockages, and restore clarity.",
    "price": "₹1000",
    "upi": "https://pay.google.com/yourupi"
  },
  {
    "title": "Akashic Record Reading",
    "description": "Discover your soul’s blueprint and life path in a 45-minute reading that awakens your inner knowing.",
    "price": "₹1500",
    "upi": "https://pay.google.com/yourupi"
  }
]
"""

with open("data/services.json", "w", encoding="utf-8") as f:
    f.write(services_json)

print("services.json created!")

# ---------- reviews.json ----------
reviews_json = """
[
  "Sheetal’s energy healing transformed my week! – Priya",
  "Insightful Akashic reading. Felt empowered. – Rahul",
  "Professional, kind, and deeply intuitive. – Ananya"
]
"""

with open("data/reviews.json", "w", encoding="utf-8") as f:
    f.write(reviews_json)

print("reviews.json created!")

print("\n✨ Project setup complete, Sheetu! ✨")
