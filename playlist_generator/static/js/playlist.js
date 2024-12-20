document
  .getElementById("playlist-form")
  .addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      mood: document.getElementById("mood").value,
      genre: document.getElementById("genre").value,
      activity: document.getElementById("activity").value,
    };

    try {
      const response = await fetch("/api/generate-playlist/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();

      if (response.ok) {
        displayPlaylist(result);
      } else {
        throw new Error(result.error || "Failed to generate playlist");
      }
    } catch (error) {
      displayError(error.message);
    }
  });

function displayPlaylist(songs) {
  const resultDiv = document.getElementById("playlist-result");
  const html = `
        <div class="card">
            <div class="card-body">
                <h3 class="card-title">Generated Playlist</h3>
                <ul class="list-group list-group-flush">
                    ${songs
                      .map(
                        (song) => `
                        <li class="list-group-item">
                            ${song.title} - ${song.artist}
                        </li>
                    `
                      )
                      .join("")}
                </ul>
                <button class="btn btn-success mt-3" onclick="savePlaylist()">Save Playlist</button>
            </div>
        </div>
    `;
  resultDiv.innerHTML = html;
}

function displayError(message) {
  const resultDiv = document.getElementById("playlist-result");
  resultDiv.innerHTML = `
        <div class="alert alert-danger">
            ${message}
        </div>
    `;
}

function getCookie(name) {
  let value = "; " + document.cookie;
  let parts = value.split("; " + name + "=");
  if (parts.length === 2) return parts.pop().split(";").shift();
}
