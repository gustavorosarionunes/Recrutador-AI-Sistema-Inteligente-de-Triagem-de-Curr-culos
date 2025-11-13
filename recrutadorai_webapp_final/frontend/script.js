const API_URL = "http://127.0.0.1:8000";

const uploadBtn = document.getElementById("uploadBtn");
const analyzeBtn = document.getElementById("analyzeBtn");
const fileInput = document.getElementById("files");
const jobSelect = document.getElementById("vaga");
const rankingDiv = document.getElementById("ranking");

uploadBtn.addEventListener("click", async () => {
  const files = fileInput.files;
  if (!files.length) return alert("Selecione pelo menos um currículo!");

  const formData = new FormData();
  for (let f of files) formData.append("files", f);

  const res = await fetch(`${API_URL}/upload`, { method: "POST", body: formData });
  alert(res.ok ? "✅ Currículos enviados!" : "❌ Erro no envio.");
});

analyzeBtn.addEventListener("click", async () => {
  const vaga = jobSelect.value;
  if (!vaga) return alert("Selecione uma vaga!");

  const res = await fetch(`${API_URL}/analyze`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ job_description: vaga }),
  });

  const data = await res.json();
  showRanking(data.ranking, vaga);
});

function showRanking(ranking, vaga) {
  rankingDiv.innerHTML = `<h3>📊 Ranking para ${vaga}</h3>`;
  ranking.forEach((r, i) => {
    rankingDiv.innerHTML += `
      <div>
        <strong>${i + 1}. ${r.filename}</strong><br>
        Compatibilidade: <b>${(r.score * 100).toFixed(1)}%</b>
      </div>
    `;
  });
}
