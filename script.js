const form = document.getElementById("uploadForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const file = document.getElementById("imageInput").files[0];
  if (!file) return alert("Please select an image!");

  const formData = new FormData();
  formData.append("image", file);

  resultDiv.textContent = "Analyzing image... ⏳";

  // Replace with your deployed backend URL
  const response = await fetch("https://your-backend-url.com/analyze", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();

  if (data.error) {
    resultDiv.textContent = data.error;
    return;
  }

  resultDiv.innerHTML = `
    <h3>Prediction: ${data.label}</h3>
    <p>Confidence: ${(data.confidence * 100).toFixed(2)}%</p>
  `;
});
