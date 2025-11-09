const form = document.getElementById("uploadForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const file = document.getElementById("imageInput").files[0];
  if (!file) return alert("Please select an image!");

  const formData = new FormData();
  formData.append("image", file);

  resultDiv.textContent = "Analyzing image... ⏳";

  try {
    // Replace this with your deployed backend URL for public use
    const response = await fetch("http://127.0.0.1:5000/analyze", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (data.error) {
      resultDiv.textContent = "Error: " + data.error;
      return;
    }

    resultDiv.innerHTML = `
      <h3>Prediction: ${data.label}</h3>
      <p>Confidence: ${(data.confidence * 100).toFixed(2)}%</p>
    `;
  } catch (err) {
    resultDiv.textContent = "Error connecting to backend: " + err;
  }
});
